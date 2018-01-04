import RoboPiLib as RPL
from setup import RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 0
sensor_pin = 24
import RoboPiLib as RPL
from setup import RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 0
sensor_pin = 24
motorR_forward = 2000
motorL_forward = 1000

RPL.servoWrite(motorR, 2000)
RPL.servoWrite(motorL, 1000)
RPL.pinMode(sensor_pin,RPL.INPUT)

def forwardSpeedChanges(change, mn = 1600, mx = 2900):
  global motorR_forward
  global motorL_forward
  motorR_forward += change
  motorL_forward += change
  motorR_forward = max(min(motorR_forward, mx), mn)
  motorL_forward = max(min(motorL_forward, mx), mn)
  print_speed()

if RPL.digitalRead(sensor_pin) == 0:
    while RPL.digitalRead(sensor_pin) == 0:
        while time.time() < time.time() + 0.2:
            forwardSpeedChanges(-100)
        while time.time() < time.time() + 0.4:
            forwardSpeedChanges(-500)
        while time.time() < time.time() + 0.6:
            RPL.servoWrite(motorR, 0)
            RPL.servoWrite(motorL, 0)

def forwardSpeedChanges(change, mn = 1600, mx = 2900):
  global motorR_forward
  global motorL_forward
  motorR_forward += change
  motorL_forward += change
  motorR_forward = max(min(motorR_forward, mx), mn)
  motorL_forward = max(min(motorL_forward, mx), mn)
  print_speed()
