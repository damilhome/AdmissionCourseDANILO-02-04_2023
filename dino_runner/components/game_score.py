from dino_runner.components.game import Game

class GameScore:
    def __init__(self):
        self.score = Game()
        self.o_score = self.score.score

    def score_to_update(self):
        return self.o_score