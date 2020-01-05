import pygame

from pygame_demos2.vector2 import Vector2


class World:
    SCR_SIZE = SRC_W, SRC_H = 640, 480
    BACKGROUND_COLOR = (255, 255, 255)
    NEST_POSITION = (SRC_W//2, SRC_H//2)
    NEST_SIZE = 80.0

    def __init__(self):
        self.entities = {}
        self.last_entity_id = 0

        # Draw the nest (a circle) on the background
        self.background = pygame.surface.Surface(self.SCR_SIZE).convert()
        self.background.fill(self.BACKGROUND_COLOR)
        pygame.draw.circle(self.background, (200, 255, 200), self.NEST_POSITION, int(self.NEST_SIZE))

    def add_entity(self, entity):
        self.entities[self.last_entity_id] = entity
        entity.id = self.last_entity_id
        self.last_entity_id += 1

    def remove_entity(self, entity):
        del self.entities[entity.id]

    def get(self, entity_id):
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None

    def process(self, time_passed):
        time_passed_seconds = time_passed / 1000.0
        for entity in list(self.entities.values()):
            entity.process(time_passed_seconds)

    def render(self, surface):
        # Draw the background and all the entities
        surface.blit(self.background, (0, 0))
        for entity in list(self.entities.values()):
            entity.render(surface)

    def get_close_entity(self, name, location, e_range=1000):
        # Find an entity within range of a location
        location = Vector2(*location)
        for entity in self.entities.values():
            if entity.name == name:
                distance = location.get_distance_to(entity.location)
                if distance < e_range:
                    return entity
        return None
