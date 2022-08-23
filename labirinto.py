import pygame


from inimigo import *
from sprite import *
import objetos
from constantes import *


bolas_group = pygame.sprite.Group()



mapa = [
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
]


# faz os osbtáculos, constrói os mapas e personagem
class Labirinto():
    def __init__(self, data, bloco, tile_size, imagem, canhao, bola, coracao):
    # criando o labirinto

        #variáveis que desenham o mapa
        self.data = data
        self.bloco = bloco
        self.mapa = imagem
        self.canhao = canhao
        self.bola = bola
        self.tile_list = []

        #variáveis que controlam a vida
        self.coracao = coracao

        self.row_count = 0
        for row in self.data:
            self.col_count = 0
            for tile in row:
                if tile == 1:
                    self.__loadImagem(self.bloco, 1)
                if tile == 2:
                    self.__loadImagem(self.canhao, 1.5)
                if tile == 3:
                    bolas = Enemy(fogo_img, self.col_count * tile_size, self.row_count*tile_size, 1, "DOWN")
                    bolas_group.add(bolas)
                if tile == 4:
                    pass
                if tile == 7:
                    img = pygame.transform.rotate(self.canhao, 90)
                    self.__loadImagem(img, 1.5)
                if tile == 8:
                    img_fogo = pygame.transform.rotate(fogo_img, 90)
                    self.bola = Enemy(img_fogo, self.col_count * tile_size, self.row_count*tile_size, 1, "LEFT")
                    bolas_group.add(self.bola)
                self.col_count += 1
            self.row_count += 1
    
    def draw(self):
    # desenhando o labirinto
        for tile in self.tile_list:
            TELA.blit(tile[0], tile[1])
        
        self.perdeVida(objetos.anne.total_vidas)

        bolas_group.update()
        bolas_group.draw(TELA)

    def __loadImagem(self, img, scale):
        #redimensionando as imagens e colocando todas em uma lista
        img = pygame.transform.scale(
                img, (int(tile_size*scale), int(tile_size*scale)))
        img_rect = img.get_rect()
        img_rect.x = self.col_count * tile_size
        img_rect.y = self.row_count * tile_size
        tile = (img, img_rect)
        self.tile_list.append(tile)
    
    def colisiao_bolas(self, player, enemy):
        #se a bola encostar na personagem:
        if pygame.sprite.spritecollide(player, enemy, False):
            player.colisao_inimigo()
            #self.()
             
    def collision_teste(self, player):
        # testando a colisão com os tiles
        # o que estavamos fazendo errado é que estavamos testando a colisão e fazendo colidir tudo junto
        # esse jeito aqui debaixo é mais fácil
        collisions = []
        for tile in self.tile_list:
            if tile[1].colliderect(player.rect):
                collisions.append(tile[1])
        return collisions
        

    def movement_collision(self, player):
        #realizando a colisão entre as tile e a personagem
        directionx = player.valor_x
        directiony = player.valor_y

        # recebe uma lista com as colisões
        colisao = self.collision_teste(objetos.anne)

        # para cada tile na colisão
        for tile in colisao:
        # se o valor que faz ela andar for maior que 0
            if directionx > 0:
        # o lado direito dela recebe o lado esquerdo do tile
                player.rect.right = tile.left
            if directionx < 0:
                player.rect.left = tile.right
        for tile in colisao:
            if directiony > 0: 
               player.rect.bottom = tile.top
            if directiony < 0:
                player.rect.top = tile.bottom 

    def perdeVida(self, total_vidas):
        for vida in range(total_vidas):
            objetos.coracao.rect.x = 500 + objetos.coracao.comp * vida
            objetos.coracao.draw()


    def morreu(self, total_vidas):
        if total_vidas <= 0:
            return False
        else:
            return True

    def colisaoBuraco(self, player):
        #transportando a personagem para o outro lado do mapa
        if objetos.buraco_negro.rect.colliderect(player.rect):
            player.rect.x = 550
            player.rect.y = 120

    def run(self):
        TELA.blit(self.mapa, (0,0))
        self.colisaoBuraco(objetos.anne)
        self.movement_collision(objetos.anne)
        self.colisiao_bolas(objetos.anne, bolas_group)
        self.draw()

# objetos das classes mapas
tema_galaxia = Labirinto(mapa, estrela_obstaculo, tile_size, mapa_galaxia,  
                                                                    canhao_img, 
                                                                    fogo_img, 
                                                                    coracao_img)