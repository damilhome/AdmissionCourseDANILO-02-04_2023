import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, HAMMER_TYPE, DUCKING_HAMMER, JUMPING_HAMMER, RUNNING_HAMMER


DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}

class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.duck_key_down = False
        self.jump_vel = self.JUMP_VEL
        self.setup_state()

    def setup_state(self):
        self.power_up_time = 0
        self.shield = False
        self.hammer = False
        self.heart = 0
        self.show_text = False
        self.shield_time_up = 0

    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5

    def update(self, user_input):
        if self.dino_run or self.dino_duck:
            self.run()
        elif self.dino_jump:
            self.jump()

        if self.step_index >= 9:
            self.step_index = 0

        if user_input[pygame.K_UP] or user_input[pygame.K_SPACE] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_duck = False
            self.dino_run = True
            self.duck_key_down = False

        if user_input[pygame.K_DOWN]:
            if not self.duck_key_down:
                self.dino_jump = False
                self.dino_run = False
                self.dino_duck = True
                self.duck_key_down = True
            else:
                self.duck_key_down = False

    def run(self):
        if self.dino_duck:
            self.image = DUCK_IMG[self.type][self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS + 40
            self.jump_vel = self.JUMP_VEL
            self.step_index += 1
        else:
            self.image = RUN_IMG[self.type][self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS
            self.jump_vel = self.JUMP_VEL
            self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump and self.hammer and self.jump_vel <= 0:
            pass
        elif self.dino_jump and self.hammer:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        else:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
