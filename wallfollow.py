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

while True:
    while RPL.analogRead(0) > 550 and RPL.analogRead(0) < 600:
        RPL.servoWrite(motorL, 1000)
        RPL.servoWrite(motorR, 1000)
        if RPL.analogRead(0) < 550:
            break
        if RPL.analogRead(0) > 600:
            break
        
    while RPL.analogRead(0) < 550:
        move = time.time()
        while move < time.time() + 1.5:
            RPL.servoWrite(motorL, 1450)
            RPL.servoWrite(motorR, 1530)
        else: 
            break
        
    while RPL.analogRead(0) > 600:
        cool = time.time()
        while move < time.time + 1.5:
            RPL.servoWrite(motorL, 1465)
            RPL.servoWrite(motorR, 1530)
        else: 
            break
         
