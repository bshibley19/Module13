import RoboPiLib as RPL
from setup import RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 7
sensor_pin = 16
move = time.time()
i = 5
j = 0.7


RPL.pinMode(sensor_pin,RPL.INPUT)
RPL.servoWrite(motorR, 1000)
RPL.servoWrite(morotL, 1000)

#if RPL.digitalRead(sensor_pin) == 0:
while time.time() < (move + i):
    RPL.servoWrite(motorR, 1480)
    RPL.servoWrite(motorL, 1520)
while time.time() > (move + i):
    RPL.servoWrite(motorR, 0)
    RPL.servoWrite(motorL, 0)
