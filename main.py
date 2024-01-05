from typing import Any
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 545, 620
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("flappy bird")

# Set up game clock
clock = pygame.time.Clock()

bg = pygame.image.load('img/bg.png')
ground = pygame.image.load('img/ground.png')

ground_scroll = 0
scroll_speed = 4


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load('img/bird1.png'),
                       pygame.image.load('img/bird2.png'), pygame.image.load('img/bird3.png')]
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self) -> None:
        self.counter += 1
        flap_cool_down = 5
        if self.counter > flap_cool_down:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]


bird_group = pygame.sprite.Group()
flappy = Bird(100, width//2)
bird_group.add(flappy)
# Game loop
running = True
while running:

    # daw bg
    screen.blit(bg, (0, 0))
    # draw ground
    screen.blit(ground, (ground_scroll, 485))
    ground_scroll -= scroll_speed
    # Each little bars on the ground image are 35 pixels
    if ground_scroll < -35:
        ground_scroll = 0

    bird_group.draw(screen)
    bird_group.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
