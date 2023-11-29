# -*- coding: utf-8 -*-
from turtle import Turtle, Screen
from math import pi, sin, cos
from timeit import default_timer as timer


body = Turtle(shape="circle", visible=False)   # Черепашка, яка імітує фізичне тіло
body.color('red')
body.penup()

mody = Turtle(shape="circle", visible=False)   # Черепашка, яка імітує фізичне тіло
mody.color('blue')
mody.penup()

time_t = Turtle(visible=False)                 # Черепашка, яка виводить час руху
rotation_number = Turtle(visible=False)        # Черепашка, яка виводить число обертів
positionx  = Turtle(visible=False)             # Черепашка, яка виводить координату x body
positiony  = Turtle(visible=False)             # Черепашка, яка виводить координату x body
Amplitude  = Turtle(visible=False)             # Черепашка, яка виводить амплітуду
AngularVelocity  = Turtle(visible=False)       # Черепашка, яка виводить кутову швидкість
Ratio  = Turtle(visible=False)                 # Черепашка, яка виводить відношення кутових швидкостей
RotationPeriod  = Turtle(visible=False)        # Черепашка, яка виводить період обертання
Phi  = Turtle(visible=False)                   # Черепашка, яка виводить зсув фаз
axis = Turtle(visible=False)                   # Черепашка, яка рисує координатні осі
font = ("Consolas", 12, "normal")


# Рисування координатних осей
def AxisDraw(axis, maxval):
    axis.speed(0)
    axis.setposition(0,-maxval)
    axis.goto(0,maxval)
    axis.penup()
    axis.setposition(-maxval,0)
    axis.pendown()
    axis.goto(maxval,0)

# Функція motion() рухає черепашку body

def output_in_screen(self, x_coord, y_coord, string):
    self.undo()
    self.penup()
    self.setposition(x_coord, y_coord)
    self.write(string,font = font)

# define gcd function
def gcd(x, y):
   """This function implements the Euclidian algorithm
   to find G.C.D. of two numbers"""
   while(y):
       x, y = y, x % y
   return x

def motion(self, A, omega, k1, k2, phi, t):
    #---------------- Кінематичні закони руху ---------------------
    Period = 2*pi/(gcd(k1,k2)*omega)
    def x(t):
        return A * cos(k1 * omega * t)        # Координата body  x

    def y(t):
        return A * cos(k2 * omega * t - phi)  # Координата body y

    self.setposition(x(t), y(t)) # Положення  черепашки body
    self.showturtle()
    self.pendown()

    # ------------------------------- Виведенні змінних на екран ----------------------------------------------------
    output_in_screen(time_t, -300, 320, "t = " + str(round(t, 2)) )
    output_in_screen(RotationPeriod, -300, 300, "T = " + str(round(Period,2)))
    output_in_screen(positionx, 300, 320, "x = " + str( round(x(t),2)))
    output_in_screen(positiony, 300, 300, "y = " + str( round(y(t),2)))
    output_in_screen(Amplitude, -300, -260, "A     = " + str(A) )
    output_in_screen(AngularVelocity, -300, -280, "omega = " + str(omega))
    output_in_screen(Ratio, -300, -300, "ratio = " + str(k1) + "/"+ str(k2))
    output_in_screen(Phi, -300, -320, "phi = " + str(phi))

    screen.update()
    # ---------------------------------------------------------------------------------------------------------------

    n = int( round(t, 2) / round(Period, 2) )
    output_in_screen(rotation_number, -300, 280, "n = " + str(n))


AxisDraw(axis, 300)

screen = Screen()
screen.tracer(0)
# -------------------------- Константи ----------------------------
A     = 200
omega = 1
k1    = 1
k2    = 3
while True:
      t = timer()
      motion(body, A, omega, k1, k2, pi/2, t)
#screen.exitonclick()


