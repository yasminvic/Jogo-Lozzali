import pygame
from pygame.locals import *
import os # importar os diretórios
from math import sin #retorna o seno do valor passado

from sprite import *
from constantes import *




# guarda o diretorio desse arquivo até a pasta arquivo, é o caminho absoluto
diretorio_main = os.path.dirname(__file__)
# juntando os diretórios das sprites com o dos arquivos py
diretorio_sprites = os.path.join(diretorio_main, "sprites")



# tudo que tem uma funcionalidade
class Objeto(pygame.sprite.Sprite):
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
        self.cliquei = False

        self.valor_x = 0
        self.valor_y = 0

        #variáveis que controlam a invencibilidade 
        self.invencibilidade = False
        self.invencibilidade_duracao = 400
        self.hurt_time = 0

        #controla a vida da personagem
        self.total_vidas = 3

    def draw(self):
        if self.invencibilidade: #se invencibilidade for True:
            alpha = self.invisivel()
            self.image.set_alpha(alpha) #define a transparência
        else:
            self.image.set_alpha(255)

        TELA.blit(self.image, (self.rect.x, self.rect.y))

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

    def morreu(self):
        if self.total_vidas <= 0:
            return False
        else:
            return True

    def update(self):
        self.draw()
        self.andar()
        self.invencibilidade_timer()
 

# criando objetos da classe objetos
buraco_negro = Objeto(buraconegro, 15, 410, 2)
chave = Objeto(chave_img, 500, 200, 1)
coracao = Objeto(coracao_img, 400, 10, 2)
anne = Objeto(anne_img, 100, 75, 1)

