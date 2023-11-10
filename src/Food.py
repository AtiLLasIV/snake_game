import pygame
import random
from pygame.math import Vector2

from src.DefaultParams import DefaultParams


class Fruit:
    def __init__(self):
        self.random_pos()
        self.color = (255, 0, 0)
        self.is_draw_bonus = False

    def random_pos(self):
        self.x = random.randint(0, def_par.cell_number - 1)
        self.y = random.randint(0, def_par.cell_number - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.is_draw_bonus = 1 == random.randint(1, 10)  # появится ли бонус (шанс 10%)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * def_par.cell_size, self.pos.y * def_par.cell_size, def_par.cell_size,
                                 def_par.cell_size)
        pygame.draw.rect(def_par.screen, self.color, fruit_rect)


class Bonus:
    def __init__(self):
        self.color = (12, 8, 116)

    def random_pos(self):
        self.x = random.randint(0, def_par.cell_number - 1)
        self.y = random.randint(0, def_par.cell_number - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)

        self.type_of_bonus = random.randint(1, 2)
        if self.type_of_bonus == 1:
            self.color = (12, 8, 116)
        if self.type_of_bonus == 2:
            self.color = (133, 0, 75)

    def draw_bonus(self):
        fruit_rect = pygame.Rect(self.pos.x * def_par.cell_size, self.pos.y * def_par.cell_size, def_par.cell_size,
                                 def_par.cell_size)
        pygame.draw.rect(def_par.screen, self.color, fruit_rect)  # color


def_par = DefaultParams()
