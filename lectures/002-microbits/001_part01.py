# Imports go at the top
from microbit import *
import random

x = 2
y = 4

# Code in a 'while True:' loop repeats forever
while True:
    # player code
    if (button_a.was_pressed() and x - 1 >= 0):
        display.set_pixel(x, y, 0)
        x -= 1;
    if (button_b.was_pressed() and x + 1 <= 4):
        display.set_pixel(x, y, 0)
        x += 1;
    display.set_pixel(x, y, 9)
    sleep(1000/30)