import pygame, sys, math
from gameobjects.vector2 import Vector2

pygame.init()

map_file = 'images/map.png'
SCR_SIZE = SCR_W, SCR_H = 640, 480

screen = pygame.display.set_mode(SCR_SIZE, 0, 32)

map_img = pygame.image.load(map_file).convert()

map_pos = Vector2(0, 0)

scroll_speed = 1000.0

clock = pygame.time.Clock()

joystick = None

if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

print(joystick)
if joystick is None:
    print("Sorry, you need a joystick for this demo")
    pygame.quit()
    exit()

print(f"num of joystick axis: {joystick.get_numaxes()}")

def quit_game():
    pygame.quit()
    sys.exit()

background_color = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit_game()

    scroll_direction = Vector2(0, 0)
    if joystick.get_numhats() > 0:
        scroll_direction = Vector2(*joystick.get_hat(0))
        scroll_direction.normalize()

    analog_scroll = Vector2(0, 0)
    if joystick.get_numaxes() >= 2:
        axis_x = joystick.get_axis(0)
        axis_y = joystick.get_axis(1)
        # print(f"axis_x: {axis_x}, axis_y: {axis_y}")
        # print(f"joystick name: {joystick.get_name()}, numballs: {joystick.get_numballs()}")
        analog_scroll = Vector2(axis_x, -axis_y)

    screen.fill(background_color)
    screen.blit(map_img, (-map_pos.x, map_pos.y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    map_pos += scroll_direction * scroll_speed * time_passed_seconds
    map_pos += analog_scroll * scroll_speed * time_passed_seconds

    pygame.display.flip()

