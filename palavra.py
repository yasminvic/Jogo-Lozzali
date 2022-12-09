import pygame
import random

from sprite import *
from sons import *


class Palavra(pygame.sprite.Sprite):
    def __init__(self, image, x, y, scale, id, audio):
        pygame.sprite.Sprite.__init__(self)
        self.audio = audio #falando as silabas
        self.id = id #na hora de tirar do menu
        self.scale = scale
        self.image = image
        self.comp = self.image.get_width()
        self.alt = self.image.get_height()
        self.image = pygame.transform.scale(
                        self.image, (int(self.comp*self.scale), int(self.alt*self.scale))).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




palavraAle = random.randint(0, 8)

palavra1 = Palavra(lista_silabas[palavraAle][0], 150, 200, 0.5, 1, list_sons[palavraAle])    
palavra2 = Palavra(lista_silabas[palavraAle][1], 430, 440, 0.5, 2, list_sons[palavraAle])   

palavra1_menu = Palavra(lista_silabas_cinza[palavraAle][0], 250, 10, 0.5, 1, list_sons[palavraAle])    
palavra2_menu = Palavra(lista_silabas_cinza[palavraAle][1], 350, 10, 0.5, 2, list_sons[palavraAle]) 

traco_menu = Palavra(traco_img, 300, 10, 0.5, 3, list_sons[palavraAle])    
chave = Palavra(chave_img, 500, 200, 1, 4, list_sons[palavraAle])