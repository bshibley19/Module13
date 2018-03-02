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
    while RPL.analogRead(0) > 500 and RPL.analogRead(0) < 700:
        RPL.servoWrite(motorL, 0)
        RPL.servoWrite(motorR, 0)
        
    while RPL.analogRead(0) < 500:
        move = time.time()
        while move < time.time() + 1.5:
            RPL.servoWrite(motorL, 1450)
            RPL.servoWrite(motorR, 1530)
           
    while RPL.analogRead(0) > 700:
        cool = time.time()
        while move < time.time + 1.5:
            RPL.servoWrite(motorL, 0)
            RPL.servoWrite(motorR, 1530)
            
