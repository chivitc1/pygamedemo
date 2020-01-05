import pygame


class GamePadEvent:
    TYPE_HAT = "HAT"
    TYPE_BALL = "BALL"
    TYPE_ACTION = "ACTIONS"
    TYPE_OPTION = "OPTIONS"
    TYPE_MASTER = "MASTERS"

    BTN_ONE_DOWN = "BTN_ONE_DOWN"
    BTN_TWO_DOWN = "BTN_TWO_DOWN"
    BTN_THREE_DOWN = "BTN_THREE_DOWN"
    BTN_FOUR_DOWN = "BTN_FOUR_DOWN"

    BTN_ONE_UP = "BTN_ONE_UP"
    BTN_TWO_UP = "BTN_TWO_UP"
    BTN_THREE_UP = "BTN_THREE_UP"
    BTN_FOUR_UP = "BTN_FOUR_UP"

    HAT_UP = "HAT_UP"
    HAT_DOWN = "HAT_DOWN"
    HAT_LEFT = "HAT_LEFT"
    HAT_RIGHT = "HAT_RIGHT"
    HAT_RELEASED = "HAT_RELEASED"

    START_DOWN = "START_DOWN"
    START_UP = "START_UP"

    SELECT_DOWN = "SELECT_DOWN"
    SELECT_UP = "SELECT_UP"

    OPTION_R1_DOWN = "OPTION_R1_DOWN"
    OPTION_R1_UP = "OPTION_R1_UP"
    OPTION_R2_DOWN = "OPTION_R2_DOWN"
    OPTION_R2_UP = "OPTION_R2_UP"
    OPTION_L1_DOWN = "OPTION_L1_DOWN"
    OPTION_L1_UP = "OPTION_L1_UP"
    OPTION_L2_DOWN = "OPTION_L2_DOWN"
    OPTION_L2_UP = "OPTION_L2_UP"

    def __init__(self, event):
        self.type = None
        self.value = None

        if event.type == pygame.JOYHATMOTION:
            self.type = self.TYPE_HAT

            if event.value == (0, -1):
                self.value = self.HAT_DOWN
            if event.value == (0, 1):
                self.value = self.HAT_UP

            if event.value == (-1, 0):
                self.value = self.HAT_LEFT
            if event.value == (1, 0):
                self.value = self.HAT_RIGHT

            if event.value == (0, 0):
                self.value = self.HAT_RELEASED

        if event.type == pygame.JOYBUTTONDOWN:
            self.type = self.TYPE_ACTION
            if event.button == 0:
                self.value = self.BTN_ONE_DOWN
            if event.button == 1:
                self.value = self.BTN_TWO_DOWN
            if event.button == 2:
                self.value = self.BTN_THREE_DOWN
            if event.button == 3:
                self.value = self.BTN_FOUR_DOWN

            if event.button == 4:
                self.value = self.OPTION_L1_DOWN
                self.type = self.TYPE_OPTION
            if event.button == 5:
                self.value = self.OPTION_R1_DOWN
                self.type = self.TYPE_OPTION
            if event.button == 6:
                self.value = self.OPTION_L2_DOWN
                self.type = self.TYPE_OPTION
            if event.button == 7:
                self.value = self.OPTION_R2_DOWN
                self.type = self.TYPE_OPTION

            if event.button == 8:
                self.value = self.SELECT_DOWN
                self.type = self.TYPE_MASTER
            if event.button == 9:
                self.value = self.START_DOWN
                self.type = self.TYPE_MASTER

        if event.type == pygame.JOYBUTTONUP:
            self.type = self.TYPE_ACTION
            if event.button == 0:
                self.value = self.BTN_ONE_UP
            if event.button == 1:
                self.value = self.BTN_TWO_UP
            if event.button == 2:
                self.value = self.BTN_THREE_UP
            if event.button == 3:
                self.value = self.BTN_FOUR_UP

            if event.button == 4:
                self.value = self.OPTION_L1_UP
                self.type = self.TYPE_OPTION
            if event.button == 5:
                self.value = self.OPTION_R1_UP
                self.type = self.TYPE_OPTION
            if event.button == 6:
                self.value = self.OPTION_L2_UP
                self.type = self.TYPE_OPTION
            if event.button == 7:
                self.value = self.OPTION_R2_UP
                self.type = self.TYPE_OPTION

            if event.button == 8:
                self.value = self.SELECT_UP
                self.type = self.TYPE_MASTER
            if event.button == 9:
                self.value = self.START_UP
                self.type = self.TYPE_MASTER

    def __str__(self):
        return f"(type: {self.type}, value: {self.value})"