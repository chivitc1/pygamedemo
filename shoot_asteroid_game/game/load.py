import pyglet
import random
from . import resources, util, asteroid


def player_lives(num_icons, batch=None):
    """Generate sprites for player life icon"""
    player_live_list = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=resources.player_image, x=785 - i*30, y=585, batch=batch)
        new_sprite.scale = 0.5
        player_live_list.append(new_sprite)
    return player_live_list


def asteroids(num_asteroids, player_position, batch=None):
    asteroid_list = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while util.distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 800)
        new_asteroid = asteroid.Asteroid(x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x, new_asteroid.velocity_y = random.random()* 40, random.random() * 40
        asteroid_list.append(new_asteroid)
    return asteroid_list


