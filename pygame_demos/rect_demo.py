import pygame, sys, random

pygame.init()
scr_size = w, h = 640, 480

screen = pygame.display.set_mode(scr_size, 0, 32)

def draw_rects(screen_surface):
    screen_surface.lock()
    screen_surface.fill((0, 0, 0))
    for count in range(10):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        random_pos = (random.randint(0, w), random.randint(0, h))
        random_size = (w - random.randint(random_pos[0], w), h - random.randint(random_pos[1], h))
        pygame.draw.rect(screen_surface, random_color, pygame.Rect(random_pos, random_size))
    screen_surface.unlock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_rects(screen)
    pygame.time.wait(1000)
    pygame.display.flip()