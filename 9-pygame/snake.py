#importando o pygame
from sys import exit 
import pygame
from pygame.locals import *
#inicialização do pygame
pygame.init()
#configura as dimensões da janela e cria a tela
LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("SNAKE GAME") # define o titulo do 
#cria o relogio para controlar o fps
relogio = pygame.time.Clock()
#===================================
#2 definindo tamanho dos blocos e do fundo
TAMANHO_GRAMADO = 20 #Largura x altura em px

COR_FUNDO = (170,215,81) #(R,G,B)
COR_GRAMA = (162,209,73)





#looping que mantem a janela aberta
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
    tela.fill(COR_FUNDO)
    #atualiza o que aparece na tela
    pygame.display.flip()
    #manter a taxa de 10 quadros por segundo
    relogio.tick(10) 
#1. 
pygame.quit
exit()