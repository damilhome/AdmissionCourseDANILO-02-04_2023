from dino_runner.components.obstacles.moving_obstacles import movingObstacle
from dino_runner.utils.constants import BIRD

class Bird(movingObstacle):
    def __init__(self):
        super().__init__(BIRD)
        self.rect.y = 300
