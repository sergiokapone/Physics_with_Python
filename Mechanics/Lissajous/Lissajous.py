# -*- coding: utf-8 -*-

from turtle import Turtle, Screen
from math import pi, cos
from timeit import default_timer as timer


# %% class
class Body(Turtle):
    """
    Oscilating bodies.
    Amplitude - Object Amplitude
    omega     - Object Angular Velocity
    phi       - Phase Shift
    k1        - x Coordinate Angular Velocity amplifier
    k2        - y Coordinate Angular Velocity amplifier
    """

    def __init__(self, Amplitude=100, omega=1, k1=1, k2=1, phi=pi / 2):
        Turtle.__init__(self)
        self.Amplitude = Amplitude
        self.omega = omega
        self.k1 = k1
        self.k2 = k2
        self.phi = phi


timer_t = Turtle(visible=False)
timer_t.penup()
timer_t.setposition(300, 300)

global screen
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

    t0 = timer()  # strange nonzeroth starting value of time
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


def AxisDraw(axis, maxval):
    """
    Drawing Cartesian coordinates
    """
    axis.speed(0)
    axis.setposition(0, -maxval)
    axis.goto(0, maxval)
    axis.penup()
    axis.setposition(-maxval, 0)
    axis.pendown()
    axis.goto(maxval, 0)


# %% Main fumnction


def main():
    global screen
    screen = Screen()
    axis = Turtle(visible=False)
    AxisDraw(axis, 300)

    body1 = Body(Amplitude=200, omega=1, k1=1, k2=2, phi=0)
    body1.color("red")

    body2 = Body(Amplitude=200, omega=1, k1=1, k2=2, phi=pi / 2)
    body2.color("blue")

    loop([body1, body2])


if __name__ == "__main__":
    main()
    screen.mainloop()
