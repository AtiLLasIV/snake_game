import pygame

from src.DefaultParams import DefaultParams
from src.Level import Level
from src.Snake import Snake
from src.Food import Fruit, Bonus


class Game:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.level = Level()
        self.bonus = Bonus()

        # возможные состояния:
        self.main_menu_state = -1
        self.pause_state = -2
        self.game_state = 0
        self.levels_state = 1
        self.exit_state = 2
        self.current_state = self.main_menu_state
        self.timer = 200

        self.score = 0
        self.max_scores = [0, 0, 0, 0, 0]

        self.is_game_over = False

    def update(self):
        self.snake.move_snake()
        self.check_eating()
        self.check_fruit_pos()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake(self.level.snake_color)
        self.level.draw_level()
        self.draw_score()
        if self.fruit.is_draw_bonus:
            self.bonus.draw_bonus()

    def check_eating(self):
        if self.fruit.pos == self.snake.body[0]:
            self.score += 10
            if self.fruit.is_draw_bonus:
                del self.bonus
                self.bonus = Bonus()
            self.fruit.random_pos()
            if self.fruit.is_draw_bonus:
                self.bonus.random_pos()
            self.snake.add_part()
            self.timer *= 0.95
            pygame.time.set_timer(def_par.SCREEN_UPDATE, int(self.timer))
        if self.fruit.is_draw_bonus and self.bonus.pos == self.snake.body[0]:
            # повышенные очки за съедание
            if self.bonus.type_of_bonus == 1:
                self.score += 50
                self.fruit.is_draw_bonus = False
            # обнуляет таймер:
            if self.bonus.type_of_bonus == 2:
                self.score += 10
                self.timer = 200
                self.fruit.is_draw_bonus = False

    def check_fruit_pos(self):
        for block in self.level.blocks:
            if self.fruit.pos == block:
                self.fruit.random_pos()
            if self.fruit.is_draw_bonus and (self.bonus.pos == block or self.bonus.pos == self.fruit.pos):
                self.bonus.random_pos()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < def_par.cell_number or not 0 <= self.snake.body[0].y < def_par.cell_number:
            self.game_over()

        for block in self.level.blocks:
            if block == self.snake.body[0]:
                self.game_over()

        for part in self.snake.body[1:]:
            if part == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        # Музыка главного меню:
        pygame.mixer.music.load('src/music/main_menu_music.wav')
        pygame.mixer.music.play(-1)

        if self.max_scores[self.level.level] < self.score:
            self.max_scores[self.level.level] = self.score

        self.is_game_over = True
        self.current_state = self.main_menu_state

    def draw_map(self):
        pass

    def draw_score(self):
        score_text = str(self.score)
        score_surface = def_par.game_font.render(score_text, True, (0, 0, 0))
        score_x = def_par.cell_size * (def_par.cell_number - 2)
        score_y = def_par.cell_size * (def_par.cell_number - 2)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        def_par.screen.blit(score_surface, score_rect)


def_par = DefaultParams()
