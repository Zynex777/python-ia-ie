# Projeto em desenvolvimento, preservado sem acrescentar etapas do jogo.
# Cada quadro processa eventos, atualiza a posição, desenha e exibe a tela.
# A cobra é uma lista de retângulos: inserir a cabeça e remover a cauda produz movimento.

#importando o pygame
from sys import exit 
from random import randint 
import pygame
from pygame.locals import *
#inicialização do pygame
pontos = 0
pygame.init()
#configura as dimensões da janela e cria a tela
LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption(f"Jogo Da Cobrinha") # define o titulo do 
#cria o relogio para controlar o fps
relogio = pygame.time.Clock()

#11.musica
pygame.mixer.music.load("BoxCat_Games_-_08_-_CPU_Talk.ogg.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
som_comida = pygame.mixer.Sound("smw_coin.wav")

#===================================
#2 definindo tamanho dos blocos e do fundo
TAMANHO_GRAMADO = 20 #Largura x altura em px

COR_FUNDO = (170,215,81) #(R,G,B)
COR_GRAMA = (135, 184, 44)

#====================================
#4 a estrutura e o estado inicial da cobra
inicio = [
    pygame.Rect(x,200,TAMANHO_GRAMADO,TAMANHO_GRAMADO)
    for x in (80,60,40)
]
# copy() cria outra lista, mas os objetos Rect iniciais continuam compartilhados.
cobra = inicio.copy()
#====================================
#5 movimento automatico da cobra
velocidade_x = TAMANHO_GRAMADO
velocidade_y = 0

#====================================
#7 A comida da cobra
comida_x = randint(0,(LARGURA - TAMANHO_GRAMADO) // TAMANHO_GRAMADO) * TAMANHO_GRAMADO
comida_y = randint(0,(ALTURA - TAMANHO_GRAMADO) // TAMANHO_GRAMADO) * TAMANHO_GRAMADO
comida = pygame.Rect(comida_x, comida_y, TAMANHO_GRAMADO, TAMANHO_GRAMADO)

pontos = 0
fonte = pygame.font.SysFont("arial",35,bold=True)

#looping que mantem a janela aberta
rodando = True
# O laço principal representa a sequência de quadros da animação.
while rodando:
    # Consome os eventos pendentes de teclado e de fechamento da janela.
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False

        #====================================
        #6 controles do teclado(setas)
        # O teste do eixo atual impede uma inversão direta para o sentido oposto.
        elif evento.type == KEYDOWN:
            if (evento.key == K_LEFT or evento.key == K_a) and velocidade_x == 0:
                velocidade_x = - TAMANHO_GRAMADO
                velocidade_y = 0
            elif (evento.key == K_RIGHT or evento.key == K_d) and velocidade_x == 0:
                velocidade_x = TAMANHO_GRAMADO
                velocidade_y = 0
            elif (evento.key == K_UP or evento.key == K_w) and velocidade_y == 0:
                velocidade_x = 0 
                velocidade_y = - TAMANHO_GRAMADO
            elif (evento.key == K_DOWN or evento.key == K_s) and velocidade_y == 0:
                velocidade_x = 0
                velocidade_y = TAMANHO_GRAMADO
                   

    #====================================
    #5 Atualizando a posição da cobra
    # Cria a próxima cabeça somando o deslocamento às coordenadas atuais.
    cabeca = pygame.Rect(
        cobra[0].x + velocidade_x,
        cobra[0].y + velocidade_y,
        TAMANHO_GRAMADO,
        TAMANHO_GRAMADO
    )
    cobra.insert(0,cabeca) #insere novo elemento da cabeca
    if cobra[0].colliderect(comida):
        comida.x = randint(0,(LARGURA-TAMANHO_GRAMADO) // TAMANHO_GRAMADO) * TAMANHO_GRAMADO
        comida.y = randint(0,(ALTURA-TAMANHO_GRAMADO) // TAMANHO_GRAMADO) * TAMANHO_GRAMADO
        pontos +=1
        pygame.mixer.Sound.play(som_comida)
        pygame.display.set_caption(f"Pontos: {pontos}")
        print(pontos)
        
    else:
        cobra.pop() #remove o ultimo item da lista cobra
    if (
        cobra[0].x < 0
        or cobra[0].x >= LARGURA
        or cobra[0].y < 0
        or cobra[0].y >= ALTURA
        or any(cobra[0].colliderect(parte) for parte in cobra[1:])
    ):
        cobra = inicio.copy()
        velocidade_x = TAMANHO_GRAMADO
        velocidade_y = 0
        pontos = 0
        comida.x = randint(0,(LARGURA - TAMANHO_GRAMADO) // TAMANHO_GRAMADO) * TAMANHO_GRAMADO
        comida.y = randint(0,(ALTURA - TAMANHO_GRAMADO) // TAMANHO_GRAMADO) * TAMANHO_GRAMADO

    #pintando toda a tela com a cor de fundo
    tela.fill(COR_FUNDO)




    #====================================
    #3 desenhando o fundo quadriculado (grama)
    # O resto x % 40 alterna o início das faixas para criar o quadriculado.
    for x in range(0,LARGURA,TAMANHO_GRAMADO): #range(inicio,fim,salto)
        for y in range(x % 40,ALTURA,40):
            pygame.draw.rect(
                tela,COR_GRAMA,(x,y,TAMANHO_GRAMADO,TAMANHO_GRAMADO)
            )

    #====================================
    #7 Desenhando a comida na tela 
    pygame.draw.rect(
        tela,
        "red",
        comida,
        0,
        10
    )

    #====================================
    #4 a estrutura e o estado inicial da cobra
    for parte in cobra:
        pygame.draw.rect(tela,"royalblue",parte,0,6)


    
    #9; renderizando e exibindo placar
    mensagem_placar = f"pontos: {pontos}"
    texto_formatado = fonte.render(mensagem_placar,True,(50,50,50))
    tela.blit(texto_formatado, (20,20))


    #atualiza o que aparece na tela
    pygame.display.flip()
    #manter a taxa de 10 quadros por segundo
    # Este valor limita a animação a 9 quadros por segundo.
    relogio.tick(9) 
#1. 
# Sem parênteses, esta linha referencia pygame.quit sem executar a função.
pygame.quit
exit()