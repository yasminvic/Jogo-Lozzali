import pygame
from pygame.locals import *
import os  # importar os diretórios
from sys import exit

import constantes
from constantes import tela, tile_size
import sprite

pygame.init()

# guarda o diretorio desse arquivo até a pasta arquivo, é o caminho absoluto
diretorio_main = os.path.dirname(__file__)
# juntando os diretórios das sprites com o dos arquivos py
diretorio_sprites = os.path.join(diretorio_main, "sprites")



total_vidas = 6

bolas_group = pygame.sprite.Group()

# mapa do jogo
mapa = [
 [0, 5, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 0, 0],
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

# tudo que tem uma funcionalidade
class Objetos():
    def __init__(self, image, x, y, scale):
        self.imagem = image
        comp = self.imagem.get_width()
        alt = self.imagem.get_height()
        self.imagem = pygame.transform.scale(
        self.imagem, (int(comp*scale), int(alt*scale))).convert_alpha()
        self.rect = self.imagem.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cliquei = False

    def draw(self):
        tela.blit(self.imagem, (self.rect.x, self.rect.y))

    def apertar(self):
        tela.blit(self.imagem, (self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        action = False

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.cliquei == False:
                self.cliquei = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.cliquei = False
        return action

    def andar(self):
        # fazendo o personagem andar e fazendo a animação dele
        self.valor_x = 0
        self.valor_y = 0
        if pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_a]:
            if self.rect.x > 0:
                self.valor_x = -constantes.VELOCIDADE
                self.valor_y = 0
        if pygame.key.get_pressed()[K_RIGHT] or pygame.key.get_pressed()[K_d]:
            if self.rect.x < (constantes.LARGURA - 30):
                self.valor_x = constantes.VELOCIDADE
                self.valor_y = 0
        if pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_w]:
            if self.rect.y > (constantes.ALTURA - 410):
                self.valor_y = -constantes.VELOCIDADE
                self.valor_x = 0
        if pygame.key.get_pressed()[K_DOWN] or pygame.key.get_pressed()[K_s]:
            if self.rect.y < (constantes.ALTURA - 35):
                self.valor_y = constantes.VELOCIDADE
                self.valor_x = 0
        self.rect.x += self.valor_x
        self.rect.y += self.valor_y

    def update(self):
        self.draw()
        self.andar()
    
    def up(self):
        self.draw()
        self.apertar()

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
        self.movimento = 1
        self.cont = 0

    def update(self):
        if self.side == "DOWN":
            self.rect.y += self.movimento
            self.cont += 1
            if self.rect.y > constantes.ALTURA - 30:
                self.rect.y -= self.cont
                self.cont = 0
        if self.side == "LEFT":
            self.rect.x += self.movimento
            self.cont += 1
            if self.rect.x > constantes.LARGURA - 30:
                self.rect.x -= self.cont
                self.cont = 0

        


# fechar a janela
def eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# constrói o menu
def Menu():
    # desenha tela de fundo
    tela.blit(sprite.menu_img, (0, 0))
    menu_state = "main"
    # verifica se é o menu principal
    if menu_state == "main":
    # draw screen buttons
        if botao_jogar.apertar():
            tema_galaxia.update()
        if botao_regras.apertar():
            menu_state = "options"
        if botao_sair.apertar():
            pygame.quit()
            exit()
    # check if the options menu is open
    if menu_state == "options":
        # inicia o loop
        tela_regras = True
        while tela_regras:
        # preenche tudo de preto
            tela.fill((0, 0, 0))
            eventos()
            # desenha e verifica se o botão foi apertado
            if botao_flecha.apertar():
                # volta para o menu principal
                menu_state = "main"
                tela_regras = False
            # inicia o loop que faz tudo de novo, doideira né nem sabia que dava de fazer isso
            pygame.display.flip()


# faz os osbtáculos, constrói os mapas e personagem
class Labirinto():
    def __init__(self, data, bloco, tile_size, imagem, total_vidas, canhao, bola, coracao):
    # criando o labirinto
        self.data = data
        self.bloco = bloco
        self.mapa = imagem
        self.canhao = canhao
        self.bola = bola
        self.total_vidas = total_vidas
        self.coracao = coracao
        self.vidas = []
        self.tile_list = []
        row_count = 0
        for row in self.data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(
                                self.bloco, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "estrela")
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(
                                self.canhao, (tile_size*1.5, tile_size*1.5))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "canhao")
                    self.tile_list.append(tile)
                if tile == 3:
                    bolas = Enemy(sprite.fogo_img, col_count * tile_size, row_count*tile_size, 1, "DOWN")
                    bolas_group.add(bolas)
                if tile == 4:
                    img = pygame.transform.scale(
                                self.coracao, (tile_size*3, tile_size*3))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    vida = (img, img_rect)
                    self.vidas.append(vida)
                if tile == 5:
                    self.botao_pause = Objetos(sprite.pause_img, 0,0,2)
                    self.botao_pause.rect.x = col_count * tile_size
                    self.botao_pause.rect.y = row_count * tile_size
                if tile == 6:
                    self.botao_home = Objetos(sprite.home_img, 60,0,2)
                    self.botao_home.rect.x = col_count * tile_size
                    self.botao_home.rect.y = row_count * tile_size
                if tile == 7:
                    image = pygame.transform.scale(
                                self.canhao, (tile_size*1.5, tile_size*1.5))
                    img = pygame.transform.rotate(image, 90)
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, "canhao")
                    self.tile_list.append(tile)
                if tile == 8:
                    img_fogo = pygame.transform.rotate(sprite.fogo_img, 90)
                    bola = Enemy(img_fogo, col_count * tile_size, row_count*tile_size, 1, "LEFT")
                    bolas_group.add(bola)
                col_count += 1
            row_count += 1
    
    def draw(self):
        # desenhando o labirinto
        for tile in self.tile_list:
            tela.blit(tile[0], tile[1])
        for vida in self.vidas:
            tela.blit(vida[0], vida[1])
        
        bolas_group.update()
        bolas_group.draw(tela)
        
 
    def colisiao_bolas(self):
        if pygame.sprite.spritecollide(anne, bolas_group, False):
            anne.rect.x -= 15
            anne.rect.y -=5
            self.total_vidas -= 1
            if len(self.vidas) != 0:
                del(self.vidas[0])
        if self.total_vidas <= 0:
            return False
        else:
            return True
           

    def collision_teste(self):
        # testando a colisão com os tiles
        # o que estavamos fazendo errado é que estavamos testando a colisão e fazendo colidir tudo junto
        # esse jeito aqui debaixo é mais fácil
        collisions = []
        for tile in self.tile_list:
            if tile[1].colliderect(anne.rect):
                collisions.append(tile[1])
        return collisions

    def movement_collision(self):
        directionx = anne.valor_x
        directiony = anne.valor_y

        # recebe uma lista com as colisões
        colisao = self.collision_teste()

        # para cada tile na colisão
        for tile in colisao:
        # se o valor que faz ela andar for maior que 0
            if directionx > 0:
            # o lado direito dela recebe o lado esquerdo do tile
                anne.rect.right = tile.left
            if directionx < 0:
                anne.rect.left = tile.right
        for tile in colisao:
            if directiony > 0: 
                anne.rect.bottom = tile.top
            if directiony < 0:
                anne.rect.top = tile.bottom 

            
    def colisaoBuraco(self):
        if buraco_negro.rect.colliderect(anne.rect):
            anne.rect.x = 550
            anne.rect.y = 120

    def game_over(self):
        game_over = self.colisiao_bolas()
        if game_over == False:
            self.jogando = False
            perdeu = True
            while perdeu:
                eventos()
                tela.fill(constantes.CINZA)
                if botao_jogar.apertar():
                    perdeu = False
                    self.update()
                if botao_sair.apertar():
                    pygame.quit()
                    exit()
                pygame.display.flip()
        else:
            self.jogando = True
    
    def paused(self):
        pause = True
        while pause:
            eventos()
            tela.fill(constantes.CINZA)
            if botao_jogar.apertar():
                pause = False
            if botao_sair.apertar():
                pygame.quit()
                exit()
            pygame.display.flip()
    
    def reiniciar(self):
        anne.rect.x = 150
        anne.rect.y = 60
        self.total_vidas = 6
    
    def modifica(self):
        eventos()
        tela.blit(self.mapa, (0, 0))
        self.draw()
        buraco_negro.draw()
        self.colisaoBuraco()
        anne.update()
        self.colisiao_bolas()
        self.movement_collision()
        self.game_over()


    def jogo(self):
        self.jogando = True
        while self.jogando:

            self.modifica()

            if self.botao_pause.apertar():
                self.paused()
            if self.botao_home.apertar():
                self.reiniciar()
                self.jogando = False 
            
            pygame.display.flip()

    def update(self):
        self.reiniciar()
        self.jogo()


