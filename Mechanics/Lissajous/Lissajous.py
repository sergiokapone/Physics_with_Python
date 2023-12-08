from turtle import Turtle, Screen
from math import pi, cos
from timeit import default_timer as timer


# %% class
class Body(Turtle):
    """
    Oscillating bodies.
    amplitude - Object Amplitude
    omega     - Object Angular Velocity
    phi       - Phase Shift
    k1        - x Coordinate Angular Velocity amplifier
    k2        - y Coordinate Angular Velocity amplifier
    """

    def __init__(self, amplitude: int = 100, omega: int = 1,
                 k1: int = 1, k2: int = 1,
                 phi: float = pi / 2) -> None:

        Turtle.__init__(self)
        self.Amplitude: int = amplitude
        self.omega: int = omega
        self.k1: int = k1
        self.k2: int = k2
        self.phi: float = phi


timer_t: Turtle = Turtle(visible=False)
timer_t.penup()
timer_t.setposition(300, 300)

# global screen
screen = Screen()
screen.tracer(0)


# %% loop function
def loop(bodies):
    """
    The movement of bodies in accordance with a sinusoidal law
    """
    for body in bodies:
        body.penup()
        body.showturtle()
        body.shape("circle")
        body.speed(1)

    t0 = timer()  # strange nonzero starting value of time
    while True:
        time = timer() - t0
        for body in bodies:
            body.x = body.Amplitude * cos(
                body.k1 * body.omega * time
            )  # x Coordinate law of motion
            body.y = body.Amplitude * cos(
                body.k2 * body.omega * time - body.phi
            )  # y Coordinate law of motion
            body.goto(body.x, body.y)
            body.pendown()

        timer_t.write("t = " + str(round(time, 2)))
        screen.update()
        timer_t.undo()


# %% Axis Draw


def axis_draw(axis, max_val) -> None:
    """
    Drawing Cartesian coordinates
    """
    axis.speed(0)
    axis.setposition(0, -max_val)
    axis.goto(0, max_val)
    axis.penup()
    axis.setposition(-max_val, 0)
    axis.pendown()
    axis.goto(max_val, 0)


# %% Main function


def main():
    global screen
    screen = Screen()
    axis: Turtle = Turtle(visible=False)
    axis_draw(axis, 300)

    body1: Body = Body(amplitude=200, omega=1, k1=1, k2=2, phi=0)
    body1.color("red")

    body2: Body = Body(amplitude=200, omega=1, k1=1, k2=2, phi=pi / 2)
    body2.color("blue")

    loop([body1, body2])


if __name__ == "__main__":
    main()
    screen.mainloop()
