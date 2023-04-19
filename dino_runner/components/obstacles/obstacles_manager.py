import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.game import Game
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from dino_runner.utils.constants import DEFAULT_TYPE

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.o_game = Game()
        self.o_score = self.o_game.score.score

    def update(self, game):
        obstacle_list = random.choice([SMALL_CACTUS, LARGE_CACTUS, "BIRD"])
        positionY = 325 if obstacle_list == SMALL_CACTUS else 300

        if len(self.obstacles) == 0 and self.o_score < 200:
            self.obstacles.append(Cactus(SMALL_CACTUS, 325))
        elif len(self.obstacles) == 0 and self.o_score < 400:
            i = random.choice((SMALL_CACTUS, LARGE_CACTUS))
            y = 325 if i == SMALL_CACTUS else 300
            self.obstacles.append(Cactus(i, y))
        elif len(self.obstacles) == 0 and self.o_score > 400:
            if obstacle_list == SMALL_CACTUS or LARGE_CACTUS:
                self.obstacles.append(Cactus(obstacle_list, positionY))
            else:
                self.obstacles.append(Bird())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.player.hammer = False
                    game.player.type = DEFAULT_TYPE
                    game.playing = False
                    game.death_count += 1
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
