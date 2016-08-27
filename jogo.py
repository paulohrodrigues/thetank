# coding: latin1
import pygame, sys
from pygame.locals import *
import random 

#------ inicia padrão do pygame --------------------------------------
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('THE TANK')
fpsClock = pygame.time.Clock()
#------ fim dos principios iniciais padrão do pygame ------------------


#lista que carregara todas as balas instanciadas
bala=list()

#posição inicial do tank
x=100	
y=100

#auxiliar para controlar o evento de keydown e keyup 
keyPressed=False

#inicializa orientação do tank durante o jogo
orientacao="BAIXO"

#momento de tiro
orientacaoTiro="NOT"





#função basica para finalizar o jogo ao receber o comando de fechamento
def finaliza():
	pygame.quit()
	sys.exit()



#função que controla todos os eventos recebidos so teclado
def controleDeEventos(event):
	global x,y,orientacao,bala,orientacaoTiro
	if event.key == K_LEFT:
		orientacao="ESQUERDA"
	if event.key == K_RIGHT:
		orientacao="DIREITA"
	if event.key == K_UP:
		orientacao="CIMA"
	if event.key == K_DOWN:
		orientacao="BAIXO"
	if event.key == K_SPACE:
		orientacaoTiro="OK"
	else:
		orientacaoTiro="NOT"


		
#função que atraves de variaveis manipuladas controla a movimentações e ações do tank 		
def controlePersonagem():
	global x,y,keyPressed,orientacao,orientacaoTiro
	
	if(keyPressed==True and orientacao=="DIREITA" and orientacaoTiro=="NOT"):
		x+=3
	if(keyPressed==True and orientacao=="ESQUERDA" and orientacaoTiro=="NOT"):
		x-=3
	if(keyPressed==True and orientacao=="CIMA" and orientacaoTiro=="NOT"):
		y-=3
	if(keyPressed==True and orientacao=="BAIXO" and orientacaoTiro=="NOT"):
		y+=3


def tanque(posicao,tamanho):
	global x,y

	pygame.draw.rect(DISPLAYSURF,  (255, 0, 0), (x, y, tamanho, tamanho))
	if(posicao=="BAIXO"):
		pygame.draw.rect(DISPLAYSURF,  (255, 0, 0), (x+(tamanho/3), y+tamanho, tamanho/3, tamanho/3))
	elif(posicao=="CIMA"):
		pygame.draw.rect(DISPLAYSURF,  (255, 0, 0), (x+(tamanho/3), y-(tamanho/3), tamanho/3, tamanho/3))
	elif(posicao=="DIREITA"):
		pygame.draw.rect(DISPLAYSURF,  (255, 0, 0), (x+tamanho, y+(tamanho/3), tamanho/3, tamanho/3))
	elif(posicao=="ESQUERDA"):
		pygame.draw.rect(DISPLAYSURF,  (255, 0, 0), (x-(tamanho/3), y+(tamanho/3), tamanho/3, tamanho/3))





while True:
	DISPLAYSURF.fill((255, 255, 255))


	

	for event in pygame.event.get():	
		if event.type == QUIT:
			finaliza()
		elif event.type == KEYDOWN:
			controleDeEventos(event)
			keyPressed = True				
		elif(event.type == KEYUP):
			keyPressed = False
			orientacaoTiro="NOT"

	controleTiro()
	controlePersonagem()
	tanque(orientacao,30)

	pygame.display.update()
	fpsClock.tick(30)