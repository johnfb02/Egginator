#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import math

"""

    Initializing modules

"""
ev3 = EV3Brick()
x_motor = Motor(Port.A) # Rotates the ball
z_motor = Motor(Port.B) # Raises/lowers the pen
y_motor = Motor(Port.C) # Moves pen across ball

button = TouchSensor(Port.S1) #Button

startSpeed = 10
topSpeed = 15

timer = StopWatch()

"""

    Utility-functions

"""

def returnToStartingPoint():
    z_motor.run_until_stalled(-70, duty_limit=50)
    y_motor.run_until_stalled(100, duty_limit=40)
    y_motor.reset_angle(0)
    y_motor.run_angle(50, -35)
    z_motor.reset_angle(0)
    y_motor.reset_angle(0)
    

def raisePen():
    z_motor.run_until_stalled(-25, duty_limit=40)

def lowerPen():
    z_motor.run_until_stalled(25, duty_limit=45)
    z_motor.reset_angle(0)
    #z_motor.run_angle(25, -5)

def startUp():
    returnToStartingPoint()
    z_motor.reset_angle(0)
    y_motor.reset_angle(0)
    
def stop():
    y_motor.stop()
    x_motor.stop()

"""

    Draw-functions

"""

def drawWave(amplitude, frequency):
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
    lowerPen()
    x_motor.reset_angle(0)
    x_motor.run_angle(100, 365)
    x_motor.reset_angle(0)
    stop()
    raisePen()
    
def drawThickLine():
    lowerPen()
    x_motor.reset_angle(0)
    x_motor.run_angle(400, 2880)
    x_motor.reset_angle(0)
    stop()
    raisePen()
    
def drawDottedLine(dots):
    for i in range(dots):
        x_motor.run_angle(100, 360/dots)
        lowerPen()
        raisePen()
    
def drawYLine(n):
    lowerPen()
    y_motor.run_angle(100, 20)
    y_motor.run_angle(100, -50)
    raisePen()
    
    for i in range(n-1):
        x_motor.run_angle(100, 360/n)
        lowerPen()
        #y_motor.run_until_stalled(100, duty_limit=40)
        y_motor.run_angle(100, 50)
        y_motor.run_angle(100, -50)
        raisePen()
        
def drawCircle(a):
    lowerPen()
    for angle in range(360):
        x_motor.run(1.5 * a * math.sin(math.radians(angle)))
        y_motor.run(a * math.cos(math.radians(angle)))
        if angle is not 360:
            wait(1)
    stop()
    raisePen()

def setAngle(angle):
    y_motor.run_angle(100, angle)

"""

    Egg prints

"""
#Wave with two lines outside of it
def printEgg1():
    drawWave(120, 10)
    while (not button.pressed()):
            print("Trykk knapp for å fortsette")
    startUp()
    setAngle(-25)
    drawThickLine()
    setAngle(50)
    drawThickLine()
    
#Five thick Lines
def printEgg2():
    setAngle(24)
    for x in range(5):
        drawThickLine()
        setAngle(-12)
        
#Lines with waves between
def printEgg3(): 
    setAngle(3)
    drawThickLine()
    while (not button.pressed()):
        print("Trykk knapp for å fortsette")
    startUp()
    setAngle(-3)
    drawThickLine()
    while (not button.pressed()):
        print("Trykk knapp for å fortsette")
    startUp()
    setAngle(-13)
    drawWave(75, 14)
    while (not button.pressed()):
        print("Trykk knapp for å fortsette")
    startUp()
    setAngle(-18)
    drawThickLine()
    while (not button.pressed()):
        print("Trykk knapp for å fortsette")
    startUp()
    setAngle(5)
    drawWave(75, 14)
    while (not button.pressed()):
        print("Trykk knapp for å fortsette")
    startUp()
    setAngle(20)
    drawThickLine()
    
#Multiple lines
def printEgg4():
    angle = 24
    for x in range(8):
        setAngle(angle)
        drawThickLine()
        while (not button.pressed()):
            print("Trykk knapp for å fortsette")
        angle -= 8
        startUp()
        
#Work in progress
def printEgg5(): #Funker ikke ennå
    setAngle(24)
    drawThickLine()
    x_motor.run(360)
    lowerPen()
    y_motor.run_until_stalled(-12, duty_limit=40)
    stop()
    drawThickLine()

#Grid
def printEgg6():
    angle = 24
    for x in range(8):
        setAngle(angle)
        drawThickLine()
        angle -= 8
        startUp()
    while (not button.pressed()):
            print("Trykk knapp for å fortsette")
    drawYLine(24)
    
#Thick lines and dotted line
def printEgg7(): 
    setAngle(20)
    for x in range(2):
        drawThickLine()             
        setAngle(-10)
        print("Next line")
        
    drawDottedLine(30)              
    setAngle(-10)
    print("Next line")
    
    for x in range(2):
        drawThickLine()             
        setAngle(-10)
        print("Next line")
        
def printEgg8():
    setAngle(24)
    for x in range(48):
        drawThickLine()
        setAngle(-1)
        
"""

    Main run

"""
ev3.speaker.beep()

timer.reset()
startUp()

while timer.time() < 4000:
    pass

#n = 8
#for i in range(n):
#    drawCircle(150)
#    returnToStartingPoint()
#    x_motor.run_angle(100, 360/n)

printEgg1()

ev3.speaker.beep()
