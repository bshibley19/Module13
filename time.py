import RoboPiLib as RPL
from setup import RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 0
time = time.time()
i = 3
e = 6

while True:
    while time.time() < time + i:
        RPL.servoWrite(motorR, 1000)
        RPL.servoWrite(motorL, 2000)
print(time.time)
    while time.time() > time + i and time.time() < time + e:
        RPL.servoWrite(motorR, 0)
        RPL.servoWrite(motorL, 0)

    while time.time() > time + e
        i = i + 4
        e = e + 4
