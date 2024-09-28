import pygame


class DefaultParams:
    def __init__(self):
        pygame.display.set_caption('Sheriff Snekich')
        pygame.display.set_icon(pygame.image.load("src/images/icon.ico"))

        self.cell_size = 30
        self.cell_number = 26

        self.screen = pygame.display.set_mode((self.cell_number * self.cell_size, self.cell_number * self.cell_size))
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.Font("src/other/GameFont.otf", 50)

        self.cup_image = pygame.image.load('src/images/cup.png').convert_alpha()

        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, 200)


pygame.init()
