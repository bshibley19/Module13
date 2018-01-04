import RoboPiLib as RPL
from setup import RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 0
sensor_pin = 24

RPL.servoWrite(motorR, 1000)
RPL.servoWrite(motorL, 2000)
RPL.pinMode(sensor_pin,RPL.INPUT)

if RPL.digitalRead() == 0:
    while True:
        while time.time() < time.time() + 0.2:
            RPL.servoWrite(motorR, 750)
            RPL.servoWrite(motorL, 1750)
        while time.time() < time.time() + 0.4:
            RPL.servoWrite(motorR, 500)
            RPL.servoWrite(motorL, 1500)
        while time.time() < time.time() + 0.6:
            RPL.servoWrite(motorR, 0)
            RPL.servoWrite(motorL, 0)
