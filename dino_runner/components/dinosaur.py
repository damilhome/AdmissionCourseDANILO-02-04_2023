import pygame
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING


class Dinosaur:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.duck_key_down = False
        self.jump_vel = self.JUMP_VEL

    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5

    def update(self, user_input):
        if self.dino_run or self.dino_duck:
            self.run()
        elif self.dino_jump:
            self.jump()

        if self.step_index >= 10:
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
            self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS + 40
            self.jump_vel = self.JUMP_VEL
            self.step_index += 1
        else:
            self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS
            self.jump_vel = self.JUMP_VEL
            self.step_index += 1

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
