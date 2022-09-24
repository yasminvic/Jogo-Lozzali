import pygame
import random

from sprite import *


class Palavra(pygame.sprite.Sprite):
    def __init__(self, image, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.comp = self.image.get_width()
        alt = self.image.get_height()
        self.image = pygame.transform.scale(
                        self.image, (int(self.comp*scale), int(alt*scale))).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


listaPalavras = [[lo_img, ja_img]]
palavraAle = 0

palavra1 = Palavra(listaPalavras[palavraAle][0], 150, 200, 0.5)        
palavra2 = Palavra(listaPalavras[palavraAle][1], 430, 440, 0.5)   
    