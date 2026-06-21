#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



            # check for all events
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #pygame.quit()  # close window
                    #quit()  # end pygame
                    # da linha 1 a 14todo codigo e para criar a janela do jogo, a nossa base.
