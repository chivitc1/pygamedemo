import pygame, sys

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.RESIZABLE, 32) #create a graphical window

pygame.display.set_caption("Hello")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        print(event)
    screen.fill(black) # erase the screen by filling it with a black RGB color
    pygame.display.flip()

