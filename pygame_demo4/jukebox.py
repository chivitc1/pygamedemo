import os
import sys

import pygame

DEFAULT_MUSIC_PATH = "/home/chinv/Music/rap_viet/"

SCREEN_SIZE = SCREEN_W, SCREEN_H = 800, 600

TRACK_END = pygame.USEREVENT + 1


def get_music(path):
    raw_filenames = os.listdir(path)
    music_files = []
    for filename in raw_filenames:
        if filename.endswith('.mp3'):
            music_files.append(os.path.join(DEFAULT_MUSIC_PATH, filename))

    return sorted(music_files)


class Button:
    def __init__(self, image, position):
        self.position = position
        self.image = image

    def render(self, surface):
        x, y = self.position
        w, h = self.image.get_size()
        x -= w/2
        y -= h/2
        surface.blit(self.image, (x, y))

    def is_over(self, point):
        # Return True if a point is over the button
        point_x, point_y = point
        x, y = self.position
        w, h = self.image.get_size()
        x -= w / 2
        y -= h / 2

        if x <= point_x < x + w and y <= point_y < y + h:
            return True
        return False


def start():
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()
    # pygame.mixer.music.set_volume(0.9)
    screen = pygame.display.set_mode(SCREEN_SIZE, 0)
    default_font = pygame.font.get_default_font()
    font = pygame.font.SysFont(default_font, 16, False)
    # Create our buttons
    x = 100
    y = 240
    button_width = 150
    spacing = 1

    # Store the buttons in a dictionary, so we can assign them names
    buttons = {}
    scale = (50, 50)
    img_prev = pygame.transform.scale(pygame.image.load("image3/media-prev.png").convert_alpha(), scale)
    img_pause = pygame.transform.scale(pygame.image.load("image3/media-pause.png").convert_alpha(), scale)
    img_stop = pygame.transform.scale(pygame.image.load("image3/media-stop.png").convert_alpha(), scale)
    img_play = pygame.transform.scale(pygame.image.load("image3/media-play.png").convert_alpha(), scale)
    img_next = pygame.transform.scale(pygame.image.load("image3/media-next.png").convert_alpha(), scale)

    buttons["prev"] = Button(img_prev, (x, y))

    padding = img_prev.get_size()[0] + spacing
    buttons["pause"] = Button(img_pause, (x + padding, y))

    padding += img_pause.get_size()[0] + spacing
    buttons["stop"] = Button(img_stop, (x + padding, y))

    padding += img_stop.get_size()[0] + spacing
    buttons["play"] = Button(img_play, (x + padding, y))

    padding += img_play.get_size()[0] + spacing
    buttons["next"] = Button(img_next, (x + padding, y))

    # os.chdir(MUSIC_PATH)
    music_filenames = get_music(DEFAULT_MUSIC_PATH)
    # print(music_filenames)
    if len(music_filenames) == 0:
        return

    white = (255, 255, 255)
    label_surfaces = []
    # Render the track names
    for filename in music_filenames:
        txt = os.path.split(filename)[-1]
        txt = txt.split('.')[0]
        surface = font.render(txt, True, (100, 0, 100))
        label_surfaces.append(surface)
    current_track = 0
    max_tracks = len(music_filenames)
    print("-"*20, "Music List", "-"*20)
    for i, item in enumerate(music_filenames):
        print(f"{i+1}. {item}")
    # load_track(music_filenames[current_track])
    clock = pygame.time.Clock()

    playing = False
    paused = False

    # This event is sent when a music track ends
    pygame.mixer.music.set_endevent(TRACK_END)

    while True:
        button_pressed = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Find the pressed button
                for button_name, button in buttons.items():
                    if button.is_over(event.pos):
                        button_pressed = button_name
                        print(f"Click button {button_name}")
                        break

            if event.type == TRACK_END:
                button_pressed = "next"

        if button_pressed is not None:
            if button_pressed == "next":
                current_track = (current_track + 1) % max_tracks
                load_track(music_filenames[current_track])
                if playing:
                    play_current_track()
            elif button_pressed == "prev":
                # if pygame.mixer.music.get_pos() > 3000:
                #     # If the track has been playing for more that 3 seconds,
                #     # rewind i, otherwise select the previous track
                #     stop_current_track()
                #     pygame.time.wait(1000)
                #     play_current_track()
                # else:
                if current_track > 0:
                    current_track = (current_track -1) % max_tracks
                else:
                    current_track = max_tracks

                if playing:
                    load_track(music_filenames[current_track])
                    play_current_track()

            elif button_pressed == "pause":
                if paused:
                    unpause_current_track()
                    paused = False
                else:
                    pause_current_track()
                    paused = True

            elif button_pressed == "stop":
                stop_current_track()
                playing = False

            elif button_pressed == "play":
                if paused:
                    unpause_current_track()
                    paused = False
                else:
                    stop_current_track()
                    load_track(music_filenames[current_track])
                    play_current_track()
                    playing = True

        screen.fill(white)
        # Render the name of the currently track
        label = label_surfaces[current_track]
        w, h = label.get_size()
        screen.blit(label, ((SCREEN_W - w)/2, 450))

        # Render all the buttons
        for button in list(buttons.values()):
            button.render(screen)

        # No animation, 5 frames per second is fine!
        clock.tick(3)
        pygame.display.update()


def load_track(filename):
    print(f"Loading track: {filename}")
    # if pygame.mixer.music.get_busy():
    #     print("Music is playing. Stop before load track")
    #     stop_current_track()
    #     pygame.time.wait(1000)
    pygame.mixer.music.load(filename)
    pygame.time.wait(1000)


def pause_current_track():
    print("Pause")
    pygame.mixer.music.pause()


def unpause_current_track():
    print("Unpause")
    pygame.mixer.music.unpause()


def play_current_track():
    print("Play")
    pygame.mixer.music.play()


def stop_current_track():
    print("Stop")
    pygame.mixer.music.stop()


if __name__ == '__main__':
    start()

