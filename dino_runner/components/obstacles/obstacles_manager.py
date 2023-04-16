import pygame
import random

from dino_runner.components.obstacles.small_cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        self.number = random.randrange(0, 2)
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
            self.obstacles.append(Cactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles[self.number])
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
