import RoboPiLib as RPL
from setup import RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

print "Please type in the pin number of your motors."
b = int(raw_input("Left Motor > "))
c = int(raw_input("Right Motor > "))
motorL = b
motorR = c


RPL.servoWrite(motorR, 0)
RPL.servoWrite(motorL, 0)
