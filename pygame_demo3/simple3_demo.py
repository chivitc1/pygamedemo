import pygame, sys, math
from gameobjects.vector3d import Vector3

SCREEN_SIZE = SCREEN_W, SCREEN_H = 640, 480
CUBE_SIZE = 300
text_color = (255, 255, 255)
text_pos = (5, 5)
fov_text_pos = (5, 35)
distance_text_pos = (5, 65)
bg_color = (0, 0, 0)


def calculate_view_distance(fov, screen_width):
    viewing_distance = (screen_width/2.0) / math.tan(math.radians(fov)/2.0)
    return viewing_distance


def quit_game():
    pygame.quit()
    sys.exit()


def get_direction(pressed_keys):
    direction = Vector3()
    if pressed_keys[pygame.K_LEFT]:
        direction.x = -1.0
    elif pressed_keys[pygame.K_RIGHT]:
        direction.x = +1.0

    if pressed_keys[pygame.K_UP]:
        direction.y = +1.0
    elif pressed_keys[pygame.K_DOWN]:
        direction.y = -1.0

    if pressed_keys[pygame.K_q]:
        direction.z = +1.0
    elif pressed_keys[pygame.K_a]:
        direction.z = -1.0

    return direction


def start():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    ball = pygame.image.load("images/ball.png").convert_alpha()

    points = create_cube_points()
    fov = 90.0 #degrees
    viewing_distance = calculate_view_distance(fov, SCREEN_W)

    points.sort(key=point_z, reverse=True)

    center_x, center_y = SCREEN_W/2, SCREEN_H/2
    ball_w, ball_h = ball.get_size()
    ball_center_x, ball_center_y = ball_w/2, ball_h/2

    camera_position = Vector3(0.0, 0.0, -700.0)
    camera_speed = Vector3(300.0, 300.0, 300.0)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        screen.fill(bg_color)
        pressed_keys = pygame.key.get_pressed()
        time_passed = clock.tick(30)
        time_passed_seconds = time_passed / 1000.0
        direction = get_direction(pressed_keys)

        if pressed_keys[pygame.K_w]:
            fov = min(179.0, fov + 1.0)
            viewing_distance = calculate_view_distance(fov, SCREEN_W)
        elif pressed_keys[pygame.K_s]:
            fov = max(1.0, fov - 1.0)
            viewing_distance = calculate_view_distance(fov, SCREEN_W)

        camera_position += direction * camera_speed * time_passed_seconds

        # Draw the 3D points
        for point in points:
            x, y, z = point - camera_position
            if z > 0:
                x = x * viewing_distance / z
                y = -y * viewing_distance / z
                x += center_x
                y += center_y
                screen.blit(ball, (x - ball_center_x, y - ball_center_y))

        # Draw the field of view diagram
        diagram_width = SCREEN_W / 4
        diagram_color = (50, 255, 50)
        diagram_points = []
        diagram_points.append((diagram_width / 2, 100 + viewing_distance / 4) )
        diagram_points.append( (0, 100) )
        diagram_points.append( (diagram_width, 100) )
        diagram_points.append( (diagram_width / 2, 100 + viewing_distance / 4) )
        diagram_points.append( (diagram_width / 2, 100))
        pygame.draw.lines(screen, diagram_color, False, diagram_points, 2)

        # Draw the text
        default_font = pygame.font.get_default_font()
        font = pygame.font.SysFont(default_font, 24)
        cam_text = font.render(f"Camera = {str(camera_position)}", True, text_color)
        screen.blit(cam_text, text_pos)

        fov_text = font.render(f"Field of view = {int(fov)}", True, text_color)
        screen.blit(fov_text, fov_text_pos)

        distance_text = font.render(f"Viewing distance = {round(viewing_distance, 3)}", True, text_color)
        screen.blit(distance_text, distance_text_pos)

        pygame.display.flip()


def create_cube_points():
    points = []
    # Create a list of points along the edge of a cube
    for x in range(0, CUBE_SIZE + 1, 20):
        edge_x = x == 0 or x == CUBE_SIZE
        for y in range(0, CUBE_SIZE + 1, 20):
            edge_y = y == 0 or y == CUBE_SIZE
            for z in range(0, CUBE_SIZE + 1, 20):
                edge_z = z == 0 or z == CUBE_SIZE
                if sum((edge_x, edge_y, edge_z)) >= 2:
                    point_x = float(x) - CUBE_SIZE / 2
                    point_y = float(y) - CUBE_SIZE / 2
                    point_z = float(z) - CUBE_SIZE / 2

                    points.append(Vector3(point_x, point_y, point_z))
    return points


def point_z(point):
    # Sort points in z order
    return point.z

if __name__ == '__main__':
    start()