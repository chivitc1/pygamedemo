import pygame, sys, math
from random import randint

SCREEN_SIZE = SCREEN_W, SCREEN_H = 640, 480
WHITE = (255, 255, 255)

class Star:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed


def quit_game():
    pygame.quit()
    sys.exit()


def start():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    stars = []

    for n in range(200):
        x = float(randint(0, SCREEN_W))
        y = float(randint(0, SCREEN_H))
        speed = float(randint(10, 300))
        stars.append(Star(x, y, speed))

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game()

        y = float(randint(0, SCREEN_H))
        speed = float(randint(10, 300))
        star = Star(SCREEN_W * 1.0, y, speed)
        stars.append(star)
        time_passed = clock.tick()
        time_passed_seconds = time_passed/1000.0
        screen.fill((0, 0, 0))

        for st in stars:
            new_x = st.x - time_passed_seconds * st.speed
            pygame.draw.aaline(screen, WHITE, (new_x, st.y), (st.x + 1.0, st.y))
            st.x = new_x

        def on_screen(star):
            return star.x > 0

        stars = list(filter(on_screen, stars))

        pygame.display.flip()


if __name__ == '__main__':
    start()
