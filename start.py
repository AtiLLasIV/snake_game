import sys
import pygame
from pygame.math import Vector2

from src.button import ButtonLevels, ButtonMainMenu
from src.DefaultParams import DefaultParams
from src.game import Game, Snake, Fruit


pygame.init()

def_par = DefaultParams()
game = Game()
button_menu = ButtonMainMenu()
button_levels = ButtonLevels()

pygame.mixer.music.load('src/music/main_menu_music.wav')
pygame.mixer.music.play(-1)

while True:
    if game.current_state == game.exit_state:
        pygame.quit()
        sys.exit()
    if game.current_state == game.levels_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.current_state = game.main_menu_state
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    button_levels.select -= 1
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    button_levels.select += 1
                if event.key == pygame.K_RETURN:
                    game.level.make_level(button_levels.select, game.max_scores)
                    game.level.load_music(button_levels.select)
                    game.current_state = game.game_state
                    game.timer = 200
                    game.snake = Snake()
                    game.fruit = Fruit()

        screen_rect = pygame.Rect(0, 0, def_par.cell_number * def_par.cell_size, def_par.cell_number * def_par.cell_size)
        pygame.draw.rect(def_par.screen, (29, 115, 115), screen_rect)
        button_levels.draw_levels(game)

    if game.current_state == game.pause_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.current_state = game.game_state
                if event.key == pygame.K_ESCAPE:
                    game.is_game_over = False
                    game.current_state = game.main_menu_state

    if game.current_state == game.main_menu_state:
        # мб потом поменять на другую ковбойскую музыку

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    button_menu.select -= 1
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    button_menu.select += 1
                if event.key == pygame.K_RETURN:
                    game.current_state = button_menu.select
                    game.level.load_music(button_levels.select)
                    game.timer = 200
                    game.snake = Snake()
                    game.fruit = Fruit()

        game.score = 0
        screen_rect = pygame.Rect(0, 0, def_par.cell_number * def_par.cell_size, def_par.cell_number * def_par.cell_size)
        pygame.draw.rect(def_par.screen, (29, 115, 115), screen_rect)
        button_menu.draw_menu()

    if game.current_state == game.game_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == def_par.SCREEN_UPDATE:
                game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if game.snake.direction.y != 1:
                        game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if game.snake.direction.y != -1:
                        game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if game.snake.direction.x != 1:
                        game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if game.snake.direction.x != -1:
                        game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_SPACE:
                    game.current_state = game.pause_state
                if event.key == pygame.K_ESCAPE:
                    game.game_over()

        def_par.screen.fill(game.level.color)
        game.draw_elements()

    pygame.display.update()
    def_par.clock.tick(60)

