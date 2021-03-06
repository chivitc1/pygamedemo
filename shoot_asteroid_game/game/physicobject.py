import pyglet
from . import util


class PhysicalObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0

        # And a flag to remove this object from the game_object list
        self.dead = False

        # Flags to toggle collision with bullets
        self.is_bullet = False
        self.reacts_to_bullets = True

        # List of new objects to go in the game_objects list
        self.new_objects = []

        # Tell the game handler about any event handlers
        # Only applies to things with keyboard/mouse input
        self.event_handlers = []

    def update(self, dt):
        """This method should be call every frame"""

        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # wrap around screen if necessary
        self.check_bounds()

    def check_bounds(self):
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 800 + self.image.width / 2
        max_y = 600 + self.image.height / 2

        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x

        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y

    def collides_with(self, other):
        """Determine if this object collides with another"""

        # Ignore bullet collisions if we're supposed to
        if self.is_bullet and not other.reacts_to_bullets:
            return False
        if not self.reacts_to_bullets and other.is_bullet:
            return False

        # Calculate distance between object centers that would be a collision,
        # assuming square resources
        # collision_distance = self.image.width / 2 + other.image.width / 2
        collision_distance = self.image.width * 0.5 * self.scale + other.image.width * 0.5 * other.scale

        # Get distance using position tuples
        actual_distance = util.distance(self.position, other.position)

        return actual_distance <= collision_distance

    def handle_collision_with(self, other):
        if other.__class__ is not self.__class__:
            self.dead = True
