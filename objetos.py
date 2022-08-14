import pygame
from pygame.locals import *
import os # importar os diretórios
from sys import exit
from math import sin #retorna o seno do valor passado

import sprite
import funcoes
from constantes import *
from inimigo import Enemy
from coracao import Coracoes


pygame.init()

# guarda o diretorio desse arquivo até a pasta arquivo, é o caminho absoluto
diretorio_main = os.path.dirname(__file__)
# juntando os diretórios das sprites com o dos arquivos py
diretorio_sprites = os.path.join(diretorio_main, "sprites")


bolas_group = pygame.sprite.Group()
coracao_group = pygame.sprite.Group()

# mapa do jogo
mapa = [
 [0, 5, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
class Objeto():
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

        #variáveis que controlam a invencibilidade 
        self.invencibilidade = False
        self.invencibilidade_duracao = 400
        self.hurt_time = 0

        #controla a vida da personagem
        self.total_vidas = 3

    def draw(self):
        if self.invencibilidade: #se invencibilidade for True:
            alpha = self.invisivel()
            self.imagem.set_alpha(alpha) #define a transparência
        else:
            self.imagem.set_alpha(255)

        TELA.blit(self.imagem, (self.rect.x, self.rect.y))


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

    def andar(self):
        # fazendo o personagem andar e fazendo a animação dele
        self.valor_x = 0
        self.valor_y = 0
        if pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_a]:
            if self.rect.x > 0:
                self.valor_x = -VELOCIDADE
                self.valor_y = 0
        if pygame.key.get_pressed()[K_RIGHT] or pygame.key.get_pressed()[K_d]:
            if self.rect.x < (LARGURA - 30):
                self.valor_x = VELOCIDADE
                self.valor_y = 0
        if pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_w]:
            if self.rect.y > (ALTURA - 410):
                self.valor_y = -VELOCIDADE
                self.valor_x = 0
        if pygame.key.get_pressed()[K_DOWN] or pygame.key.get_pressed()[K_s]:
            if self.rect.y < (ALTURA - 35):
                self.valor_y = VELOCIDADE
                self.valor_x = 0
        self.rect.x += self.valor_x
        self.rect.y += self.valor_y

    def colisao_inimigo(self):
        if not self.invencibilidade: #se a invencibilidade for not true:
            self.total_vidas -= 1 #perde uma vida
            print(self.total_vidas)
            self.invencibilidade = True #invencibilidade vira True
            self.hurt_time = pygame.time.get_ticks() #armazena o momento exato da colisão
            #pygame.time.get_ticks() retorna o número de milissegundos desde que pygame.init() foi chamado
    
    def invencibilidade_timer(self):
        if self.invencibilidade: #se invencibilidade for True:
            timer_atual = pygame.time.get_ticks() #armazena o momento atual
            #se a diferença entre o momento atual o quando colidiu for maior que o tempo estipulado para duração da invencibilidade:
            if (timer_atual - self.hurt_time) >= self.invencibilidade_duracao:  
                self.invencibilidade = False #invencibilidade recebe False
    
    def invisivel(self):
        #variável valor vai oscilar entre positivo e negativo
        valor = sin(pygame.time.get_ticks())
        if valor > 0: #se for positivo, não tem transparência
            return 255
        else:
            #se for negativo, tem transparência
            return 0

    def update(self):
        self.draw()
        self.andar()
        self.invencibilidade_timer()
 

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
        self.vidas = []

        self.row_count = 0
        for row in self.data:
            self.col_count = 0
            for tile in row:
                if tile == 1:
                    self.__loadImagem(self.bloco, 1)
                if tile == 2:
                    self.__loadImagem(self.canhao, 1.5)
                if tile == 3:
                    bolas = Enemy(sprite.fogo_img, self.col_count * tile_size, self.row_count*tile_size, 1, "DOWN")
                    bolas_group.add(bolas)
                if tile == 4:
                    pass
                if tile == 5:
                    self.botao_pause = Objeto(sprite.pause_img, 0,0,2)
                    self.botao_pause.rect.x = self.col_count * tile_size
                    self.botao_pause.rect.y = self.row_count * tile_size
                if tile == 6:
                    self.botao_home = Objeto(sprite.home_img, 60,0,2)
                    self.botao_home.rect.x = self.col_count * tile_size
                    self.botao_home.rect.y = self.row_count * tile_size
                if tile == 7:
                    img = pygame.transform.rotate(self.canhao, 90)
                    self.__loadImagem(img, 1.5)
                if tile == 8:
                    img_fogo = pygame.transform.rotate(sprite.fogo_img, 90)
                    bola = Enemy(img_fogo, self.col_count * tile_size, self.row_count*tile_size, 1, "LEFT")
                    bolas_group.add(bola)
                self.col_count += 1
            self.row_count += 1
    
    def draw(self):
    # desenhando o labirinto
        for tile in self.tile_list:
            TELA.blit(tile[0], tile[1])
        for vida in self.vidas:
            TELA.blit(vida[0], vida[1])
        
        self.perdeVida(anne.total_vidas)

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
    
    def colisiao_bolas(self):
        #se a bola encostar na personagem:
        if pygame.sprite.spritecollide(anne, bolas_group, False):
            anne.colisao_inimigo()
             
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
        #realizando a colisão entre as tile e a personagem
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

    def perdeVida(self, total_vidas):
        for vida in range(total_vidas):
            coracao.rect.x = 500 + coracao.comp * vida
            coracao.draw()


    def morreu(self, total_vidas):
        if total_vidas <= 0:
            return False
        else:
            return True


    
    def colisaoBuraco(self):
        #transportando a personagem para o outro lado do mapa
        if buraco_negro.rect.colliderect(anne.rect):
            anne.rect.x = 550
            anne.rect.y = 120

    def game_over(self):
        #tela de game over
        game_over = self.morreu(anne.total_vidas)
        if game_over == False:
            self.jogando = False
            perdeu = True
            while perdeu:
                RELOGIO.tick(FPS)
                funcoes.eventos()
                TELA.fill(CINZA)
                if botao_jogar.apertar():
                    self.update()
                    self.jogando = True
                    perdeu = False
                if botao_sair.apertar():
                    pygame.quit()
                    exit()
                pygame.display.flip()
        else:
            self.jogando = True
    
    def paused(self):
        #tela de pause
        pause = True
        while pause:
            RELOGIO.tick(FPS)
            funcoes.eventos()
            TELA.fill(CINZA)
            if botao_jogar.apertar():
                pause = False
            if botao_sair.apertar():
                pygame.quit()
                exit()
            pygame.display.flip()
    
    def reiniciar(self):
        #reiniciar o jogo
        anne.rect.x = 150
        anne.rect.y = 60
        self.total_vidas = 3
        
    def modifica(self):
        #todas as funcões que modificam o jogo
        funcoes.eventos()
        TELA.blit(self.mapa, (0, 0))
        self.draw()
        buraco_negro.draw()
        self.colisaoBuraco()
        anne.update()
        self.movement_collision()
        self.colisiao_bolas()
        #self.perdeVida(anne.total_vidas)
        self.game_over()


    def jogo(self):
        #loop do jogo
        self.jogando = True
        while self.jogando:
            RELOGIO.tick(FPS)

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
botao_jogar = Objeto(sprite.jogar_img, 250, 180, 1)
botao_regras = Objeto(sprite.regras_img, 240, 230, 1)
botao_sair = Objeto(sprite.sair_img, 265, 280, 1)
botao_flecha = Objeto(sprite.flecha_img, 8, 410, 3)
buraco_negro = Objeto(sprite.buraconegro, 15, 410, 2)
coracao = Objeto(sprite.coracao_img, 400, 10, 2)
anne = Objeto(sprite.anne_img, 0, 50, 1)

# objetos das classes mapas
tema_galaxia = Labirinto(mapa, sprite.estrela_obstaculo, tile_size, sprite.mapa_galaxia,  
                                                                    sprite.canhao_img, 
                                                                    sprite.fogo_img, 
                                                                    sprite.coracao_img)