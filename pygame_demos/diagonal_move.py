import pygame, sys

size = w, h = 640, 320
pygame.init()
screen = pygame.display.set_mode(size, 0, 32)
background = pygame.image.load('images/sushiplate.jpg').convert()
clock = pygame.time.Clock()

rect_color = 0, 255, 0
rect_size = 40, 40

x, y = 100, 100
speedx, speedy = 133, 170 # pixel / second

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, rect_color, pygame.Rect((x, y), rect_size))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    x += time_passed_seconds * speedx
    y += time_passed_seconds * speedy
    if x > w - rect_size[0]:
        speedx = -speedx
        x = w - rect_size[0]
    elif x < 0:
        speedx = -speedx
        x = 0

    if y > h - rect_size[1]:
        speedy = -speedy
        y = h - rect_size[1]
    elif y < 0:
        speedy = -speedy
        y = 0

    pygame.display.flip()
    # pygame.time.wait(10)