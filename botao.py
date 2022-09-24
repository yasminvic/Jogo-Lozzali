import pygame

from constantes import *
from sprite import *

class Botao:
    def __init__(self, image, x, y, scale):
        self.imagem = image
        self.comp = self.imagem.get_width()
        alt = self.imagem.get_height()
        self.imagem = pygame.transform.scale(
                        self.imagem, (int(self.comp*scale), int(alt*scale))).convert_alpha()
        self.rect = self.imagem.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cliquei = False
    
    def apertar(self):
        TELA.blit(self.imagem, (self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        action = False

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.cliquei == False:
                self.cliquei = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.cliquei = False
        return action

botao_jogar = Botao(jogar_img, 250, 180, 1)
botao_regras = Botao(regras_img, 240, 230, 1)
botao_sair = Botao(sair_img, 265, 280, 1)
botao_flecha = Botao(flecha_img, 8, 410, 3)
botao_pause = Botao(pause_img, 10, 3, 2)
