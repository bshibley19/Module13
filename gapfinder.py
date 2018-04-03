import RoboPiLib as RPL
import time
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motor_L = 6
motor_R = 7

analog_1 = 0
analog_2 = 1

RPL.servoWrite = motor
RPL.analogRead = sensor

i =3

def move_forward:
  motor(motor_L, 1400)
  motor(motor_R, 1600)

def slightTurn_R:
  motor(motor_L, )
  motor(motor_R, )
  
def slightTurn_L:
  motor(motor_L, )
  motor(motor_R, )

def largeTurn_R:
  motor(motor_L, )
  motor(motor_R, )

def largeTurn_L:
  motor(motor_L, )
  motor(motor_R, )
  
  
