import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Параметри задачі
river_width = 400  # ширина річки в метрах
swimmer_speed = 4  # швидкість рибалки в м/с
current_speed = 3  # швидкість течії в м/с

# Час перепливання (однаковий в обох випадках)
crossing_time = river_width / swimmer_speed  # 100 секунд

distance = np.sqrt(river_width ** 2 + (current_speed * crossing_time ) ** 2)

# Налаштування графіку
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Перепливання річки рибалкою: порівняння без течії та з течією', fontsize=14)

# График 1: Без течения
ax1.set_xlim(-50, 450)
ax1.set_ylim(-50, 450)
ax1.set_xlabel('Відстань по течії (м)')
ax1.set_ylabel('Ширина річки (м)')
ax1.set_title('Без течії')
ax1.grid(True, alpha=0.3)
ax1.set_aspect('equal')  # Рівний масштаб осей

# Береги річки
ax1.axhline(y=0, color='brown', linewidth=3)
ax1.axhline(y=river_width, color='brown', linewidth=3)
ax1.fill_between([0, 400], 0, river_width, alpha=0.2, color='lightblue')

# Береги річки
ax2.axhline(y=0, color='brown', linewidth=3)
ax2.axhline(y=river_width, color='brown', linewidth=3)
ax2.fill_between([0, 400], 0, river_width, alpha=0.2, color='lightblue')

# Графік 2: З течією річки
ax2.set_xlim(-50, 450)
ax2.set_ylim(-50, 450)
ax2.set_xlabel('Відстань по течії (м)')
ax2.set_ylabel('Ширина річки (м)')
ax2.set_title('З течією 3 м/с')
ax2.grid(True, alpha=0.3)
ax2.set_aspect('equal')  # Рівний масштаб осей

# Стрілки течії
for i in range(50, 400, 50):
    for j in range(50, river_width, 50):
        ax2.arrow(i, j, 20, 0, head_width=10, head_length=10,
                  fc='blue', ec='blue', alpha=0.5)

# Ініціалізація точок рибалки та стрілок швидкості
swimmer1, = ax1.plot([], [], 'ro', markersize=8, label='Рибалка')
trail1, = ax1.plot([], [], 'r--', alpha=0.7, label='Траєкторія')
swimmer2, = ax2.plot([], [], 'ro', markersize=8, label='Рибалка')
trail2, = ax2.plot([], [], 'r--', alpha=0.7, label='Траєкторія')

# Список для зберігання стрілок швидкості
velocity_artists = []

# Текст для відображення часу
time_text1 = ax1.text(0.02, 0.98, '', transform=ax1.transAxes, fontsize=12,
                      verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
time_text2 = ax2.text(0.02, 0.98, '', transform=ax2.transAxes, fontsize=12,
                      verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Масиви для зберігання траєкторій
trail1_x, trail1_y = [], []
trail2_x, trail2_y = [], []

# Функція анімації
def animate(frame):
    # Очищаємо попередні стрілки швидкості
    for artist in velocity_artists:
        artist.remove()
    velocity_artists.clear()

    t = frame * 0.2  # Час у секундах (сповільнюємо анімацію)

    if t <= crossing_time:
        # Випадок 1: Без течії (або в системі відліку води)
        x1 = 0  # рибалка пливе прямо
        y1 = swimmer_speed * t

        # Випадок 2: З течією
        x2 = current_speed * t  # зміщення за течією
        y2 = swimmer_speed * t  # рух поперек річки

        # Оновлення позицій рибалок
        swimmer1.set_data([x1], [y1])
        swimmer2.set_data([x2], [y2])

        # Додавання точок до траєкторій
        trail1_x.append(x1)
        trail1_y.append(y1)
        trail2_x.append(x2)
        trail2_y.append(y2)

        # Оновлення траєкторій
        trail1.set_data(trail1_x, trail1_y)
        trail2.set_data(trail2_x, trail2_y)

        # Додавання стрілок швидкості
        # Випадок 1: швидкість тільки вгору (y-напрямок)
        velocity1 = ax1.arrow(x1, y1, 0, swimmer_speed * 10, head_width=10, head_length=10,
                              fc='green', ec='green', alpha=0.8, label='Швидкість')
        velocity_artists.append(velocity1)

        # Випадок 2: результуючий вектор швидкості (течія + рух рибалки)
        velocity2 = ax2.arrow(x2, y2, current_speed * 10, swimmer_speed * 10, head_width=10, head_length=10,
                              fc='green', ec='green', alpha=0.8, label='Швидкість')
        velocity_artists.append(velocity2)

        # Оновлення тексту часу
        time_text1.set_text(f'Час: {t:.1f} с\nПройдено: {y1:.1f} м')
        time_text2.set_text(f'Час: {t:.1f} с\nПройдено: {np.sqrt(y2 ** 2 + x2 ** 2):.1f} м\nЗнос: {x2:.1f} м')

    else:
        # Анімацію завершено, показуємо фінальні позиції
        time_text1.set_text(f'ФІНІШ!\nЧас: {crossing_time:.1f} с\nПройдено: {river_width} м')
        time_text2.set_text(f'ФІНІШ!\nЧас: {crossing_time:.1f} с\nПройдено: {distance:.1f} м\nЗнос: {current_speed * crossing_time:.1f} м')

    return [swimmer1, trail1, swimmer2, trail2, time_text1, time_text2] + velocity_artists

# Додавання легенд
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')

# Створення анімації
frames = int(crossing_time / 0.2) + 50  # додаткові кадри для показу результату
anim = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=False, repeat=True)

plt.tight_layout()
plt.show()

# Виведення розрахунків
print("="*60)
print("РОЗРАХУНКИ:")
print(f"Ширина річки: {river_width} м")
print(f"Швидкість рибалки: {swimmer_speed} м/с")
print(f"Швидкість течії: {current_speed} м/с")
print(f"Час перепливання: {crossing_time} с")
print(f"Зміщення по течії: {current_speed * crossing_time} м")
print("="*60)
print("ПОЯСНЕННЯ:")
print("Рибалка пливе поперек річки з постійною швидкістю 4 м/с.")
print("Течія НЕ впливає на час перепливання, тільки на траєкторію.")
print("В обох випадках рибалка перетинає річку за один і той же час!")
print("Зелені стрілки показують вектор швидкості рибалки: у лівому графіку — власна швидкість (вертикально), у правому — результуюча швидкість (з урахуванням течії).")
print("="*60)

# Збереження анімації у відеоформат
# Варіант 1: MP4 (потребує ffmpeg)
try:
    anim.save('rybalka_animation.mp4', writer='ffmpeg', fps=20, bitrate=1800)
    print("Анімація збережена як rybalka_animation.mp4")
except:
    print("Помилка збереження MP4. Перевірте, чи встановлено ffmpeg")

# Варіант 2: GIF
try:
    anim.save('rybalka_animation.gif', writer='pillow', fps=20)
    print("Анімація збережена як rybalka_animation.gif")
except:
    print("Помилка збереження GIF")
