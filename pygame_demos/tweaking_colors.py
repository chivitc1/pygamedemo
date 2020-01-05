import pygame, sys

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)


def create_scales(height):
    red_scale_surface = pygame.surface.Surface((640, height))
    green_scale_surface = pygame.surface.Surface((640, height))
    blue_scale_surface = pygame.surface.Surface((640, height))
    for x in range(640):
        c = int((x/639.0)*255.0)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        line_rect = pygame.Rect(x, 0, 1, height)
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)
    return red_scale_surface, green_scale_surface, blue_scale_surface

height = 80
red_scale, green_scale, blue_scale = create_scales(height)
color = [127, 127, 127]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))

    screen.blit(red_scale, (0, 0 * height))
    screen.blit(green_scale, (0, 1 * height))
    screen.blit(blue_scale, (0, 2 * height))

    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        for component in range(3):
            if component * height < y < (component + 1) * height:
                color[component] = int((x/639.0)*255.0)
            pygame.display.set_caption(("Pygame color test - " + str(tuple(color))))

    for component in range(3):
        pos = (int((color[component]/255.0)*639), component*height + height//2)
        pygame.draw.circle(screen, (255, 255, 255), pos, 20)

    pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))

    pygame.display.flip()
