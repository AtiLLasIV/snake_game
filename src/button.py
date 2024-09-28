import pygame
from src.DefaultParams import DefaultParams


class ButtonMainMenu:
    def __init__(self):
        self.button_image = []
        self.button_image.insert(0, pygame.image.load('src/images/Buttons/button_start.png').convert_alpha())
        self.button_image.insert(1, pygame.image.load('src/images/Buttons/button_level.png').convert_alpha())
        self.button_image.insert(2, pygame.image.load('src/images/Buttons/button_exit.png').convert_alpha())

        self.button_image_select = []
        self.button_image_select.insert(0, pygame.image.load('src/images/Buttons/button_start_1.png').convert_alpha())
        self.button_image_select.insert(1, pygame.image.load('src/images/Buttons/button_level_1.png').convert_alpha())
        self.button_image_select.insert(2, pygame.image.load('src/images/Buttons/button_exit_1.png').convert_alpha())

        self.button_rect = []
        self.button_rect.insert(0, pygame.Rect(8 * def_par.cell_size, 7 * def_par.cell_size,
                                               16 * def_par.cell_size, 12 * def_par.cell_size))
        self.button_rect.insert(1, pygame.Rect(8 * def_par.cell_size, 12 * def_par.cell_size,
                                               16 * def_par.cell_size, 17 * def_par.cell_size))
        self.button_rect.insert(2, pygame.Rect(8 * def_par.cell_size, 17 * def_par.cell_size,
                                               16 * def_par.cell_size, 22 * def_par.cell_size))

        self.prev_select = 0
        self.select = 0

    def draw_menu(self):
        for i in range(len(self.button_rect)):
            def_par.screen.blit(self.button_image[i], self.button_rect[i])
        self.draw_select()

    def draw_select(self):
        def_par.screen.blit(self.button_image[self.prev_select], self.button_rect[self.prev_select])
        if self.select == len(self.button_rect):
            self.select = 0
        if self.select == -1:
            self.select = len(self.button_rect) - 1
        self.prev_select = self.select
        def_par.screen.blit(self.button_image_select[self.select], self.button_rect[self.select])


class ButtonLevels:
    def __init__(self):
        self.button_image = []
        self.button_image.insert(0, pygame.image.load('src/images/Buttons/Level/button_lvl1.png').convert_alpha())
        self.button_image.insert(1, pygame.image.load('src/images/Buttons/Level/button_lvl2.png').convert_alpha())
        self.button_image.insert(2, pygame.image.load('src/images/Buttons/Level/button_lvl3.png').convert_alpha())
        self.button_image.insert(3, pygame.image.load('src/images/Buttons/Level/button_lvl4.png').convert_alpha())
        self.button_image.insert(4, pygame.image.load('src/images/Buttons/Level/button_lvl5.png').convert_alpha())

        self.button_image_select = []
        self.button_image_select.insert(0, pygame.image.load(
            'src/images/Buttons/Level/button_lvl1_1.png').convert_alpha())
        self.button_image_select.insert(1, pygame.image.load(
            'src/images/Buttons/Level/button_lvl2_1.png').convert_alpha())
        self.button_image_select.insert(2, pygame.image.load(
            'src/images/Buttons/Level/button_lvl3_1.png').convert_alpha())
        self.button_image_select.insert(3, pygame.image.load(
            'src/images/Buttons/Level/button_lvl4_1.png').convert_alpha())
        self.button_image_select.insert(4, pygame.image.load(
            'src/images/Buttons/Level/button_lvl5_1.png').convert_alpha())

        self.button_rect = []
        self.button_rect.insert(0, pygame.Rect(8 * def_par.cell_size, 3 * def_par.cell_size,
                                               16 * def_par.cell_size, 7 * def_par.cell_size))
        self.button_rect.insert(1, pygame.Rect(8 * def_par.cell_size, 7 * def_par.cell_size,
                                               16 * def_par.cell_size, 11 * def_par.cell_size))
        self.button_rect.insert(2, pygame.Rect(8 * def_par.cell_size, 11 * def_par.cell_size,
                                               16 * def_par.cell_size, 15 * def_par.cell_size))
        self.button_rect.insert(3, pygame.Rect(8 * def_par.cell_size, 15 * def_par.cell_size,
                                               16 * def_par.cell_size, 19 * def_par.cell_size))
        self.button_rect.insert(4, pygame.Rect(8 * def_par.cell_size, 19 * def_par.cell_size,
                                               16 * def_par.cell_size, 23 * def_par.cell_size))

        self.cup_rect = []
        self.cup_rect.insert(0, pygame.Rect(19 * def_par.cell_size, 3.5 * def_par.cell_size,
                                            23 * def_par.cell_size, 7.5 * def_par.cell_size))
        self.cup_rect.insert(1, pygame.Rect(19 * def_par.cell_size, 7.5 * def_par.cell_size,
                                            23 * def_par.cell_size, 11.5 * def_par.cell_size))
        self.cup_rect.insert(2, pygame.Rect(19 * def_par.cell_size, 11.5 * def_par.cell_size,
                                            23 * def_par.cell_size, 15.5 * def_par.cell_size))
        self.cup_rect.insert(3, pygame.Rect(19 * def_par.cell_size, 15.5 * def_par.cell_size,
                                            23 * def_par.cell_size, 19.5 * def_par.cell_size))
        self.cup_rect.insert(4, pygame.Rect(19 * def_par.cell_size, 19.5 * def_par.cell_size,
                                            23 * def_par.cell_size, 23.5 * def_par.cell_size))

        self.prev_select = 0
        self.select = 0

    def draw_levels(self, game):
        for i in range(len(self.button_rect)):
            def_par.screen.blit(self.button_image[i], self.button_rect[i])
            def_par.screen.blit(def_par.cup_image, self.cup_rect[i])

            # выводим рекорды
            max_score_text = str(game.max_scores[i])
            max_score_surface = def_par.game_font.render(max_score_text, True, (0, 0, 0))
            score_x = 23 * def_par.cell_size
            score_y = (4.5 + 4 * i) * def_par.cell_size
            score_rect = max_score_surface.get_rect(center=(score_x, score_y))
            def_par.screen.blit(max_score_surface, score_rect)

        self.draw_select()

    def draw_select(self):
        def_par.screen.blit(self.button_image[self.prev_select], self.button_rect[self.prev_select])
        if self.select == len(self.button_rect):
            self.select = 0
        if self.select == -1:
            self.select = len(self.button_rect) - 1
        self.prev_select = self.select
        def_par.screen.blit(self.button_image_select[self.select], self.button_rect[self.select])


def_par = DefaultParams()

