import RoboPiLib as RPL
import time
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

def forward():
    RPL.servoWrite(1, 1400)
    RPL.servoWrite(2, 1600)
    print "Forward"
def reverse():
    RPL.servoWrite(1, 1600)
    RPL.servoWrite(2, 1400)
    print "stop"
def start_right():
    RPL.servoWrite(2, 1550)
    RPL.servoWrite(1, 1420)
    print "Turning Right"
def start_left():
    RPL.servoWrite(1, 1460)
    RPL.servoWrite(2, 1550)
    print "Turning Left"

    
while True:
    sensorL = RPL.digitalRead(22)
    sensorM = RPL.digitalRead(20)
    sensorR = RPL.digitalRead(23)
    move_forward = False
    move_left = False
    move_right = False
    go_reverse = False
    
    
    if sensorL == 1:
        move_right = True
    elif sensorM == 1:
        go_reverse = True
    elif sensorR == 1:
        move_left = True
    else:
        move_forward = True
   
   
    if move_forward:
        forward()
    elif go_reverse:
        reverse()
    elif move_left:
        start_left()
    elif move_right:
        start_right()
   
