#!/usr/bin/env pybricks-micropython

# Pybricks imports
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor)
from pybricks.parameters import Port, Stop, Direction, Button
from pybricks.tools import wait, StopWatch


# Other imports
import math


# Initialization and instantiation of Pybricks modules, and some constants
ev3 = EV3Brick()
x_motor = Motor(Port.A) # Egg rotation
y_motor = Motor(Port.C) # Pen motion across egg
z_motor = Motor(Port.B) # Moves pen towards/away from egg
timer = StopWatch()
button = TouchSensor(Port.S1) # Button

startSpeed = 10
topSpeed = 15

####################
# Helper functions #
####################

def returnToStartingPoint():
    """
    Resets the pen position to a known point by raising it,
    moving the pen all the way "up" the egg,
    then moving 50 degrees back down
    """
    z_motor.run_until_stalled(-70, duty_limit=50)
    y_motor.run_until_stalled(100, duty_limit=40)
    y_motor.reset_angle(0)
    y_motor.run_angle(50, -35)
    z_motor.reset_angle(0)
    y_motor.reset_angle(0)

def raisePen():
    """
    Raises the pen up from the egg
    """
    z_motor.run_until_stalled(-25, duty_limit=40)

def lowerPen():
    """
    Lowers the pen down towards the egg
    """
    z_motor.run_until_stalled(25, duty_limit=45)
    z_motor.reset_angle(0)

def setAngle(angle):
    """
    Moves the pen up or down lengthwise along the egg by a given angle
    """
    y_motor.run_angle(100, angle)
    
def stop():
    """
    Stops the motors responsible for rotating the egg and moving the pen across the egg
    """
    y_motor.stop()
    x_motor.stop()

#####################
# Drawing functions #
#####################
# These combine the above helpers with various motor control functions
# to create repeatable drawings and patterns.
# Note: every drawing functionassumes the pen to be floating before drawing starts, and so every
# drawing function starts with lowerPen() and ends with raisePen()
def drawWave(amplitude, frequency):
    """
    Draws a sine wave around the egg
    """
    lowerPen()
    x_motor.reset_angle(0)
    x_motor.dc(startSpeed)
    while(x_motor.angle() < 360):
        if x_motor.angle()+startSpeed < topSpeed: 
            x_motor.dc(x_motor.angle()+startSpeed)  #Increase speed over time
        angle = math.cos(frequency * math.radians(x_motor.angle())) * amplitude
        y_motor.run(angle)
    stop()
    raisePen()

def drawLine():
    """
    Draws a single straight line around the egg
    """
    lowerPen()
    x_motor.reset_angle(0)
    x_motor.run_angle(100, 365)
    x_motor.reset_angle(0)
    stop()
    raisePen()
    
def drawThickLine():
    """
    Draws a single straight line around the egg, with several passes for a thicker line
    """
    lowerPen()
    x_motor.reset_angle(0)
    x_motor.run_angle(400, 2880)
    x_motor.reset_angle(0)
    stop()
    raisePen()
    
def drawDottedLine(dots):
    """
    Draws a dotted line around the egg, with a given number of total dots
    """
    for i in range(dots):
        x_motor.run_angle(100, 360/dots)
        lowerPen()
        raisePen()
    
def drawYLine(n):
    """
    Draws a single line lengthwise along the egg
    """
    lowerPen()
    y_motor.run_angle(100, 20)
    y_motor.run_angle(100, -50)
    raisePen()
    
    for i in range(n-1):
        x_motor.run_angle(100, 360/n)
        lowerPen()
        y_motor.run_angle(100, 50)
        y_motor.run_angle(100, -50)
        raisePen()
        
def drawCircle(a):
    """
    Draws a circle on the egg, with circumference a
    """
    lowerPen()
    for angle in range(360):
        x_motor.run(1.5 * a * math.sin(math.radians(angle)))
        y_motor.run(a * math.cos(math.radians(angle)))
        if angle is not 360:
            wait(1)
    stop()
    raisePen()


######################
# Printing functions #
######################
# These functions combine the above functions in various ways to build intricate patterns

