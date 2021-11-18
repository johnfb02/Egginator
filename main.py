#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import math

ev3 = EV3Brick()
x_motor = Motor(Port.A) # Rotates the ball
z_motor = Motor(Port.B) # Raises/lowers the pen
y_motor = Motor(Port.C) # Moves pen across ball

button = TouchSensor(Port.S1) #Button

startSpeed = 10
topSpeed = 15

timer = StopWatch()

def returnToStartingPoint(angle):
    z_motor.run_until_stalled(-70, duty_limit=50)
    y_motor.run_until_stalled(100, duty_limit=40)
    y_motor.reset_angle(0)
    y_motor.run_angle(50, -1 * angle)
    z_motor.reset_angle(0)
    y_motor.reset_angle(0)
    

def raisePen():
    z_motor.run_until_stalled(-25, duty_limit=40)

def lowerPen():
    z_motor.run_until_stalled(25, duty_limit=40)
    z_motor.reset_angle(0)
    #z_motor.run_angle(25, -5)

def startUp():
    returnToStartingPoint(35)
    z_motor.reset_angle(0)
    y_motor.reset_angle(0)
    
def stop():
    y_motor.stop()
    x_motor.stop()

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
    
def drawCircle(radius):
    #setAngle(radius)
    lowerPen()
    while(x_motor.angle() < radius*2):
        x_motor.dc(10)
        y_speed = (-x_motor.angle()-5)/(math.sqrt((-x_motor.angle()-5)**2 + radius**2))
        y_motor.run(y_speed*radius)

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
    
def drawYLine(n):
    for i in range(n):
        x_motor.run_angle(100, 360/n)
        lowerPen()
        y_motor.run_until_stalled(100, duty_limit=40)
        y_motor.run_angle(100, -65)
        raisePen()
        

def setAngle(angle):
    y_motor.run_angle(100, angle)

#-------------Differnt egg-prints------------------#
def printEgg1():
    drawWave(120, 10)
    setAngle(-15)
    drawThickLine()
    setAngle(30)
    drawThickLine()
    
def printEgg2():
    setAngle(30)
    for x in range(5):
        drawThickLine()
        setAngle(-15)
        
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
    setAngle(10)
    drawWave(75, 14)
    while (not button.pressed()):
        print("Trykk knapp for å fortsette")
    startUp()
    setAngle(20)
    drawThickLine()
    
def printEgg4():
    angle = 24
    for x in range(9):
        setAngle(angle)
        drawThickLine()
        while (not button.pressed()):
            print("Trykk knapp for å fortsette")
        angle -= 8
        startUp()
        
def printEgg5(): #Funker ikke ennå
    setAngle(20)
    lowerPen()
    drawThickLine()
    y_motor.run(-10)
    x_motor.run_angle(360, 1440)
    drawThickLine()
    stop()
    raisePen()

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
        
#----------------Main-function-----------------#
ev3.speaker.beep()

timer.reset()
startUp()

while timer.time() < 4000:
    pass

printEgg2()

ev3.speaker.beep()
