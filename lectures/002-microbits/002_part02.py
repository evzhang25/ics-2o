# Imports go at the top
from microbit import *
import random

def run_game(highscore):
    player_x = 2
    player_y = 4

    while (not button_a.was_pressed()):
        if (button_b.was_pressed()):
            display.scroll(highscore)
            sleep(500)
        display.set_pixel(player_x, player_y, 9)
        sleep(500)
        display.set_pixel(player_x, player_y, 0)
        sleep(500)
    
    object_x = random.randint(0, 4)
    object_y = 0
    laser_x = random.randint(0, 4)
    laser_time = random.randint(1, 10) * 5
    frame = 0
    score = 0
    
    while True:
        if (frame % 5) == 0:
            display.set_pixel(object_x, object_y, 0)
            if (object_y + 1 <= 4):
                object_y += 1
            else:
                object_x = random.randint(0, 4)
                object_y = 0
                score += 1
            if (object_x == player_x and object_y == player_y):
                break

        if (frame == laser_time):
            frame = 0
            display.set_pixel(laser_x, 0, 3)
            display.set_pixel(laser_x, 1, 3)
            display.set_pixel(laser_x, 2, 3)
            display.set_pixel(laser_x, 3, 3)
            display.set_pixel(laser_x, 4, 3)
            sleep(250)
            display.set_pixel(laser_x, 0, 0)
            display.set_pixel(laser_x, 1, 0)
            display.set_pixel(laser_x, 2, 0)
            display.set_pixel(laser_x, 3, 0)
            display.set_pixel(laser_x, 4, 0)
            sleep(250)
            display.set_pixel(laser_x, 0, 3)
            display.set_pixel(laser_x, 1, 3)
            display.set_pixel(laser_x, 2, 3)
            display.set_pixel(laser_x, 3, 3)
            display.set_pixel(laser_x, 4, 3)
            sleep(250)
            display.set_pixel(laser_x, 0, 0)
            display.set_pixel(laser_x, 1, 0)
            display.set_pixel(laser_x, 2, 0)
            display.set_pixel(laser_x, 3, 0)
            display.set_pixel(laser_x, 4, 0)
            sleep(250)
            display.set_pixel(laser_x, 0, 3)
            display.set_pixel(laser_x, 1, 3)
            display.set_pixel(laser_x, 2, 3)
            display.set_pixel(laser_x, 3, 3)
            display.set_pixel(laser_x, 4, 3)
            sleep(250)
            display.set_pixel(laser_x, 0, 0)
            display.set_pixel(laser_x, 1, 0)
            display.set_pixel(laser_x, 2, 0)
            display.set_pixel(laser_x, 3, 0)
            display.set_pixel(laser_x, 4, 0)
            sleep(250)

            display.set_pixel(laser_x, 0, 9)
            display.set_pixel(laser_x, 1, 9)
            display.set_pixel(laser_x, 2, 9)
            display.set_pixel(laser_x, 3, 9)
            display.set_pixel(laser_x, 4, 9)
            if (player_x == laser_x):
                break
            sleep(500)
            display.set_pixel(laser_x, 0, 0)
            display.set_pixel(laser_x, 1, 0)
            display.set_pixel(laser_x, 2, 0)
            display.set_pixel(laser_x, 3, 0)
            display.set_pixel(laser_x, 4, 0)

            laser_x = random.randint(0, 4)
            
        # player code
        if (button_a.was_pressed() and player_x - 1 >= 0):
            display.set_pixel(player_x, player_y, 0)
            player_x -= 1;
        if (button_b.was_pressed() and player_x + 1 <= 4):
            display.set_pixel(player_x, player_y, 0)
            player_x += 1;
    
        display.set_pixel(object_x, object_y, 9)
        display.set_pixel(player_x, player_y, 6)
        frame += 1
        
        sleep(1000/30)

    if (highscore < score):
        highscore = score
    display.scroll(score)
    sleep(1000)

    return highscore

highscore = 0
while (True):
    highscore = run_game(highscore)