import RoboPiLib as RPL
from setup import RPL
import time
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 7
sensor_pin = 16
i = 4.9

while RPL.digitalRead(sensor_pin) == 1:
    PTW.state['d0'] = RPL.digitalRead(sensor_pin)
    PTW.state['m1'] = RPL.digitalRead(sensor_pin)
    PTW.state['m7'] = RPL.digitalRead(sensor_pin)
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    PTW.post()
    if RPL.digitalRead(sensor_pin) != 1:
        break

while RPL.digitalRead(sensor_pin) == 0:
    PTW.state['d0'] = RPL.digitalRead(sensor_pin)
    move = time.time()
    PTW.post()
    while time.time() < (move + i):
        PTW.state['m1'] = RPL.digitalRead(sensor_pin)
        PTW.state['m7'] = RPL.digitalRead(sensor_pin)
        RPL.servoWrite(motorR, 1475)
        RPL.servoWrite(motorL, 1520)
        PTW.post()
    while time.time() > (move + i):
        PTW.state['m1'] = RPL.digitalRead(sensor_pin)
        PTW.state['m7'] = RPL.digitalRead(sensor_pin)
        RPL.servoWrite(motorR, 0)
        RPL.servoWrite(motorL, 0)
        PTW.post()
