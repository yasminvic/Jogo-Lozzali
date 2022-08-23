import pygame

from constantes import ALTURA, LARGURA


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, x,y, scale, side):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        comp = self.image.get_width()
        alt = self.image.get_height()
        self.image = pygame.transform.scale(
                    self.image, (int(comp*scale), int(alt*scale))).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.side = side
        self.movimento = 3
        self.cont = 0

    def nada(self):
        pass
        if self.side == "DOWN":
            self.rect.x -= self.cont
            self.cont = 0
        if self.side == "LEFT":
            self.rect.y -= self.cont
            self.cont = 0

    def update(self):
        if self.side == "DOWN":
            self.rect.y += self.movimento
            self.cont += 3
            if self.rect.y > ALTURA - 30:
                self.rect.y -= self.cont
                self.cont = 0
        if self.side == "LEFT":
            self.rect.x += self.movimento
            self.cont += 3
            if self.rect.x > LARGURA - 30:
                self.rect.x -= self.cont
                self.cont = 0