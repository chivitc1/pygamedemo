import pygame

MUSIC_PATH = "/home/chinv/Music/rap_viet/ViDoLaEm-OsadShinHyunWoo.mp3"
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.display.set_mode((200,100))
pygame.mixer.music.load(MUSIC_PATH)

pygame.mixer.music.play()
pygame.time.wait(5000)
pygame.mixer.music.load("/home/chinv/Music/rap_viet/HaiTrieuNam-DenBien.mp3")

pygame.mixer.music.play()
pygame.time.wait(2000)

clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    # pygame.event.poll()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    clock.tick(10)