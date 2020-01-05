import pygame, sys, time  # Imports Modules
from pygame.locals import *
from gamepad import GamePadEvent

pygame.init()  # Initializes Pygame
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()  # Initializes Joystick

# get count of joysticks=1, axes=27, buttons=19 for DualShock 3

joystick_count = pygame.joystick.get_count()
print("joystick_count")
print(joystick_count)
print("--------------")

numaxes = joystick.get_numaxes()
print("numaxes")
print(numaxes)
print("--------------")

numbuttons = joystick.get_numbuttons()
print("numbuttons")
print(numbuttons)
print("--------------")

loopQuit = False
while True:
    pad_event = None

    for event in pygame.event.get():
        if event.type == QUIT:
            loopQuit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                loopQuit = True
        if loopQuit:
            break

        if event.type == pygame.JOYBUTTONUP or event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYHATMOTION \
                or event.type == pygame.JOYBALLMOTION or event.type == pygame.JOYAXISMOTION:
            # print(event)
            pad_event = GamePadEvent(event)
            if pad_event.type is not None:
                print(pad_event)

    time.sleep(1)
pygame.quit()
sys.exit()
