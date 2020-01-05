import random

from pygame_demos2.state import State
from pygame_demos2.vector2 import Vector2
from pygame_demos2.world import World


class AntStateExploring(State):
    ANT_VIEW_DISTANCE = 100.0

    def __init__(self, ant):
        State.__init__(self, "exploring")
        self.ant = ant

    def random_destination(self):
        w, h = World.SCR_SIZE
        self.ant.destination = Vector2(random.randint(0, w), random.randint(0, h))

    def do_actions(self):
        if random.randint(1, 20) == 1:
            self.random_destination()

    def check_conditions(self):
        leaf = self.ant.world.get_close_entity("leaf", self.ant.location)
        if leaf is not None:
            self.ant.leaf_id = leaf.id
            return "seeking"

        spider = self.ant.world.get_close_entity("spider", World.NEST_POSITION, World.NEST_SIZE)
        if spider is not None:
            if self.ant.location.get_distance_to(spider.location) < self.ANT_VIEW_DISTANCE:
                self.ant.spider_id = spider.id
                return "hunting"
        return None

    def entry_actions(self):
        self.ant.speed = 120.0 + random.randint(-30, 30)
        self.random_destination()


class AntStateSeeking(State):
    def __init__(self, ant):
        State.__init__(self, "seeking")
        self.ant = ant
        self.leaf_id = None

    def check_conditions(self):
        leaf = self.ant.world.get(self.ant.leaf_id)
        if leaf is None:
            return "exploring"
        if self.ant.location.get_distance_to(leaf.location) < 5:
            self.ant.carry(leaf.image)
            self.ant.world.remove_entity(leaf)
            return "delivering"

        return None

    def entry_actions(self):
        leaf = self.ant.world.get(self.ant.leaf_id)
        if leaf is not None:
            self.ant.destination = leaf.location
            self.ant.speed = 160 + random.randint(-20, 20)


class AntStateDelivering(State):
    def __init__(self, ant):
        State.__init__(self, "delivering")
        self.ant = ant

    def check_conditions(self):
        if Vector2(*World.NEST_POSITION).get_distance_to(self.ant.location) < World.NEST_SIZE:
            if (random.randint(1, 10) == 1):
                self.ant.drop(self.ant.world.background)
                return "exploring"
        return None

    def entry_actions(self):
        self.ant.speed = 60.0
        random_offset = Vector2(random.randint(-20, 20), random.randint(-20, 20))
        self.ant.destination = Vector2(*World.NEST_POSITION) + random_offset


class AntStateHunting(State):
    def __init__(self, ant):
        State.__init__(self, "hunting")
        self.ant = ant
        self.got_kill = False

    def do_actions(self):
        spider = self.ant.world.get(self.ant.spider_id)
        if spider is None:
            return
        self.ant.destination = spider.location
        if self.ant.location.get_distance_to(spider.location) < 15:
            if random.randint(1, 5) == 1:
                spider.bitten()
                if spider.health <= 0:
                    self.ant.carry(spider.image)
                    self.ant.world.remove_entity(spider)
                    self.got_kill = True

    def check_conditions(self):
        if self.got_kill:
            return "delivering"
        spider = self.ant.world.get(self.ant.spider_id)
        if spider is None:
            return "exploring"
        if spider.location.get_distance_to(World.NEST_POSITION) > World.NEST_SIZE * 3:
            return "exploring"

        return None

    def entry_actions(self):
        self.speed = 160 + random.randint(0, 50)

    def exit_actions(self):
        self.got_kill = False
        
