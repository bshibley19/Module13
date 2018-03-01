import RoboPiLib as RPL
import time
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 7
sensor_L = 16
sensor_M = 17
sensor_R = 18
analog_1 = 0
j = 3
i = 4.0

RPL.servoWrite(motorR, 1000)
RPL.servoWrite(motorL, 2000)

while RPL.analogRead(analog_1) > 460 and RPL.analogRead(analog_1) < 800:
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    if RPL.digitalRead(sensor_R) != 1 or RPL.analogRead < 420:
        break

while RPL.analogRead(analog_1) < 460 and RPL.analogRead(analog_1) > 200:
    move = time.time()
    while time.time() < (move + 1):
        RPL.servoWrite(motorR, 1530)
        RPL.servoWrite(motorL, 1460)
    while time.time() > (move + 1):
        break
    
