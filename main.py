import pygame
from pygame.locals import *
import objetos
import constantes

relogio = pygame.time.Clock()

jogar = True
while jogar:
    relogio.tick(constantes.FPS)

    # fechar a janela
    objetos.eventos()

    # chamando a função que desenha o menu
    objetos.Menu()

    pygame.display.update()

"""
criar um .py que vai ter o while principal
dps chamar esse arquivo, em forma de def no main
criar um def run que vai ter parametro mapa, onde vamos colocar a imagem de cada mapa



tem que desenhar a anne dentro da classe labirinto
"""
