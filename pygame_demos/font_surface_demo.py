import pygame, sys, random

pygame.init()
my_font = pygame.font.SysFont("arial", 16)
text_surface = my_font.render("Pygame is cool", True, (255, 255,255), (0,0,0))

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.RESIZABLE, 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
    screen.fill(black) # erase the screen by filling it with a black RGB color
    screen.blit(text_surface, (random.randint(1, width-100),random.randint(1, height - 100))) # copying pixel colors from one image to another
    pygame.display.flip() # makes everything we have drawn on the screen Surface become visible, Pygame manages the display with a double buffer
    pygame.time.wait(1000)