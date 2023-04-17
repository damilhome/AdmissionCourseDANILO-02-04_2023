import random

from dino_runner.components.obstacles.obstacles import Obstacle

class Cactus(Obstacle):
    def __init__(self, image, y):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = y
