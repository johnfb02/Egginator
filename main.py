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

startSpeed = 10
topSpeed = 20

timer = StopWatch()

def returnToStartingPoint(angle):
    z_motor.run_until_stalled(-70, duty_limit=50)
    y_motor.run_until_stalled(100, duty_limit=40)
    y_motor.reset_angle(0)
    y_motor.run_angle(50, -1 * angle)
    z_motor.reset_angle(0)
    y_motor.reset_angle(0)
    

def raisePen():
    z_motor.run_until_stalled(-25, duty_limit=50)

def lowerPen():
    z_motor.run_until_stalled(25, duty_limit=35)
    z_motor.reset_angle(0)
    z_motor.run_angle(25, -12.5)

def startUp():
    returnToStartingPoint(35)
    
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
    setAngle(radius)
    lowerPen()
    for a in range(360):
        x_motor.run(math.sin(math.radians(a)))
        y_motor.run(math.cos(math.radians(a)))
    raisePen()

def drawLine():
    lowerPen()
    x_motor.reset_angle(0)
    x_motor.run_angle(100, 365)
    x_motor.reset_angle(0)
    stop()
    raisePen()

def setAngle(angle):
    y_motor.run_angle(100, angle)

#-------------Differnt egg-prints------------------#
def printEgg1():
    drawWave(60, 10)
    setAngle(-15)
    drawLine()
    setAngle(30)
    drawLine()


ev3.speaker.beep()

timer.reset()
startUp()

while timer.time() < 4000:
    pass

drawCircle(5)

#printEgg1()

ev3.speaker.beep()
