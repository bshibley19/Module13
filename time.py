import RoboPiLib as RPL
from setup import RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 0
t_end = time.time() + 3

while time.time() < t_end
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
