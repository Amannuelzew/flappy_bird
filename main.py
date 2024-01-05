import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 545, 585
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("flappy bird")

# Set up game clock
clock = pygame.time.Clock()

bg = pygame.image.load('img/bg.png')
ground = pygame.image.load('img/ground.png')

# Game loop
running = True
while running:

    screen.blit(bg, (0, 0))
    screen.blit(ground, (0, 485))
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
