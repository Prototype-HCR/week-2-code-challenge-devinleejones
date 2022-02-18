import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

# create a neopixel object
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
pixels.brightness = 0.1

# create colors as tuple values
pink = 0xf15bb5
blue = 0x84e6f8
purple = 0x7209b7

# set color coded pixels on board, left side pink, right side blue, center purple
pixels[0] = pink
pixels[1] = pink
pixels[2] = pink
pixels[3] = purple
pixels[4] = purple
pixels[5] = purple
pixels[6] = purple
pixels[7] = blue
pixels[8] = blue
pixels[9] = blue
time.sleep(4)

#  declare digital inputs for both buttons
button_a = DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=Pull.DOWN)
button_b = DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=Pull.DOWN)

led_state = True

while True:
    # gather all input values from sensors
    button_a_read = button_a.value
    button_b_read = button_b.value

    # set outputs based on the value of my variables
    if button_a_read and button_b_read == True:
        # turn the neopixels purple
        pixels.fill(purple)
    elif button_a_read == True:
        # turn the neopixels pink
        pixels.fill(pink)
    elif button_b_read == True:
        pixels.fill(blue)
        # turn the neopixels blue
    else:
        pixels.fill(0)
        print('Press the A button for pink, Press the B button for blue, or Press both for Purple!')
        # print instructions in Serial when no buttons are being pressed

    time.sleep(0.1)
