import pygame

import sprite
from objetos import botao_jogar, botao_sair, botao_regras, botao_flecha, tema_galaxia
from constantes import TELA, FPS, RELOGIO


# fechar a janela
def eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


# constrói o menu
def Menu():
 # desenha tela de fundo
    TELA.blit(sprite.menu_img, (0, 0))
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
            RELOGIO.tick(FPS)
        
            # preenche tudo de preto
            TELA.fill((0, 0, 0))
            eventos()
            # desenha e verifica se o botão foi apertado
            if botao_flecha.apertar():
            # volta para o menu principal
                menu_state = "main"
                tela_regras = False
            # inicia o loop que faz tudo de novo, doideira né nem sabia que dava de fazer isso
            pygame.display.flip()
