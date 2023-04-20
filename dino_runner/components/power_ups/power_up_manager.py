import random
import pygame
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.heart import Heart

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.shield_truth = False
        self.hammer_truth = False
        self.heart_truth = False

    def generate_power_up(self, score):
        self.power_up_choice = random.randint(0, 2)
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 600)
            if self.power_up_choice == 0:
                self.power_ups.append(Shield())
                self.shield_truth = True
            elif self.power_up_choice == 1:
                self.power_ups.append(Hammer())
                self.hammer_truth = True
            elif self.power_up_choice == 2:
                self.power_ups.append(Heart())
                self.heart_truth = True

    def update(self, score, game_speed, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect) and self.shield_truth:
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.shield_truth = False
                self.power_ups.remove(power_up)
            elif player.dino_rect.colliderect(power_up.rect) and self.hammer_truth:
                power_up.start_time = pygame.time.get_ticks()
                player.hammer = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.hammer_truth = False
                self.power_ups.remove(power_up)
            elif player.dino_rect.colliderect(power_up.rect) and self.heart_truth:
                player.heart += 1
                self.heart_truth = False
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
