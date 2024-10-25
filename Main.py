# import modules
from machine import Pin, PWM
import picoexplorer as display
import utime
import random


# set up screen
buf = bytearray(display.get_width() * display.get_height() * 2)
display.init(buf)

while True:    
    
    # fill the screen blue
    display.set_pen(100, 100, 225)
    display.clear()         

    # draw title
    display.set_pen(225, 255, 255)
    display.text("CanSat- fulford", 0, 0, 240, 4)
    
   
    
    if display.is_pressed(display.BUTTON_A):
        display.text("A", 0, 50, 240, 8)
    elif display.is_pressed(display.BUTTON_B):
            display.text("B", 0, 150, 240, 8)
   
    
    display.update()
    utime.sleep(0.1)

