# Author: Mia Zhou
# 14 January 2026

import pygame
import random

# Colours
WHITE = (255, 255, 255)
GREEN = (255, 0, 0)
BLACK = (0, 0, 0)

# Constants
WIDTH = 800
HEIGHT = 600
SCREENSIZE = (WIDTH, HEIGHT)

# Other Constants
FPS = 60
SEAL_X = 300
SEAL_Y = 200
SEAL_SPEED = 5

# Seal Class
class Seal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = SEAL_X
        self.rect.y = SEAL_Y
        seal_x = random.randint(50, WIDTH // 2)
        seal_y = random.randint(50, HEIGHT // 2)

        self.rect.x = seal_x
        self.rect.y = seal_y

        self.speed_x = random.choice([-SEAL_SPEED, SEAL_SPEED])
        self.speed_y = random.choice([-SEAL_SPEED, SEAL_SPEED])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

# Score and Comic Sans Font
score = 0
font = pygame.font.Font("Comic Sans", 36)
# Clock for controlling fps
clock = pygame.time.Clock()
# Initialize pygame
pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Seal Game")
# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    all_sprites.update()

    # Draw game objects
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

# Quit pygame
pygame.quit()
