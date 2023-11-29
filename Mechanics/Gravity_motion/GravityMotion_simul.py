# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:46:43 2016

@author: Sergiokapone
"""

from GravityMotion import *

sun = Body()
sun.name = "Sun"
sun.mass = 1.98892 * 10**30
sun.pencolor("red")
sun.color("orange")
sun.shape("circle")

earth = Body()
earth.name = "Earth"
earth.mass = 5.9742 * 10**24
earth.px = -1 * AU
earth.vy = 29.783 * 1000  # 29.783 km/sec
earth.pencolor("blue")
# earth.hideturtle()
earth.color("blue")
earth.shapesize(0.5, 0.5, 0.5)
earth.shape("circle")

# Venus parameters taken from
# http://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html
venus = Body()
venus.name = "Venus"
venus.mass = 4.8685 * 10**24
venus.px = 0.723 * AU
venus.vy = -35.02 * 1000
venus.pencolor("red")
# venus.hideturtle()
venus.color("red")
venus.shapesize(0.5, 0.5, 0.5)
venus.shape("circle")

mercury = Body()
mercury.name = "Mercury"
mercury.mass = 3.30104 * 10**23
mercury.px = 0.307499 * AU
mercury.vy = -58.98 * 1000
mercury.pencolor("blue")
# mercury.hideturtle()
mercury.color("brown")
mercury.shapesize(0.25, 0.25, 0.25)
mercury.shape("circle")

mars = Body()
mars.name = "Mars"
mars.mass = 6.4171 * 10**23
mars.px = 1.3814 * AU
mars.vy = -26.50 * 1000
mars.pencolor("blue")
# mars.hideturtle()
mars.color("red")
mars.shapesize(0.4, 0.4, 0.4)
mars.shape("circle")

comet = Body()
comet.name = "comet"
comet.mass = 2.2 * 10**15
comet.px = 0.2 * AU
comet.vy = -90.56 * 1000
comet.pencolor("brown")
# comet.hideturtle()
comet.color("brown")
comet.shapesize(0.1, 0.1, 0.1)
comet.shape("circle")


loop([sun, mercury, venus, earth, mars, comet])
