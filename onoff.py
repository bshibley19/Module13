import RoboPiLib as RPL
from setup import RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 0
sensor_pin = 16

RPL.servoWrite(motorR, 1000)
RPL.servoWrite(motorL, 1000)
RPL.pinMode(sensor_pin,RPL.INPUT)

if RPL.digitalRead(sensor_pin) == 0:
    RPL.servoWrite(motorR, 0)
    RPL.servoWrite(motorL, 0)
