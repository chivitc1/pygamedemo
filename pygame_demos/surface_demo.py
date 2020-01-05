import sys

import pygame

pygame.init()
screen_size = screen_w, screen_h = 640, 480
screen = pygame.display.set_mode(screen_size, 0, 32)

size = (256, 256)
blank_surface = pygame.Surface(size)
blank_surface_alpha = pygame.Surface(size, depth=32)
background = pygame.image.load("images/sushiplate.jpg").convert()
mouse_cursor = pygame.image.load("images/fugu.png").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0, 0))
    screen.blit(blank_surface, (20, 20))
    screen.blit(blank_surface_alpha, (screen_w - 256, screen_h - 256))

    mouse_pos = pygame.mouse.get_pos()
    screen.blit(mouse_cursor, mouse_pos)

    pygame.display.flip()