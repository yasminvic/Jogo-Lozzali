import pygame

from constantes import *
from sprite import *
import objetos
from funcoes import *
import labirinto



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

            if objetos.botao_pause.apertar():
                self.paused()
            if objetos.botao_home.apertar():
                self.reiniciar()
                self.jogando = False 
            
            pygame.display.flip()

    def modifica(self):
        #todas as funcões que modificam o jogo
        eventos()
        labirinto.tema_galaxia.run()
        objetos.buraco_negro.draw()
        objetos.anne.update()
        #self.perdeVida(anne.total_vidas)
        self.game_over()

    def game_over(self):
        #tela de game over     
        game_over = objetos.anne.morreu()
        if game_over == False:
            self.jogando = False
            perdeu = True
            while perdeu:
                RELOGIO.tick(FPS)
                eventos()
                TELA.fill(CINZA)
                if objetos.botao_jogar.apertar():
                    self.reiniciar()
                    self.newGame()
                    #self.jogando = True #colocar ou não?
                    perdeu = False
                if objetos.botao_sair.apertar():
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
            TELA.fill(CINZA)
            if objetos.botao_jogar.apertar():
                pause = False
            if objetos.botao_sair.apertar():
                pygame.quit()
                exit()
            pygame.display.flip()
    
    def reiniciar(self):
        #reiniciar o jogo
        objetos.anne.rect.x = 150
        objetos.anne.rect.y = 60
        objetos.anne.total_vidas = 3

    def menu(self):
         # desenha tela de fundo
        TELA.blit(menu_img, (0, 0))
        self.menu_state = "main"
        # verifica se é o menu principal
        if self.menu_state == "main":
        # draw screen buttons
            if objetos.botao_jogar.apertar():
                self.newGame()
            if objetos.botao_regras.apertar():
                self.menu_state = "options"
            if objetos.botao_sair.apertar():
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
            eventos()
            # desenha e verifica se o botão foi apertado
            if objetos.botao_flecha.apertar():
            # volta para o menu principal
                self.menu_state = "main"
                tela_regras = False
            # inicia o loop que faz tudo de novo, doideira né nem sabia que dava de fazer isso
            pygame.display.flip()