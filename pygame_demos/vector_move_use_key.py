import pygame, sys
from gameobjects.vector2 import Vector2

size = w, h = 640, 320
pygame.init()
screen = pygame.display.set_mode(size, 0, 32)
background = pygame.image.load('images/sushiplate.jpg').convert()
sprite = pygame.image.load('images/intro_ball.gif').convert_alpha()
clock = pygame.time.Clock()

rect_color = 0, 255, 0
rect_size = 40, 40

sprite_position = Vector2(100.0, 100.0)
sprite_speed = 250 # pixel / second

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    key_direction = Vector2(0, 0)
    if pressed_keys[pygame.K_LEFT]:
        key_direction.x = -1
    elif pressed_keys[pygame.K_RIGHT]:
        key_direction.x = +1
    elif pressed_keys[pygame.K_UP]:
        key_direction.y = -1
    elif pressed_keys[pygame.K_DOWN]:
        key_direction.y = +1

    key_direction.normalize()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (sprite_position.x, sprite_position.y))
    # pygame.draw.rect(screen, rect_color, pygame.Rect((x, y), rect_size))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    sprite_position += key_direction * time_passed_seconds * sprite_speed

    pygame.display.flip()