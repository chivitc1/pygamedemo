import math

import pygame, sys
from gameobjects.vector2 import Vector2

size = w, h = 640, 320
pygame.init()
screen = pygame.display.set_mode(size, 0, 32)
background = pygame.image.load('images/sushiplate.jpg').convert()
sprite = pygame.image.load('images/fugu.png').convert_alpha()
clock = pygame.time.Clock()

rect_color = 0, 255, 0
rect_size = 40, 40

sprite_position = Vector2(100.0, 100.0)
sprite_speed = 250 # pixel / second
sprite_rotation = 0
sprite_rotation_speed = 360 # degrees per second

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pressed_keys = pygame.key.get_pressed()
    pressed_mouse = pygame.mouse.get_pressed()

    sprite_direction = Vector2(0, 0)

    movement_direction = 0
    rotation_direction = pygame.mouse.get_rel()[0] / 3.0

    if pressed_keys[pygame.K_LEFT]:
        rotation_direction = +1
    elif pressed_keys[pygame.K_RIGHT]:
        rotation_direction = -1
    elif pressed_keys[pygame.K_UP] or pressed_mouse[0]:
        movement_direction = +1
    elif pressed_keys[pygame.K_DOWN] or pressed_mouse[2]:
        movement_direction = -1

    screen.blit(background, (0, 0))

    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    sprite_w, sprite_h = rotated_sprite.get_size()
    sprite_draw_pos = Vector2(sprite_position.x - sprite_w/2, sprite_position.y - sprite_h/2)
    screen.blit(rotated_sprite, (sprite_draw_pos.x, sprite_draw_pos.y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds

    heading_x = math.sin(sprite_rotation * math.pi/180.0)
    heading_y = math.cos(sprite_rotation * math.pi/180.0)
    heading = Vector2(heading_x, heading_y)
    heading *= movement_direction

    sprite_position += heading * sprite_speed * time_passed_seconds

    pygame.display.flip()