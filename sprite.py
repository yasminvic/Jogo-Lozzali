import pygame

# carregar imagens

# se a imagem for transparente, o convert alpha conserva isso


sprite_sheet_naoverbal = pygame.image.load("sprites/nao_verbal.png")
pause_img = sprite_sheet_naoverbal.subsurface((160,0), (32, 32))
home_img = sprite_sheet_naoverbal.subsurface((96, 0), (32,32))

sprite_sheet_palavras = pygame.image.load("sprites/menu_palavra.png")
jogar_img = sprite_sheet_palavras.subsurface((0, 0), (186, 32))
regras_img = sprite_sheet_palavras.subsurface((186, 0), (186, 32))
sair_img = sprite_sheet_palavras.subsurface((372, 0), (186, 32))

flecha_img = pygame.image.load("sprites/flecha.png")

gameOver_img = pygame.image.load("sprites/gameOver.png")
pauseTela_img = pygame.image.load("sprites/pauseTela.png")
venceuTela_img = pygame.image.load("sprites/venceuTela.png")
mapa_galaxia = pygame.image.load("sprites/telaestaticaGALAXIA.png")
mapa_natal = pygame.image.load("sprites/telaNatal.png")
menu_img = pygame.image.load("sprites/menu.png")

estrela_obstaculo = pygame.image.load("sprites/estrela (1).png")
gelo_obstaculo = pygame.image.load("sprites/gelo.png")
canhao_img = pygame.image.load("sprites/canhao.png")
fogo_img = pygame.image.load("sprites/fogo.png")
neve_img = pygame.image.load("sprites/neve.png")
chave_img = pygame.image.load("sprites/chave.png")
buraconegro = pygame.image.load("sprites/buraconegro.png")
coracao_img = pygame.image.load("sprites/coracaovermelho.png")

#palavras coloridas
palavras_spritesheet = pygame.image.load("sprites/palavras.png")
lista_silabas = []
lista_palavras = []
x = 0
for i in range(0, 18):
    x += 100
    silaba = palavras_spritesheet.subsurface((x, 0), (100, 100))
    lista_palavras.append(silaba)

n = len(lista_palavras)
lista_silabas = []
for i in range(n):
    if(i%2 !=0):
        continue
    silaba1 = lista_palavras[i]
    silaba2 = lista_palavras[(i+1)%n]
    lista_silabas.append((silaba1, silaba2))

#palavas cinzas
lista_silabas_cinza = []
lista_palavras_cinza = []
x = 1800
for i in range(0, 18):
    x += 100
    silaba = palavras_spritesheet.subsurface((x, 0), (100, 100))
    lista_palavras_cinza.append(silaba)

n = len(lista_palavras_cinza)
lista_silabas_cinza = []
for i in range(n):
    if(i%2 !=0):
        continue
    silaba1 = lista_palavras_cinza[i]
    silaba2 = lista_palavras_cinza[(i+1)%n]
    lista_silabas_cinza.append((silaba1, silaba2))

traco_img = palavras_spritesheet.subsurface((0,0), (100, 100))

loja_img = pygame.image.load("sprites/loja.png")
lo_img = loja_img.subsurface((0,0), (133,31))
ja_img = loja_img.subsurface((133,0), (133,31))

anne_img = pygame.image.load("sprites/anne.png")