# criando objetos da classe objetos
botao_jogar = Objetos(sprite.jogar_img, 250, 180, 1)
botao_regras = Objetos(sprite.regras_img, 240, 230, 1)
botao_sair = Objetos(sprite.sair_img, 265, 280, 1)
botao_flecha = Objetos(sprite.flecha_img, 8, 410, 3)
buraco_negro = Objetos(sprite.buraconegro, 15, 410, 2)
anne = Objetos(sprite.anne_img, 0, 50, 1)

# objetos das classes mapas
tema_galaxia = Labirinto(mapa, sprite.estrela_obstaculo, tile_size, sprite.mapa_galaxia, 
                                                                    total_vidas, 
                                                                    sprite.canhao_img, 
                                                                    sprite.fogo_img, 
                                                                    sprite.coracao_img)

""" terra = pygame.image.load("sprites/terra.webp")
 self.tile_list = []
 row_count = 0
 for row in data:
 col_count = 0
 for tile in row:
 if tile == 1:
 img = pygame.transform.scale(terra, (tile_size, tile_size))
 img_rect = img.get_rect()
 img_rect.x = col_count * tile_size
 img_rect.y = row_count * tile_size
 tile = (img, img_rect)
 self.tile_list.append(tile)
 col_count += 1
 row_count += 1

 def draw(self):
 # desenhando o labirinto
 for tile in self.tile_list:
 tela.blit(tile[0], tile[1])"""

"""menu_state = "main"
 if menu_state == "main":
 if botao_sair.apertar() == True:
 pygame.quit()
 if botao_regras.apertar() == True:
 menu_state = "outros"
 if menu_state == "outros":
 if botao_sair.apertar():
 menu_state = "main"
 jogando = True
 while jogando:
 tela.fill((0,0,0))
 botao_sair.draw(10, 420)
 for event in pygame.event.get(): 
 if event.type == QUIT:
 pygame.quit()
 pygame.display.update()"""


"""if tile == 2:
img = pygame.transform.scale(
buraco_negro, (100, 100))
img_rect = buraco_negro.get_rect()
img_rect.x = col_count * tile_size
img_rect.y = row_count * tile_size
tile = (img, img_rect)
self.tile_list.append(tile)
col_count += 1row_count += 1
"""