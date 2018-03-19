import RoboPiLib as RPL
import time
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 7
sensor_R = 16
sensor_M = 17
sensor_L = 18
i = 3

while RPL.digitalRead(sensor_R) or RPL.digitalRead(sensor_M) or RPL.digitalRead(sensor_L)== 1:
    while RPL.digitalRead(sensor_R) == 0:
        move = time.time()
        while time.time() < (move + i):
            RPL.servoWrite(motorR, 1490)
            RPL.servoWrite(motorL, 1520)
            PTW.post()
        while time.time() > (move + i):
            RPL.servoWrite(motorR, 1460)
            RPL.servoWrite(motorL, 1550)
            PTW.post()
    while RPL.digitalRead(sensor_L) == 0:
        run = time.time()
        while time.time() < (run + i):
            RPL.servoWrite(motorR, 1520)
            RPL.servoWrite(motorL, 1490)
            PTW.post()
        while time.time() > (run + i):
            RPL.servoWrite(motorR, 1550)
            RPL.servoWrite(motorL, 1460)
            PTW.post()
    while RPL.digitalRead(sensor_M) == 0:
    	fun = time.time()
    	while time.time() < (fun + i):
        	RPL.servoWrite(motorL, 1000)
        	RPL.servoWrite(motorR, 1510)
	if time.time() > (fun + i):
        	RPL.servoWrite(motorL, 1000)
        	RPL.servoWrite(motorR, 2000)
    while RPL.digitalRead(sensor_M) and RPL.digitalRead(sensor_L) == 0:
    	go = time.time()
    	while time.time() < (go + i):
        	RPL.servoWrite(motorL, 1000)
        	RPL.servoWrite(motorR, 1510)
	if time.time() > (go + i):
        	RPL.servoWrite(motorL, 1000)
        	RPL.servoWrite(motorR, 2000)
    while RPL.digitalRead(sensor_M) and RPL.digitalRead(sensor_R) == 0:
   	brad = time.time()
   	while time.time() < (brad + i):
        	RPL.servoWrite(motorL, 1490)
        	RPL.servoWrite(motorR, 2000)
	if time.time() > (brad + i):
        	RPL.servoWrite(motorL, 1000)
        	RPL.servoWrite(motorR, 2000)
