"""
Need to know:
- how to get pygame template and run it.
    - white background, blue circle

Today:
- learn about the parts of a pygame program.
- draw some shapes.
- use the pygame documentation [docs] for reference.
"""

# pygame template

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_x = 200
circle_y = 200

# ---------------------------

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
    screen.fill((255, 255, 255))  # always the first drawing command
    # (DISPLAY, COLOR, LOCATION [of the center], SIZE [of the radius])
    pygame.draw.circle(screen, (0, 0, 225), (circle_x, circle_y), 30)
    pygame.draw.circle(screen, "dark green", (300, 400), 20)

    # Create shapes
    pygame.draw.rect(screen, "#F8C063", (300, 100, 200, 200))
    pygame.draw.polygon(screen, "#AAA0EB", [(400, 300), (450, 400), (300, 280)])
    pygame.draw.ellipse(screen, "#D6729E", (100, 300, 180, 320))
    pygame.draw.arc(screen, "black", (50, 50, 200, 400), 1.24, 3.14)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()