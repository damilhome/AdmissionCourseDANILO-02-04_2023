import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        list_index = random.randint(0, 2)
        obstacle_list = [SMALL_CACTUS, LARGE_CACTUS, BIRD]
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(obstacle_list[list_index]))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
