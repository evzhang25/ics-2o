import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
cloud_x = []
cloud_y = []
# ---------------------------

class cloud:
    ellipse_x = []
    ellipse_y = []

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    

    # DRAWING
    screen.fill("#8290AC")
    screen.fill("#515F7A", (0, 0, WIDTH, 120))
    screen.fill("#00827D", (0, 400, WIDTH, HEIGHT))
    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()