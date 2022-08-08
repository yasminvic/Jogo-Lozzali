import pygame


#dimensões da tela
LARGURA = 640
ALTURA = 480

#nome do jogo
TITULO_JOGO = "LOZZALI"

#tela do jogo
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO_JOGO)

#FPS
FPS = 60

#tamanho dos tiles
tile_size = 20

#cores
PRETO = (0,0,0)
AZUL = (0,2,25)
(100,149,237)
(0,128,128)
CINZA = (119,136,153)
(70,130,180)
BRANCO = (255,255,255)

#velocidade da personagem 
VELOCIDADE = 1