import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
import random
import math

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
dusk = ("#5d3c70")
night = ("#3c4370")

mountain = ("#ff9c9e")
snowcap = ("#ffded5")

ground = ("#e57082")
blossom = ("#fe4d57")

wood = ("#4a4275")
dark_wood = ("#1e2059")
light_wood = ("#944e72")
# ---------------------------

# CLASSES
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 50))
        self.image.fill(cloud_color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-50, WIDTH + 50)
        self.rect.y = random.randrange(0, HEIGHT / 3)
        self.speed = random.randrange(1, 3)

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.rect.x = random.randrange(-200, -50)
            self.rect.y = random.randrange(0, HEIGHT / 3)


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

class Petal:
    def __init__(self, x, y, speed, angle):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle

    def update(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))
        
        # wrap the petals around the screen
        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0
        if self.y > HEIGHT:
            self.y = random.randint(-50, 0)

    def draw(self):
        pygame.draw.circle(screen, blossom, (int(self.x), int(self.y)), 3)

# SETUP
# Clouds
clouds = pygame.sprite.Group()
for i in range(5):
    cloud = Cloud()
    clouds.add(cloud)

# Sun
sun = Sun()
sun_group = pygame.sprite.Group()
sun_group.add(sun)

# Moon
moon = Moon()
moon_group = pygame.sprite.Group()
moon_group.add(moon)

sky_color = night
is_day = False
is_dawn = False

# Mountains
center_x = WIDTH / 2
center_y = SCREEN_HEIGHT * 0.8
radius = 400

start_angle = -math.pi / 2
end_angle = math.pi / 2
angle_range = end_angle - start_angle

curve_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

mountain_range_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
mountain_range_surface.blit(curve_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

# Petals
petals = []
for i in range(50):
    x = random.randint(0, WIDTH)
    y = random.randint(-50, HEIGHT//2)
    speed = random.randint(1, 5)
    angle = random.randint(0, 45)
    petal = Petal(x, y, speed, angle)
    petals.append(petal)

# Cabin
cabin_width = 300
cabin_height = 100
cabin_x = 2 * WIDTH / 3 - cabin_width / 2
cabin_y = HEIGHT / 2 - cabin_height / 2

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
    pygame.draw.polygon(mountain_range_surface, mountain, [(0, HEIGHT / 2), (WIDTH / 3, HEIGHT / 3), (2 * WIDTH / 3, HEIGHT / 2), (WIDTH, HEIGHT / 2), (WIDTH, HEIGHT), (0, HEIGHT)])
    screen.blit(mountain_range_surface, (0, 0))

    # Foreground (the tower and gate and ground)
    for petal in petals:
        petal.update()
        petal.draw()
    screen.fill(ground, (0, HEIGHT // 2, WIDTH, HEIGHT))
    pygame.draw.rect(screen, dark_wood, (cabin_x, cabin_y, cabin_width, cabin_height))
    pygame.draw.polygon(screen, wood, [(cabin_x - 30, cabin_y), (cabin_x + cabin_width / 5, cabin_y - 40), (cabin_x + 4 * cabin_width / 5, cabin_y - 40), (cabin_x + cabin_width + 30, cabin_y)])
    pygame.draw.rect(screen, light_wood, (cabin_x + 20, cabin_y + 50, cabin_width - 40, cabin_height - 70))
    pygame.draw.rect(screen, wood, (cabin_x + cabin_width / 2 - 20, cabin_y + cabin_height - 50, 40, 50))
    pygame.draw.rect(screen, dark_wood, (cabin_x + cabin_width / 2 - 10, cabin_y + cabin_height - 40, 20, 10))

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------

pygame.quit()
