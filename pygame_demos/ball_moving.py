import pygame, sys

pygame.init()

ball_file = 'images/intro_ball.gif'
size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.RESIZABLE, 32) #create a graphical window
ball = pygame.image.load(ball_file) #load our ball image
ball_rect = ball.get_rect()

pygame.display.set_caption("Hello")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
    ball_rect = ball_rect.move(speed) # move the ball
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black) # erase the screen by filling it with a black RGB color
    screen.blit(ball, ball_rect) # copying pixel colors from one image to another
    pygame.display.flip() # makes everything we have drawn on the screen Surface become visible, Pygame manages the display with a double buffer
    pygame.time.wait(10)

