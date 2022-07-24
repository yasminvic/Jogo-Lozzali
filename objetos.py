import pygame
from pygame.locals import *
import os  # importar os diretórios
import constantes
from sys import exit

pygame.init()

# guarda o diretorio desse arquivo até a pasta arquivo, é o caminho absoluto
diretorio_main = os.path.dirname(__file__)
# juntando os diretórios das sprites com o dos arquivos py
diretorio_sprites = os.path.join(diretorio_main, "sprites")

pygame.display.set_caption(constantes.TITULO_JOGO)

tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))

# carregar imagens
menu_img = pygame.image.load("sprites/menu.png")
# se a imagem for transparente, o convert alpha conserva isso
sprite_sheet_naoverbal = pygame.image.load("sprites/nao_verbal.png")
pause_img = sprite_sheet_naoverbal.subsurface((160,0), (32, 32))
home_img = sprite_sheet_naoverbal.subsurface((96, 0), (32,32))
sprite_sheet_palavras = pygame.image.load("sprites/menu_palavra.png")
jogar_img = sprite_sheet_palavras.subsurface((0, 0), (186, 32))
regras_img = sprite_sheet_palavras.subsurface((186, 0), (186, 32))
sair_img = sprite_sheet_palavras.subsurface((372, 0), (186, 32))
flecha_img = pygame.image.load("sprites/flecha.gif")
mapa_galaxia = pygame.image.load("sprites/telaestaticaGALAXIA.png")
estrela_obstaculo = pygame.image.load("sprites/estrela (1).png")
anne_img = pygame.image.load("sprites/anne.png")


tile_size = 20


# mapa do jogo
mapa = [
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
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


# fechar a janela
def eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# constrói o menu
def Menu():
    # desenha tela de fundo
    tela.blit(menu_img, (0, 0))
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
            # inicia o loop que faz tudo de novo, doideira né nem sabia que dava de fazer isso
                while True:
                    Menu()
                    eventos()
                    pygame.display.flip()
            pygame.display.flip()


# faz os osbtáculos, constrói os mapas e personagem
class Labirinto():
    def __init__(self, data, bloco, tile_size, imagem):
    # criando o labirinto
        self.bloco = bloco
        self.mapa = imagem
        self.tile_list = []
        #buraco_negro = pygame.image.load("sprites/buraconegro.png")
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(
                                self.bloco, (tile_size, tile_size))
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
            tela.blit(tile[0], tile[1])
 
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
        anne.rect.x = 180
        anne.rect.y = 80


    def jogo(self):
        self.jogando = True
        while self.jogando:
            eventos()
            tela.fill(constantes.PRETO)
            tela.blit(self.mapa, (0, 0))
            self.draw()
            anne.update()
            if botao_pause.apertar():
                self.paused()
            if botao_home.apertar():
                self.reiniciar()
                self.jogando = False   
            self.movement_collision()
            for i in range(1, 10):
                # print("oi")
                if i == 10:
                    self.jogando = False
            pygame.display.flip()

    def update(self):
        self.jogo()


# objetos das classes mapas
tema_galaxia = Labirinto(mapa, estrela_obstaculo, tile_size, mapa_galaxia)


# criando objetos da classe objetos
botao_jogar = Objetos(jogar_img, 250, 180, 1)
botao_regras = Objetos(regras_img, 240, 230, 1)
botao_sair = Objetos(sair_img, 265, 280, 1)
botao_flecha = Objetos(flecha_img, 8, 410, 3)
botao_pause = Objetos(pause_img, 10, 0, 2)
botao_home = Objetos(home_img, 65, 0, 2)
anne = Objetos(anne_img, 180, 80, 1)

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