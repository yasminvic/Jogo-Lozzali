import pygame

# fechar a janela
def eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()