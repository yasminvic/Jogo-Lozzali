from random import randint
import pygame
from pygame.locals import *
from sys import exit


from inimigo import *
from sprite import *
import objetos
from constantes import *
from palavra import *
from funcoes import eventos

pygame.mixer.init()
#pygame.mixer.music.play(-1) 
barulho_colisao = pygame.mixer.Sound("musica/smw_coin.wav") 
barulho_colisao.set_volume(0.7) 

bolas_group = pygame.sprite.Group()
chave_group = pygame.sprite.Group()
missao_group = pygame.sprite.Group()

# faz os osbtáculos, constrói os mapas e personagem
class Labirinto():
    def __init__(self, data, bloco, tile_size, mapa, canhao, bola, coracao):
    # criando o labirinto


        #variavel que controla as fases
        self.naotroca = False
        self.level = 1
        self.missaoContador = 0
        self.encostavel = False

        #variáveis que desenham o mapa
        self.data = data
        self.bloco = bloco
        self.mapa = mapa
        self.canhao = canhao
        self.bola = bola
        self.tile_list = []

        #variáveis que controlam a vida
        self.coracao = coracao

        #adiciona chave dentro de um grupo
        missao_group.add(objetos.chave)
        missao_group.add(palavra1)
        missao_group.add(palavra2)

        #desenha os tiles
        self.row_count = 0
        for row in self.data:
            self.col_count = 0
            for tile in row:
                if tile == 1:
                    self.__loadImagem(self.bloco, 1)
                if tile == 2:
                    self.__loadImagem(self.canhao, 1.5)
                if tile == 3:
                    bolas = Enemy(self.bola, self.col_count * tile_size, self.row_count*tile_size, 1, "DOWN")
                    bolas_group.add(bolas)
                if tile == 4:
                    pass
                if tile == 7:
                    img = pygame.transform.rotate(self.canhao, 90)
                    self.__loadImagem(img, 1.5)
                if tile == 8:
                    self.bola_rotacionada = pygame.transform.rotate(self.bola, 90)
                    bolas = Enemy(self.bola_rotacionada, self.col_count * tile_size, self.row_count*tile_size, 1, "LEFT")
                    bolas_group.add(bolas)
                self.col_count += 1
            self.row_count += 1

    
    def draw(self):
    # desenhando o labirinto
        
        TELA.blit(self.mapa, (0,0))

        for tile in self.tile_list:
            TELA.blit(tile[0], tile[1])
        
        self.perdeVida(objetos.anne.total_vidas)

        bolas_group.update()
        bolas_group.draw(TELA)

        missao_group.draw(TELA)

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

    def colisaoBuraco(self, player):
        #transportando a personagem para o outro lado do mapa
        if objetos.buraco_negro.rect.colliderect(player.rect):
            player.rect.x = 550
            player.rect.y = 120

    def colisao_chave(self, player, chave):
        #se a personagem encostar nas palavras ou na chave
        missao_colisao = pygame.sprite.spritecollide(player, chave, False)
        if missao_colisao:
            if not self.encostavel:
                self.missaoContador += 1
                for missao in missao_colisao:
                    barulho_colisao.play()
                    missao.kill()

        if self.missaoContador == 3:
            self.level += 1
            self.MudaFase(objetos.anne)

        if self.level == 3:
            self.venceu()
              
    def MudaFase(self, player):    
        if self.level == 2:
            self.reiniciar_tela(objetos.anne, mapa_natal, gelo_obstaculo, neve_img, MAPA_NATAL)
            player.rect.x = 7
            player.rect.y = 70
        
    def mudaObjeto(self):
        if not self.naotroca:
            self.row_count = 0
            for row in self.data:
                self.col_count = 0
                for tile in row:
                    if tile == 1:
                        self.__loadImagem(self.bloco, 1)
                    if tile == 2:
                        self.__loadImagem(self.canhao, 1.5)
                    if tile == 3:
                        bolas = Enemy(self.bola, self.col_count * tile_size, self.row_count*tile_size, 1, "DOWN")
                        bolas_group.add(bolas)
                    if tile == 7:
                        img = pygame.transform.rotate(self.canhao, 90)
                        self.__loadImagem(img, 1.5)
                    if tile == 8:
                        self.bola_rotacionada = pygame.transform.rotate(self.bola, 90)
                        bolas = Enemy(self.bola_rotacionada, self.col_count * tile_size, self.row_count*tile_size, 1, "LEFT")
                        bolas_group.add(bolas)
                    if tile == 4:
                        img = pygame.transform.rotate(self.canhao, 180)
                        self.__loadImagem(img, 1.5)
                    if tile == 5:
                        self.bola_rotacionada = pygame.transform.rotate(self.bola, 90)
                        bolas = Enemy(self.bola_rotacionada, self.col_count * tile_size, self.row_count*tile_size, 1, "UP")
                        bolas_group.add(bolas)
                    self.col_count += 1
                self.row_count += 1
            self.naotroca = True

    def reiniciar_tela(self, player, mapa, bloco, bola, data):
        player.rect.x = 100
        player.rect.y = 75
        player.total_vidas = 3

        self.mapa = mapa
        self.bloco = bloco
        self.bola = bola
        self.data = data
        self.tile_list.clear()
        bolas_group.empty()
        self.naotroca = False
        self.mudaObjeto()
        self.encostavel = False
        self.missaoContador = 0

        palavra1.rect.x = random.randint(100, 300)
        palavra1.rect.y = random.randint(50, 300)

        palavra2.rect.x = random.randint(350, 400)
        palavra2.rect.y = random.randint(350, 450)

        objetos.chave.rect.x = random.randint(100, 500)
        objetos.chave.rect.y = random.randint(100, 500)

        missao_group.add(palavra1)
        missao_group.add(palavra2)
        missao_group.add(objetos.chave)

    def venceu(self):
        self.running = True
        while self.running:
            RELOGIO.tick(FPS)
            eventos()
            for event in pygame.event.get():
                if event.type == KEYDOWN: 
                    if event.key == K_y:
                        print("oi")
                        self.running = False
                        break;

            TELA.fill(CINZA)


            pygame.display.flip()

    def run(self):
        self.colisao_chave(objetos.anne, missao_group)
        self.colisaoBuraco(objetos.anne)
        self.movement_collision(objetos.anne)
        self.colisiao_bolas(objetos.anne, bolas_group)
        self.draw()
        self.encostavel = False

# objetos das classes mapas
tema_galaxia = Labirinto(MAPA_GALAXIA, estrela_obstaculo, tile_size,  mapa_galaxia, canhao_img, 
                                                                    fogo_img, 
                                                                    coracao_img)