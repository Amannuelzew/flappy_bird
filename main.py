import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 864, 936
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("flappy bird")

# Set up game clock
clock = pygame.time.Clock()
ground_scroll = 0
scroll_speed = 4
bottom = 768
pip_gap = 150
pipe_frequency = 1500
last_time = pygame.time.get_ticks()-pipe_frequency
flying = False
game_over = False

bg = pygame.image.load('img/bg.png')
ground = pygame.image.load('img/ground.png')


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
        self.velocity = 0
        self.clicked = False

    def update(self) -> None:

        if flying:
            # gravity
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8
            if self.rect.top < 100:
                self.rect.top = 100

            if self.rect.bottom < bottom and self.rect.top >= 100:
                self.rect.y += int(self.velocity)
        if not game_over:
            # jump
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.velocity = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            # handle animation
            self.counter += 1
            flap_cool_down = 5
            if self.counter > flap_cool_down:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]
            # rotate
            self.image = pygame.transform.rotate(
                self.images[self.index], self.velocity * -2)


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/pipe.png')
        self.rect = self.image.get_rect()
        # position -1 for bottom pipe; 1 for top
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y-pip_gap]
        else:
            self.rect.topleft = [x, y+pip_gap]

    def update(self) -> None:
        self.rect.x -= scroll_speed


bird_group = pygame.sprite.Group()
flappy = Bird(100, width//2)
bird_group.add(flappy)

pipe_group = pygame.sprite.Group()


# Game loop
running = True
while running:

    # daw bg
    screen.blit(bg, (0, 0))
    # draw ground
    bird_group.draw(screen)
    bird_group.update()

    pipe_group.draw(screen)
    pipe_group.update()

    screen.blit(ground, (ground_scroll, bottom))

    if flappy.rect.bottom >= bottom:
        game_over = True
        flying = False
    if not game_over and flying:
        # generate pipes automatically
        now = pygame.time.get_ticks()
        if now-last_time > pipe_frequency:
            bottom_pipe = Pipe(width, width//2, -1)
            top_pipe = Pipe(width, width//2, 1)
            pipe_group.add(bottom_pipe)
            pipe_group.add(top_pipe)
            last_time = now
        ground_scroll -= scroll_speed
        # Each little bars on the ground image are 35 pixels
        if ground_scroll < -35:
            ground_scroll = 0

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not flying and not game_over:
            flying = True

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
