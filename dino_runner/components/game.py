import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacles_manager import ObstacleManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.game_score import GameScore


FONT_STYLE = "freesansbold.ttf"

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = GameScore()
        self.save_score = 0
        self.h_score = 0
        self.death_count = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()
    
    def stop_game(self):
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        while self.playing:
            self.events()
            self.update()
            self.draw()   

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.score.score, self.game_speed, self.player)

    def update_score(self):
        self.score.score += 1
        self.save_score = self.score.score
        if self.score.score < 500:
            if self.score.score % 100 == 0:
                self.game_speed += 3
        elif self.score.score < 5000:
            if self.score.score % 500 == 0:
                self.game_speed += 3
        else:
            if self.score.score % 1000 == 0:
                self.game_speed += 3

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #Também aceita código hexadecimal "#FFFFFF"
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def draw_score(self):
        self.write_text_on_screen(f"Score: {self.score.score}", 900, 50, 22)
        self.write_text_on_screen(f"Highest: {self.h_score}", 900, 80, 22)

    def draw_power_up_time(self):
        if self.player.shield or self.player.hammer:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show > 0:
                self.write_text_on_screen(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds.", 370, 40, 22)
            else:
                self.player.shield = False
                self.player.hammer = False
                self.player.type = DEFAULT_TYPE


    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_SPACE):
                self.run()
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE):
                self.stop_game()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if self.death_count == 0:
            self.write_text_on_screen("Press any key to start", half_screen_width - 130, half_screen_height, 22)
        else:
            if self.save_score > self.h_score:
                self.h_score = self.save_score
            self.write_text_on_screen("GAME OVER", half_screen_width - 115, half_screen_height - 150, 33)
            self.write_text_on_screen('Press "SPACE" to restart or "ESC" to exit.', half_screen_width - 230, half_screen_height + 85, 22)
            self.screen.blit(ICON, (half_screen_width - 145, half_screen_height - 70))
            self.write_text_on_screen(f"Score: {self.save_score}", half_screen_width - 10, half_screen_height -60, 22)
            self.write_text_on_screen(f"Highest: {self.h_score}", half_screen_width - 10, half_screen_height - 30, 22)
            if self.death_count == 1:
                self.write_text_on_screen(f"Died: {self.death_count} time", half_screen_width- 10, half_screen_height, 22)
            else:
                self.write_text_on_screen(f"Died: {self.death_count} times", half_screen_width- 10, half_screen_height, 22)
            self.score.score = 0
            self.game_speed = 20
        
        pygame.display.update()
        self.handle_events_on_menu()

    def write_text_on_screen(self, text, width, height, size):
        font = pygame.font.Font(FONT_STYLE, size)
        text = font.render(text, True, (0, 0, 0))
        self.screen.blit(text, (width, height))
