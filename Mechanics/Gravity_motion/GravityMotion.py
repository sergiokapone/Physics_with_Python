#!/usr/bin/env python3
#https://fiftyexamples.readthedocs.io/en/latest/gravity.html
from numpy import sqrt
from turtle import *
from scipy import constants as const
G = const.G

# Assumed scale: 100 pixels = 1AU.
AU = (149.6e6 * 1000)     # 149.6 million km, in meters.
SCALE = 250 / AU
title("Gravity of bodies")

class Body(Turtle):
    """Subclass of Turtle representing a gravitationally-acting body.

    Extra attributes:
    mass : mass in kg
    vx, vy: x, y velocities in m/s
    px, py: x, y positions in m
    """
    name = 'Body'
    mass = None
    vx = vy = 0.0
    px = py = 0.0
    
    def attraction(self, other):
        """(Body): (fx, fy)

        Returns the force exerted upon this body by the other body.
        """
        # Report an error if the other object is the same as this one.
        if self is other:
            raise ValueError("Attraction of object %r to itself requested"
                             % self.name)

        # Compute the distance of the other body.
        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox-sx)
        dy = (oy-sy)
        r = sqrt(dx**2 + dy**2)

        # Report an error if the distance is zero; otherwise we'll
        # get a ZeroDivisionError exception further down.
        if r == 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.name, other.name))

        # Compute the force of attraction
        f = G * self.mass * other.mass / r**2# / (sqrt(1 - 2*1000000*G*other.mass/(r*c**2)))

        # Compute the direction of the force.
        fx = dx/r * f
        fy = dy/r * f
        return fx, fy

def update_info(step, bodies):
    """(int, [Body])

    Displays information about the status of the simulation.
    """
    print('Step #{}'.format(step))
    for body in bodies:
        s = '{:<8}  Pos.={:>6.2f} {:>6.2f} Vel.= {:>10.3f} {:>10.3f}'.format(
            body.name, body.px/AU, body.py/AU, body.vx, body.vy)
        print(s)


def loop(bodies):
    """([Body])

    Never returns; loops through the simulation, updating the
    positions of all the provided bodies.
    """
    timestep = 1/10 * 24 * 3600  #Timestep in seconds

    step = 0

    while True:
        #Initialization
        for body in bodies:
            body.penup()
            body.goto(body.px*SCALE, body.py*SCALE)
        step += 1
        update_info(step, bodies)
        
        for body in bodies:
            body.pendown()
            total_fx = total_fy = 0.0
            
            # Add up all of the forces exerted on 'body'.
            for other in bodies:
                # Don't calculate the body's attraction to itself
                if body is other:
                    continue
                fx, fy = body.attraction(other)
                total_fx += fx
                total_fy += fy

            # Record the total force exerted.
            fx, fy = total_fx, total_fy
            
            # Update velocities based upon on the force.
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep
           
            # Update positions
            body.px += body.vx * timestep
            body.py += body.vy * timestep
            body.goto(body.px*SCALE, body.py*SCALE)

            #body.dot(3)
            body.pendown()
def main():
    sun = Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30
    sun.color('orange')
    sun.shape('circle')
    
    earth = Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10**24
    earth.px = -1*AU
    earth.vy = 29.783 * 1000            # 29.783 km/sec
    earth.pencolor('blue')
    #earth.hideturtle()
    earth.color('blue')
    earth.shapesize(0.5,0.5,0.5)
    earth.shape('circle')
    
    # venus parameters taken from
    # http://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html
    venus = Body()
    venus.name = 'Venus'
    venus.mass = 4.8685 * 10**24
    venus.px = 0.723 * AU
    venus.vy = -35.02 * 1000
    venus.pencolor('red')
    #venus.hideturtle()
    venus.color('red')
    venus.shapesize(0.5,0.5,0.5)
    venus.shape('circle')
    
    mercury = Body()
    mercury.name = 'Mercury'
    mercury.mass = 3.30104 * 10**23
    mercury.px = 0.307499 * AU
    mercury.vy = -58.98 * 1000
    mercury.pencolor('blue')
    #mercury.hideturtle()
    mercury.color('brown')
    mercury.shapesize(0.25,0.25,0.25)
    mercury.shape('circle')
    
    mars = Body()
    mars.name = 'Mars'
    mars.mass = 6.4171 * 10**23
    mars.px = 1.3814 * AU
    mars.vy = -26.50 * 1000
    mars.pencolor('blue')
    #mars.hideturtle()
    mars.color('red')
    mars.shapesize(0.4,0.4,0.4)
    mars.shape('circle')
    
    
    loop([sun, mercury, venus, mars])

if __name__ == '__main__':
    main()