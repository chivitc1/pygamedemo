import pygame, sys

pygame.init()

size = w, h = 640, 480
screen = pygame.display.set_mode(size, 0, 32)

points = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            points.append(event.pos)
    screen.fill((0,0,0))

    if len(points) > 3:
        pygame.draw.polygon(screen, (0, 255, 0), points)

    for point in points:
        pygame.draw.circle(screen, (0, 0, 255), point, 5)

    pygame.display.flip()