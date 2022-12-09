import pygame

pygame.init()
fonte = pygame.font.SysFont('arial', 20, True, False) 

mensagem = f"Desenvolvedores: "

bruno = "Bruno Maffezzoli Rodrigues"
davi = "Davi Gabriel Krueger"
heloisa = "Heloisa Loos Pasta"
yasmin = "Yasmin Victória Alves de Souza"



texto_formatado = fonte.render(mensagem, True, (255,255,0))
texto_formatado2 = fonte.render(bruno, True, (255,255,0))
texto_formatado3 = fonte.render(davi, True, (255,255,0))
texto_formatado4 = fonte.render(heloisa, True, (255,255,0))
texto_formatado5 = fonte.render(yasmin, True, (255,255,0))

mensagem = f"Professores: "
luiz = "Luiz Ricardo Uriarte"
ricardo = "Ricardo de La Rocha Ladeira"

texto_formatado6 = fonte.render(mensagem, True, (255,255,0))
texto_formatado7 = fonte.render(luiz, True, (255,255,0))
texto_formatado8 = fonte.render(ricardo, True, (255,255,0))