def drawPattern1():
    """
    Draws a wave function with straight lines around it
    There is a pause between the wave and the lines being drawn to allow user to change
    to a different colour if desired
    """
    drawWave(120, 10)

    ev3.screen.clear()
    ev3.screen.print("Press button to proceed")
    while not button.pressed():
        pass
    ev3.screen.print("Proceeding!")
    
    returnToStartingPoint()
    setAngle(-25)
    drawThickLine()
    setAngle(50)
    drawThickLine()
    
def drawPattern2():
    """
    Draws five evenly-spaced thick lines around the egg
    """
    setAngle(24)
    for x in range(5):
        drawThickLine()
        setAngle(-12)

def drawPattern3():
    """
    Draws a pattern of waves, separated by thick straight lines
    """
    setAngle(3)
    drawThickLine()
    
    ev3.screen.clear()
    ev3.screen.print("Press button to proceed")
    while not button.pressed():
        pass
    ev3.screen.print("Proceeding!")
    
    returnToStartingPoint()
    setAngle(-3)
    drawThickLine()

    ev3.screen.clear()
    ev3.screen.print("Press button to proceed")
    while not button.pressed():
        pass
    ev3.screen.print("Proceeding!")
        
    returnToStartingPoint()
    setAngle(-13)
    drawWave(75, 14)

    ev3.screen.clear()
    ev3.screen.print("Press button to proceed")
    while not button.pressed():
        pass
    ev3.screen.print("Proceeding!")
    
    returnToStartingPoint()
    setAngle(-18)
    drawThickLine()

    ev3.screen.clear()
    ev3.screen.print("Press button to proceed")
    while not button.pressed():
        pass
    ev3.screen.print("Proceeding!")
    
    returnToStartingPoint()
    setAngle(5)
    drawWave(75, 14)

    ev3.screen.clear()
    ev3.screen.print("Press button to proceed")
    while not button.pressed():
        pass
    ev3.screen.print("Proceeding!")

    returnToStartingPoint()
    setAngle(20)
    drawThickLine()
    
def drawPattern4():
    """
    Draws multiple thick lines around the egg,
    allowing the user to change pen colour for every line drawn
    """
    angle = 24
    for x in range(8):
        setAngle(angle)
        drawThickLine()

        ev3.screen.clear()
        ev3.screen.print("Press button to proceed")
        while not button.pressed():
            pass
        ev3.screen.print("Proceeding!")

        angle -= 8
        returnToStartingPoint()
        
def drawPattern5():
    """
    Draws a spiralling line from the top to the bottom of the egg,
    with thick lines at the very top and bottom of the spiral
    """
    setAngle(24)
    drawThickLine()
    x_motor.run(360)
    lowerPen()
    y_motor.run_until_stalled(-12, duty_limit=40)
    stop()
    drawThickLine()

def drawPattern6():
    """
    Draws a grid pattern on the egg
    """
    angle = 24
    for x in range(8):
        setAngle(angle)
        drawThickLine()
        angle -= 8
        returnToStartingPoint()

    ev3.screen.clear()
    ev3.screen.print("Press button to proceed")
    while not button.pressed():
        pass
    ev3.screen.print("Proceeding!")
    
    drawYLine(24)
    
def drawPattern7():
    """
    Draws a pattern consisting of two thick lines, a dotted line and two thick lines
    """ 
    setAngle(20)
    for x in range(2):
        drawThickLine()             
        setAngle(-10)
        ev3.screen.print("Next line")
        
    drawDottedLine(30)              
    setAngle(-10)
    ev3.screen.print("Next line")
    
    for x in range(2):
        drawThickLine()             
        setAngle(-10)
        ev3.screen.print("Next line")
        
def drawPattern8():
    """
    Uses multiple thicklines to create a coloured band around the egg
    """
    setAngle(24)
    for x in range(48):
        drawThickLine()
        setAngle(-1)
        
##############################
# Actual code to be executed #
##############################
# Code for the current egg to be drawn goes after this point

ev3.speaker.beep()

timer.reset()
returnToStartingPoint()

while timer.time() < 4000:
    pass

drawPattern1()

ev3.speaker.beep()
