import pygame, sys

size = w, h = 640, 480
pygame.init()
screen = pygame.display.set_mode(size, 0, 32)

background_color = 0, 0, 0
font_color = 255, 0, 0
title_color = 0, 255, 0

title_pos = (100, 20)
font = pygame.font.SysFont("arial", 32)
font_height = font.get_linesize()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(background_color)
    title_surface = font.render("Press keys and see!", True, title_color)
    screen.blit(title_surface, title_pos)

    pressed_key_text = []
    pressed_keys = pygame.key.get_pressed()
    y = font_height + 100

    for key_constant, pressed in enumerate(pressed_keys):
        if pressed:
            key_name = pygame.key.name(key_constant)
            text_surface = font.render(key_name + " pressed", True, font_color)
            screen.blit(text_surface, (100, y))
            y += font_height

    pygame.display.flip()
