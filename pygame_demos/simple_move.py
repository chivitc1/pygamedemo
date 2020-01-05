import pygame, sys

size = w, h = 640, 320
pygame.init()
screen = pygame.display.set_mode(size, 0, 32)
background = pygame.image.load('images/sushiplate.jpg').convert()
clock = pygame.time.Clock()

rect_color = 0, 255, 0
rect_size = 40, 40

x = 0
speed = 250 # pixel / second

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, rect_color, pygame.Rect((x, 100), rect_size))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed

    x += distance_moved
    if x > w:
        x -= w

    pygame.display.flip()
    # pygame.time.wait(10)