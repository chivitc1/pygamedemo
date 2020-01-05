import pygame, sys, math

from gameobjects.matrix44 import Matrix44
from gameobjects.vector3d import Vector3

SCREEN_SIZE = SCREEN_W, SCREEN_H = 640, 480
bg_color = (0, 0, 0)
CUBE_SIZE = 300

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

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


def start():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    ball = pygame.image.load("images/ball.png").convert_alpha()

    fov = 75.0 # degrees
    viewing_distance = calculate_view_distance(fov, SCREEN_W)

    points = create_cube_points()
    points.sort(key=point_z, reverse=True)

    center_x, center_y = SCREEN_W/2, SCREEN_H/2
    ball_w, ball_h = ball.get_size()
    ball_center_x, ball_center_y = ball_w/2, ball_h/2

    cam_position = Vector3(0.0, 0.0, 600.0)

    rotation = Vector3()
    rotation_speed = Vector3(math.radians(20), math.radians(20), math.radians(20))

    # Labels for the axes
    font = pygame.font.SysFont(pygame.font.get_default_font(), 16)
    x_surface = font.render("X", True, white)
    y_surface = font.render("Y", True, white)
    z_surface = font.render("Z", True, white)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        screen.fill(bg_color)
        time_passed = clock.tick(30)
        time_passed_seconds = time_passed / 1000.0

        rotation_direction = Vector3()

        # Adjust the rotation direction depending on key presses
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_q]:
            rotation_direction.x = +1.0
        elif pressed_keys[pygame.K_a]:
            rotation_direction.x = -1.0

        if pressed_keys[pygame.K_w]:
            rotation_direction.y = +1.0
        elif pressed_keys[pygame.K_s]:
            rotation_direction.y = -1.0

        if pressed_keys[pygame.K_e]:
            rotation_direction.z = +1.0
        elif pressed_keys[pygame.K_d]:
            rotation_direction.z = -1.0

        rotation += rotation_direction * rotation_speed * time_passed_seconds

        rotation_matrix = Matrix44.x_rotation(rotation.x)
        rotation_matrix *= Matrix44.y_rotation(rotation.y)
        rotation_matrix *= Matrix44.z_rotation(rotation.z)

        transformed_points = []
        # Transform all the points and adjust for camera position
        for point in points:
            p = rotation_matrix.transform_vec3(point) - cam_position
            transformed_points.append(p)
        transformed_points.sort(key=point_z)

        # Perspective project and blit all the points
        for x, y, z in transformed_points:
            if z < 0:
                x = center_x + x * (-viewing_distance / z)
                y = center_y + (-y) * (-viewing_distance / z)
                screen.blit(ball, (x - ball_center_x, y - ball_center_y))

        def draw_axis(label, axis, color):
            axis = rotation_matrix.transform_vec3(axis * 150.0)
            x, y, z = axis - cam_position
            x = SCREEN_W/2.0 + x * (-viewing_distance / z)
            y = SCREEN_H/2.0 + (-y) * (-viewing_distance / z)
            pygame.draw.line(screen, color, (center_x, center_y), (x, y), 2)

            w, h = label.get_size()
            screen.blit(label, (x - w/2, y - h/2))

        # Draw the x, y and z axes
        x_axis = Vector3(1, 0, 0)
        y_axis = Vector3(0, 1, 0)
        z_axis = Vector3(0, 0, 1)
        draw_axis(x_surface, x_axis, red)
        draw_axis(y_surface, y_axis, green)
        draw_axis(z_surface, z_axis, blue)

        # Display rotation information on screen
        degrees_txt = tuple(math.degrees(r) for r in rotation)
        rotation_txt = f"Rotation: Q/A {round(degrees_txt[0], 3)}, W/S {round(degrees_txt[1], 3)}, E/D {round(degrees_txt[2], 3)}"
        txt_surface = font.render(rotation_txt, True, white)
        screen.blit(txt_surface, (5, 5))

        matrix_txt = str(rotation_matrix)
        txt_y = 25
        for line in matrix_txt.split('\n'):
            txt_surface = font.render(line, True, white)
            screen.blit(txt_surface, (5, txt_y))
            txt_y += 20
        
        pygame.display.flip()


def create_cube_points():
    points = []
    # Create a list of points along the edge of a cube
    for x in range(0, CUBE_SIZE + 1, 10):
        edge_x = x == 0 or x == CUBE_SIZE
        for y in range(0, CUBE_SIZE + 1, 10):
            edge_y = y == 0 or y == CUBE_SIZE
            for z in range(0, CUBE_SIZE + 1, 10):
                edge_z = z == 0 or z == CUBE_SIZE
                if sum((edge_x, edge_y, edge_z)) >= 2:
                    p_x = float(x) - CUBE_SIZE / 2
                    p_y = float(y) - CUBE_SIZE / 2
                    p_z = float(z) - CUBE_SIZE / 2

                    points.append(Vector3(p_x, p_y, p_z))
    return points


def point_z(point):
    # Sort points in z order
    return point.z

if __name__ == '__main__':
    start()