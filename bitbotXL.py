# Tobias Johansen - tobiaj@hiof.no
from microbit import *
import neopixel #Neopixel library controls the NeoPixels lights on the bitbot

#Neopixel code is modified and taken from l33t.uk/bitbot
np = neopixel.NeoPixel(pin13, 12)

#Methods that alter the lights on bitbot
def right_lights(Red, Green, Blue):
    for pixel_id in range(6, 12):
        np[pixel_id] = (Red, Green, Blue)
    np.show()

def left_lights(Red, Green, Blue):
    for pixel_id in range(0, 6):
        np[pixel_id] = (Red, Green, Blue)
    np.show()
    
    
    
#Line Sensor
I2CADDR = 0x1c

def getLine(bit):
    mask = 1 << bit
    value = 0
    try:
        value = i2c.read(I2CADDR, 1)[0]
    except OSError:
        pass
    if (value & mask) > 0:
        return 1
    else:
        return 0

#Motor functions
def move_forward():
    pin14.write_analog(250)
    pin12.write_analog(0)
    pin16.write_analog(250)
    pin8.write_analog(0)

def move_left():
    pin14.write_analog(250)
    pin12.write_analog(0)
    pin16.write_analog(0)
    pin8.write_analog(0)

def move_right():
    pin16.write_analog(250)
    pin8.write_analog(0)
    pin14.write_analog(0)
    pin12.write_analog(0)
    
def stop():
    pin14.write_analog(0)
    pin12.write_analog(0)
    pin16.write_analog(0)
    pin8.write_analog(0)


while True:
    left_line = getLine(0)
    right_line = getLine(1)
    if(left_line == 1):
        left_lights(200,0,0)
        move_left()
    elif(right_line == 1):
        right_lights(200,0,0)
        move_right()
    elif(left_line == 0) and (right_line == 0):
        right_lights(0,200,0)
        left_lights(0,200,0)
        move_forward()
    else:
        left_lights(0,200,0)
        right_lights(0,200,0)
