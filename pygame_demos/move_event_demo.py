import pygame, sys

pygame.init()
ball_file = "images/intro_ball.gif"
bg_file = "images/bowl.jpeg"
size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.RESIZABLE, 32) #create a graphical window
background = pygame.image.load(bg_file)
ball = pygame.image.load(ball_file)

pygame.display.set_caption("Hello")
velocity = 10
x, y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        if event.type == pygame.KEYDOWN:
            move_x, move_y = 0, 0
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_LEFT:
                move_x = -velocity
            if event.key == pygame.K_RIGHT:
                move_x = +velocity
            if event.key == pygame.K_UP:
                move_y = -velocity
            if event.key == pygame.K_DOWN:
                move_y = +velocity
            x += move_x
            y += move_y
        # print(event)



    screen.fill(black) # erase the screen by filling it with a black RGB color
    screen.blit(background, (0,0))
    screen.blit(ball, (x, y))
    pygame.display.flip()
    # pygame.time.wait(10)

