import RoboPiLib as RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 7
motorR = 6
sensor_R = 16
sensor_M = 17
sensor_L = 18
i = 3

RPL.servoWrite(motorR, 2000)
RPL.servoWrite(motorL, 1000)

while RPL.digitalRead(sensor_R) or RPL.digitalRead(sensor_M) or RPL.digitalRead(sensor_L)!= 1:
	while RPL.digitalRead(sensor_R) == 0:
   		cool = time.time()
   		while time.time() < (cool + i):
        		RPL.servoWrite(motorL, 1490)
        		RPL.servoWrite(motorR, 2000)
		if time.time() > (cool + i):
        		RPL.servoWrite(motorL, 1000)
        		RPL.servoWrite(motorR, 2000)
	while RPL.digitalRead(sensor_L) == 0:
    		fun = time.time()
    		while time.time() < (fun + i):
        		RPL.servoWrite(motorL, 1000)
        		RPL.servoWrite(motorR, 1510)
		if time.time() > (fun + i):
        		RPL.servoWrite(motorL, 1000)
        		RPL.servoWrite(motorR, 2000)
	while RPL.digitalRead(sensor_M) == 0:
    		brad = time.time()
    		while time.time() < (brad + i):
        		RPL.servoWrite(motorL, 1000)
        		RPL.servoWrite(motorR, 1510)
		if time.time() > (brad + i):
        		RPL.servoWrite(motorL, 1000)
        		RPL.servoWrite(motorR, 2000)
	while RPL.digitalRead(sensor_M) and RPL.digitalRead(sensor_L) == 0:
    		me = time.time()
    		while time.time() < (me + i):
        		RPL.servoWrite(motorL, 1000)
        		RPL.servoWrite(motorR, 1510)
		if time.time() > (me + i):
        		RPL.servoWrite(motorL, 1000)
        		RPL.servoWrite(motorR, 2000)
	while RPL.digitalRead(sensor_M) and RPL.digitalRead(sensor_R) == 0:
   		hi = time.time()
   		while time.time() < (hi + i):
        		RPL.servoWrite(motorL, 1490)
        		RPL.servoWrite(motorR, 2000)
		if time.time() > (hi + i):
        		RPL.servoWrite(motorL, 1000)
        		RPL.servoWrite(motorR, 2000)
	
