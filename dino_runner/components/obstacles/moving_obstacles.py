import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class movingObstacle(Sprite):
    def __init__(self, image):
        self.image = image
        self.step_index = 0
        self.count = 0 if self.step_index < 5 else 1
        if self.step_index >= 10:
            self.step_index = 0
        self.step_index += 1
        self.rect = self.image[self.count].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.count], (self.rect.x, self.rect.y))
