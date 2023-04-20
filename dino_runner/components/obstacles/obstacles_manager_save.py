import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from dino_runner.utils.constants import DEFAULT_TYPE

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.when_appears = 0


    def update(self, game):
        list_index = random.randint(0, 2)
        positionY = 0
        if list_index == 0:
            positionY = 325
        else:
            positionY = 300
        obstacle_list = [SMALL_CACTUS, LARGE_CACTUS]

        if len(self.obstacles) == 0 and game.score < 200:
            self.obstacles.apped(Cactus(SMALL_CACTUS, 325))
        elif
        if len(self.obstacles) == 0:
            if list_index == 0 or list_index == 1:
                self.obstacles.append(Cactus(obstacle_list[list_index], positionY))
            else:
                self.obstacles.append(Bird())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield and game.player.heart > 0:
                    self.obstacles.remove(obstacle)
                    game.player.heart -= 1
                elif not game.player.shield:
                    pygame.time.delay(500)
                    game.player.hammer = False
                    game.player.type = DEFAULT_TYPE
                    game.playing = False
                    game.death_count += 1
                else:
                    self.obstacles.remove(obstacle)
        if self.when_appears < 2000:
            self.when_appears += 500

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
