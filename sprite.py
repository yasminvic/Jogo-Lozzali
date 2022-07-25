import pygame

# carregar imagens

# se a imagem for transparente, o convert alpha conserva isso

menu_img = pygame.image.load("sprites/menu.png")
sprite_sheet_naoverbal = pygame.image.load("sprites/nao_verbal.png")
pause_img = sprite_sheet_naoverbal.subsurface((160,0), (32, 32))
home_img = sprite_sheet_naoverbal.subsurface((96, 0), (32,32))
sprite_sheet_palavras = pygame.image.load("sprites/menu_palavra.png")
jogar_img = sprite_sheet_palavras.subsurface((0, 0), (186, 32))
regras_img = sprite_sheet_palavras.subsurface((186, 0), (186, 32))
sair_img = sprite_sheet_palavras.subsurface((372, 0), (186, 32))
flecha_img = pygame.image.load("sprites/FLECHA.png")
mapa_galaxia = pygame.image.load("sprites/telaestaticaGALAXIA.png")
estrela_obstaculo = pygame.image.load("sprites/estrela (1).png")
buraconegro = pygame.image.load("sprites/buraconegro.png")
anne_img = pygame.image.load("sprites/anne.png")