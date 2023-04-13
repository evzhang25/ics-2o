import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_a, K_d, K_LEFT, K_RIGHT
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

# ---------------------------

class Character():
    player_x = 400
    player_y = HEIGHT - 10
    player_rect = pygame.Rect(player_x - 10, player_y - 10, 20, 20)

    def move_left():
        if (player_x - 10 >= 0):
            player_x -= 20
    def move_right():
        if (player_x + 10 <= WIDTH):
            player_x += 20

playable_character = Character()

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_a or event.key == K_LEFT:
                playable_character.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                playable_character.move_right()
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    screen.fill("white")
    pygame.draw.rect(screen, "blue", playable_character.player_rect)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------

pygame.quit()
