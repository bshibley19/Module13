import RoboPiLib as RPL
from setup import RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 0


RPL.servoWrite(motorR, 1000)
RPL.servoWrite(motorL, 2000)
