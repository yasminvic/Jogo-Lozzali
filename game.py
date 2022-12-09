import pygame
from pygame.locals import *

from texto import *
from constantes import *
from sprite import *
import objetos
from funcoes import *
import labirinto
from botao import *
from palavra import *

#falando a palavra
som = palavra1.audio
audio_palavra = pygame.mixer.Sound(som)

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        

    def newGame(self):
        self.run()

    def run(self):
        #loop do jogo
        self.jogando = True
        while self.jogando:
            RELOGIO.tick(FPS)

            self.modifica()

            if botao_pause.apertar():
                self.paused() 
            
            pygame.display.flip()

    def modifica(self):
        #todas as funcões que modificam o jogo
        eventos()
        labirinto.tema_galaxia.run()
        objetos.buraco_negro.draw()
        objetos.anne.update()
        self.game_over()
        self.venceu()
    
    def venceu(self):
        if labirinto.tema_galaxia.level >= 3:
            running = True
            while running:
                RELOGIO.tick(FPS)
                eventos()
                TELA.blit(venceuTela_img, (0,0))
                if pygame.key.get_pressed()[K_SPACE] and labirinto.tema_galaxia.apertar: 
                    labirinto.tema_galaxia.apertar = False
                    self.reiniciar(labirinto.tema_galaxia)
                    labirinto.tema_galaxia.level = 1
                    running = False
                    self.newGame()
                pygame.display.flip()

    def game_over(self):
        #tela de game over     
        game_over = objetos.anne.morreu()
        if game_over == False:
            self.jogando = False
            perdeu = True
            while perdeu:
                RELOGIO.tick(FPS)
                eventos()
                TELA.blit(gameOver_img, (0,0))
                if botao_jogar.apertar():
                    self.reiniciar(labirinto.tema_galaxia)
                    labirinto.tema_galaxia.level = 1
                    perdeu = False
                    self.newGame()
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
            eventos()
            TELA.blit(pauseTela_img, (0,0))
            if botao_jogar.apertar():
                pause = False
            if botao_sair.apertar():
                pygame.quit()
                exit()
            pygame.display.flip()
    
    def reiniciar(self, labirinto):
        #reiniciar o jogo
        labirinto.reiniciar_tela(objetos.anne, mapa_galaxia, estrela_obstaculo, fogo_img, MAPA_GALAXIA)

    def menu(self):
         # desenha tela de fundo
        TELA.blit(menu_img, (0, 0))
        self.menu_state = "main"
        # verifica se é o menu principal
        if self.menu_state == "main":
        # draw screen buttons
            if botao_jogar.apertar():
                audio_palavra.play()
                self.newGame()               
            if botao_regras.apertar():
                self.menu_state = "options"
            if botao_sair.apertar():
                self.running = False
                pygame.quit()
                exit()
        # check if the options menu is open
        if self.menu_state == "options":
        # inicia o loop
            self.regras()

    def regras(self):
        tela_regras = True
        while tela_regras:
            RELOGIO.tick(FPS)
            
            # preenche tudo de preto
            TELA.fill((0, 0, 0))

            TELA.blit(texto_formatado, (100, 15))
            TELA.blit(texto_formatado2, (150, 65))
            TELA.blit(texto_formatado3, (150, 115))
            TELA.blit(texto_formatado4, (150, 165))
            TELA.blit(texto_formatado5, (150, 215))
            TELA.blit(texto_formatado6, (100, 285))
            TELA.blit(texto_formatado7, (150, 335))
            TELA.blit(texto_formatado8, (150, 385))
                
            eventos()
            # desenha e verifica se o botão foi apertado
            if botao_flecha.apertar():
            # volta para o menu principal
                self.menu_state = "main"
                tela_regras = False
            # inicia o loop que faz tudo de novo, doideira né nem sabia que dava de fazer isso
            pygame.display.flip()