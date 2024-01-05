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
# Game loop
running = True
while running:

    # daw bg
    screen.blit(bg, (0, 0))
    # draw ground
    screen.blit(ground, (ground_scroll, 485))
    ground_scroll -= scroll_speed
    if ground_scroll < -35:
        ground_scroll = 0
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
