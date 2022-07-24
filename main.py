import pygame
from pygame.locals import *

from objetos import eventos
from objetos import Menu
import constantes

relogio = pygame.time.Clock()

jogar = True
while jogar:
    relogio.tick(constantes.FPS)

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



