import RoboPiLib as RPL
import time
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

i = 3

def forward():
    RPL.servoWrite(6, 1400)
    RPL.servoWrite(7, 1600)
    print "Forward"
def stop():
    RPL.servoWrite(6, 0)
    RPL.servoWtire(7, 0)
    print "stop"
def right():
    RPL.servoWrite(7, 1550)
    RPL.servoWrite(6, 1420)
    print "Turning Right"
def left():
    RPL.servoWrite(6, 1460)
    RPL.servoWrite(7, 1550)
    print "Turning Left"
def small_correct():
    RPL.servoWrite(6, 1460)
    RPL.servoWrite(7, 1550)
    print "small correction"
def large_correct():
    RPL.servoWrite(6, 1460)
    RPL.servoWrite(7, 1570)
    print "large correction"
    
while True:
    sensor_1 = RPL.analogRead(0)
    sensor_2 = RPL.analogRead(1)
    move_forward = False 
    move_left = False
    move_right = False
    go_stop = False
    go_small = False
    go_large = False
    
    if sensor_1 > 400:
        move_right = True
    elif sensor_1 > 200:
        move_forward = True
    else: 
        move_left = True
    
    if sensor_1 - sensor_2 > 200:
        go_small = True
    elif sensor_1 - sensor_2 > 350:
        go_large = True
    if sensor_2 - sensor_1 > 200:
        go_small = True
    elif sensor_2 - sensor_1 > 350:
        go_large = True

     
   
    if move_forward:
        forward()
    elif go_stop:
        stop()
    elif move_left:
        left()
    elif move_right:
        right()
    elif go_small:
        small_correct()
    elif go_large:
        large_correct()


