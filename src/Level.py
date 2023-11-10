import pygame
from pygame.math import Vector2

from src.DefaultParams import DefaultParams


class Level:
    def __init__(self):
        self.blocks = []
        self.level = 0
        self.color = (255, 208, 64)
        self.snake_color = (99, 154, 0)

    def make_level(self, level_counter, max_scores):
        self.blocks.clear()
        # при достижении определенного рекорда за уровень, в этом уровне будет новый цвет змейки
        # (возможно потом сделать новый цвет уникальным для каждого уровня)
        if max_scores[level_counter] >= 500:
            self.snake_color = (153, 38, 103)
        else:
            self.snake_color = (99, 154, 0)
        if level_counter == 0:
            self.level = 0
            self.color = (255, 208, 64)

        if level_counter == 1:
            # 2 стенки по вертикали:
            self.level = 0
            self.color = (166, 241, 108)
            for i in range(15):
                self.blocks.append(Vector2(5, 5 + i))
                self.blocks.append(Vector2(20, 5 + i))
        if level_counter == 2:
            # 2 диагонали
            self.level = 2
            self.color = (214, 211, 123)
            for i in range(10):
                self.blocks.append(Vector2(13 + i, 2 + i))
                self.blocks.append(Vector2(6 + i, 13 + i))

        if level_counter == 3:
            # 1 по вертикали и 4 по горизонтали
            self.level = 3
            self.color = (191, 145, 48)
            for i in range(20):
                self.blocks.append(Vector2(13, 3 + i))
            for i in range(5):
                self.blocks.append(Vector2(5 + i, 8))
                self.blocks.append(Vector2(17 + i, 8))
                self.blocks.append(Vector2(5 + i, 18))
                self.blocks.append(Vector2(17 + i, 18))
        if level_counter == 4:
            # коробка
            self.level = 4
            self.color = (148, 148, 148)
            for i in range(15):
                self.blocks.append(Vector2(5, 5 + i))
                self.blocks.append(Vector2(20, 5 + i))
            for i in range(8):
                self.blocks.append(Vector2(9 + i, 6))
                self.blocks.append(Vector2(9 + i, 18))

    def draw_level(self):
        for block in self.blocks:
            x_pos = block.x * def_par.cell_size
            y_pos = block.y * def_par.cell_size
            block_rect = pygame.Rect(x_pos, y_pos, def_par.cell_size, def_par.cell_size)
            pygame.draw.rect(def_par.screen, (0, 0, 0), block_rect)

    def load_music(self, level_counter):
        if level_counter == 0:
            pygame.mixer.music.load('src/music/lvl1_wild_west_music.wav')
            pygame.mixer.music.play(-1)
        if level_counter == 1:
            pygame.mixer.music.load('src/music/lvl2_funny_saloon_music.wav')
            pygame.mixer.music.play(-1)
        if level_counter == 2:
            pygame.mixer.music.load('src/music/lvl3_decisive_cowboy_music.wav')
            pygame.mixer.music.play(-1)
        if level_counter == 3:
            pygame.mixer.music.load('src/music/lvl4_creepy_music.wav')
            pygame.mixer.music.play(-1)
        if level_counter == 4:
            pygame.mixer.music.load('src/music/lvl5_dungeon_music.wav')
            pygame.mixer.music.play(-1)


def_par = DefaultParams()
