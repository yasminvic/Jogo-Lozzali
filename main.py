import pygame
from pygame.locals import *


from constantes import FPS, RELOGIO
from funcoes import eventos
from game import Game

g = Game()
while g.running:
    RELOGIO.tick(FPS)

    # fechar a janela
    eventos()

    # chamando a função que desenha o menu
    g.menu()

    pygame.display.update()
