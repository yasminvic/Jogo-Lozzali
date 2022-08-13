import pygame
from pygame.locals import *


from constantes import FPS, RELOGIO
from funcoes import eventos, Menu


jogar = True
while jogar:
    RELOGIO.tick(FPS)

    # fechar a janela
    eventos()

    # chamando a função que desenha o menu
    Menu()

    pygame.display.update()

"""
criar um .py que vai ter o while principal
dps chamar esse arquivo, em forma de def no main
criar um def run que vai ter parametro mapa, onde vamos colocar a imagem de cada mapa



tem que desenhar a anne dentro da classe labirinto
"""