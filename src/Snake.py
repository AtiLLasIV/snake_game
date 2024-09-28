import pygame
from pygame.math import Vector2

from src.DefaultParams import DefaultParams


class Snake:
    def __init__(self):
        self.body = [Vector2(7, 22), Vector2(6, 22), Vector2(5, 22)]
        self.direction = Vector2(1, 0)
        # self.default_color = (99, 154, 0)

    def draw_snake(self, color=(99, 154, 0)):
        for part in self.body:
            x_pos = part.x * def_par.cell_size
            y_pos = part.y * def_par.cell_size
            block_rect = pygame.Rect(x_pos, y_pos, def_par.cell_size, def_par.cell_size)
            pygame.draw.rect(def_par.screen, color, block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_part(self):
        body_copy = self.body[:]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]


def_par = DefaultParams()
