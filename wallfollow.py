import RoboPiLib as RPL
import time
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 0
motorR = 1
sensor_L = 16
sensor_M = 17
sensor_R = 18
analog_1 = 0
i = 3

def forward():
    RPL.servoWrite(0, 1400)
    RPL.servoWrite(1, 1600)
    print "Forward"
def stop():
    RPL.servoWrite(0, 0)
    RPL.servoWtire(1, 0)
    print "stop"
def right():
    RPL.servoWrite(1, 1550)
    RPL.servoWrite(0, 1440)
    print "Turning Right"
def left():
    RPL.servoWrite(0, 1460)
    RPL.servoWrite(1, 1550)
    print "Turning Left"
    
while True:
    sensor = RPL.analogRead(0)
    move_forward = False 
    move_left = False
    move_right = False
    go_stop = False
    
    if sensor > 400:
        move_right = True
    elif sensor > 200:
        move_forward = True
    else:
        move_left = True
   
    if move_forward:
        forward()
    elif go_stop:
        stop()
    elif move_left:
        left()
    elif move_right:
        right()


