import random
import sys

import pygame

from pygame_demos2.ant import Ant
from pygame_demos2.leaf import Leaf
from pygame_demos2.spider import Spider
from pygame_demos2.vector2 import Vector2
from pygame_demos2.world import World

ANT_COUNT = 20


def quit_game():
    pygame.quit()
    sys.exit()


def start():
    pygame.init()
    screen = pygame.display.set_mode(World.SCR_SIZE, 0, 32)
    world = World()

    w, h = World.SCR_SIZE
    clock = pygame.time.Clock()
    ant_image = pygame.image.load("images/ant.png").convert_alpha()
    leaf_image = pygame.image.load("images/leaf.png").convert_alpha()
    spider_image = pygame.image.load("images/spider.png").convert_alpha()

    for ant_no in range(ANT_COUNT):
        ant = Ant(world, ant_image)
        ant.location = Vector2(random.randint(0, w), random.randint(0, h))
        ant.brain.set_state("exploring")
        world.add_entity(ant)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        time_passed = clock.tick(30)
        if random.randint(1, 40) == 1:
            leaf = Leaf(world, leaf_image)
            leaf.location = Vector2(random.randint(0, w), random.randint(0, h))
            world.add_entity(leaf)

        if random.randint(1, 100) == 1:
            spider = Spider(world, spider_image)
            spider.location = Vector2(random.randint(0, w), random.randint(0, h))
            spider.destination = Vector2(w + 50, random.randint(0, h))
            world.add_entity((spider))

        world.process(time_passed)
        world.render(screen)

        pygame.display.flip()


if __name__ == '__main__':
    start()
