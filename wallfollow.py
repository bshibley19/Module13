import RoboPiLib as RPL
import time
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

sensor_pin = 27
RPL.pinMode(sensor_pin,RPL.INPUT)

RPL.analogRead(sensor_pin)
