#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_RED, C_WHITE
from code.Score import Score

from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def show_game_finished(self):
        faixa = pygame.Rect(0, WIN_HEIGHT // 2 - 30, WIN_WIDTH, 60)
        pygame.draw.rect(self.window,C_RED, faixa)
        fonte = pygame.font.SysFont("Lucida Sans Typewriter", 36, bold=True)
        texto = fonte.render("GAME FINISHED!!", True, C_WHITE)
        texto_rect = texto.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.window.blit(texto, texto_rect)
        pygame.display.flip()
        pygame.time.delay(2000)        # Espera 2 segundos


    def run(self, ):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        self.show_game_finished()
                        score.save(menu_return, player_score)


            elif menu_return == MENU_OPTION[3]:
                score.show_score()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass
