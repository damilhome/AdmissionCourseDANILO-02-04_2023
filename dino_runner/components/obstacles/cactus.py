import random

from dino_runner.components.obstacles.obstacles import Obstacle

class Cactus(Obstacle):
    def __init__(self, image):
        self.image = image
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        if self.image == SMALL_CACTUS:
            self.rect.y = 325
        elif self.image == LARGE_CACTUS:
            self.rect.y = 300
