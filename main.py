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

timer = StopWatch()

def returnToStartingPoint(angle):
    z_motor.run_until_stalled(70, duty_limit=50)
    y_motor.run_until_stalled(100, duty_limit=40)
    y_motor.reset_angle(0)
    y_motor.run_angle(25, -1 * angle)
    z_motor.reset_angle(0)
    y_motor.reset_angle(0)
    

def raisePen():
    z_motor.run_until_stalled(25, duty_limit=50)

def lowerPen():
    z_motor.run_until_stalled(-25, duty_limit=29)
    z_motor.reset_angle(0)
    z_motor.run_angle(25, 10)

def startUp():
    returnToStartingPoint(42.5)
    
def stop():
    y_motor.stop()
    x_motor.stop()

def drawWave(amplitude, frequency):
    lowerPen()
    x_motor.dc(15)
    x_motor.reset_angle(0)
    while(x_motor.angle() < 362):
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

def setAngle(angle):
    y_motor.run_angle(100, angle)

ev3.speaker.beep()

timer.reset()
startUp()

while timer.time() < 4000:
    pass

setAngle(-20)

for i in range(2):
    drawWave(90, 10)
    setAngle(40)

ev3.speaker.beep()
