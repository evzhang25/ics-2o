import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
import random

pygame.init()

WIDTH = 800
SCREEN_HEIGHT = 600
HEIGHT = 3 * SCREEN_HEIGHT / 2
SIZE = (WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
moon_color = ("#F6F1D5")
sun_color = ("#f14052")
cloud_color = ("#FFE2E2")

day = ("#ffafac")
dawn = ("#ffb287")
dusk = ("#ff8037")
night = ("#3c4370")

ground = ("#e57082")
# ---------------------------


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 50))
        self.image.fill(cloud_color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-200, -50)
        self.rect.y = random.randrange(0, HEIGHT / 2)
        self.speed = random.randrange(1, 3)

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH:
            self.rect.x = random.randrange(-200, -50)
            self.rect.y = random.randrange(0, HEIGHT / 2)


class Sun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.image.fill(sun_color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 4, HEIGHT // 4)
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top <= 0:
            self.speed = 1
        elif self.rect.bottom >= HEIGHT:
            self.speed = -1


class Moon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.image.fill(moon_color)
        self.rect = self.image.get_rect()
        self.rect.center = (3 * WIDTH // 4, 3 * HEIGHT // 4)
        self.speed = -1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top <= 0:
            self.speed = 1
        elif self.rect.bottom >= HEIGHT:
            self.speed = -1

clouds = pygame.sprite.Group()
for i in range(5):
    cloud = Cloud()
    clouds.add(cloud)

sun = Sun()
sun_group = pygame.sprite.Group()
sun_group.add(sun)

moon = Moon()
moon_group = pygame.sprite.Group()
moon_group.add(moon)

sky_color = night
is_day = False
is_dawn = False

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
    clouds.update()
    sun_group.update()
    moon_group.update()

    # DRAWING
    # Background (the sky)
    if sun.rect.center[1] <= HEIGHT // 3:
        sky_color = day
        is_day = True
        is_dawn = False
    elif sun.rect.center[1] >= HEIGHT // 3 and sun.rect.center[1] <= 2 * HEIGHT // 3:
        if sun.rect.center[1] <= HEIGHT // 2:
            sky_color = dawn
        else:
            sky_color = dusk
        is_dawn = True
        if (sun.rect.center[1] <= HEIGHT // 2):
            is_day = True
        else:
            is_day = False
    elif sun.rect.center[1] >= 2 * HEIGHT // 3:
        sky_color = night
        is_day = False
        is_dawn = False

    screen.fill(sky_color)

    if is_dawn:
        sun_group.draw(screen)
        moon_group.draw(screen)
    elif is_day:
        sun_group.draw(screen)
    else:
        moon_group.draw(screen)

    clouds.draw(screen)

    # Foreground (the tower and gate and ground)
    screen.fill(ground, (0, HEIGHT // 2, WIDTH, HEIGHT))

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------

pygame.quit()
