# coding: utf8
import pygame, sys
from pygame.locals import *
import random
from banco import Banco
from explosao import Explosao
from colisao import Colisao
from tiro import Tiro
from inimigo import Inimigo

#------ inicia padrão do pygame --------------------------------------
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('THE TANK')
fpsClock = pygame.time.Clock()
pygame.mixer.init()
#------ fim dos principios iniciais padrão do pygame ------------------

#variaveis globais---------------------------------------
#banco
banco=Banco()
banco.criadorDeTabelas()
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
jogo="begin"
listaInimigo=list()
listaInimigo.append(Inimigo(DISPLAYSURF))
inimigosQTD=1
matouInimigo=False
colisao=Colisao()
piscaLetra=float(0)
inicializa=False
listaExplosaoForaDoObjeto=list()
auxMusicadeFundo=True
somTiro =pygame.mixer.Sound("shot.wav")
somExplosao =pygame.mixer.Sound("explosion.wav")

#dificuldades e pontuações
nivel=1
tanksAbatidos=0
score=0
#variaveis globais---------------------------------------

#inicio das funções estruturadas----------------------------
def zera():
	global auxMusicadeFundo,listaExplosaoForaDoObjeto,bala,x,y,keyPressed,orientacao,orientacaoTiro,jogo,listaInimigo,inimigosQTD,matouInimigo,colisao,piscaLetra
	inicializa=False
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
	listaInimigo=list()
	listaInimigo.append(Inimigo(DISPLAYSURF))
	inimigosQTD=1
	matouInimigo=False
	colisao=Colisao()
	piscaLetra=float(0)
	listaExplosaoForaDoObjeto=list()

#função basica para finalizar o jogo ao receber o comando de fechamento
def finaliza():
	global banco
	banco.fechaConexao()
	pygame.quit()
	sys.exit()

#função que controla todos os eventos recebidos so teclado
def controleDeEventos(event):
	global somTiro,x,y,orientacao,bala,orientacaoTiro
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
		#instancia o objeto tiro
		somTiro.play(0)
		somTiro.set_volume(0.4)
		bala.append(Tiro(x,y,orientacao,(0,100,0)))
	else:
		orientacaoTiro="NOT"

#função para controlar as balas instanciadas
def controleTiro():
	global x,y,bala
	#este for é de grande importancia para o controle das balas
	#a cada loop do jogo esse for realiza uma serie de outros loop 
	#de forma mais rapida que o loop normal do jogo fazendo toda
	#impressão de movimentação das balas no senario 
	for i in range(len(bala)):
		bala[i].atira()
		bala[i].drawBala(DISPLAYSURF)
		if(bala[i].x > 550 or bala[i].x < -50):
			del bala[i]
			break
		if(bala[i].y > 550 or bala[i].y < -50):
			del bala[i]
			break
		
#função que atraves de variaveis manipuladas controla a movimentações e ações do tank 		
def controlePersonagem():
	global x,y,keyPressed,orientacao,orientacaoTiro
	
	if(keyPressed==True and orientacao=="DIREITA" and orientacaoTiro=="NOT" and x <=470):
		x+=4
	if(keyPressed==True and orientacao=="ESQUERDA" and orientacaoTiro=="NOT" and x >=0):
		x-=4
	if(keyPressed==True and orientacao=="CIMA" and orientacaoTiro=="NOT" and y>=0):
		y-=4
	if(keyPressed==True and orientacao=="BAIXO" and orientacaoTiro=="NOT" and y<=470):
		y+=4

#função que desenha o tank do personagem principal
def tanque(posicao,tamanho):
	global x,y,jogo

	pygame.draw.rect(DISPLAYSURF,  (0,100,0), (x, y, tamanho, tamanho))
	if(posicao=="BAIXO"):
		pygame.draw.rect(DISPLAYSURF,  (0,100,0), (x+(tamanho/3), y+tamanho, tamanho/3, tamanho/3))
	elif(posicao=="CIMA"):
		pygame.draw.rect(DISPLAYSURF,  (0,100,0), (x+(tamanho/3), y-(tamanho/3), tamanho/3, tamanho/3))
	elif(posicao=="DIREITA"):
		pygame.draw.rect(DISPLAYSURF,  (0,100,0), (x+tamanho, y+(tamanho/3), tamanho/3, tamanho/3))
	elif(posicao=="ESQUERDA"):
		pygame.draw.rect(DISPLAYSURF,  (0,100,0), (x-(tamanho/3), y+(tamanho/3), tamanho/3, tamanho/3))

def controleDeInimigo():
	global nivel,jogo,colisao,bala,listaInimigo,inimigosQTD,matouInimigo
	for i in range(len(listaInimigo)):
		listaInimigo[i].draw(30);
		listaInimigo[i].controleDeMovimento();
	if(len(listaInimigo)==0):
		zera()
		nivel+=1
		jogo="vitoria"

def controleDeColisao():
	global banco,DISPLAYSURF,score,tanksAbatidos,nivel,somExplosao,time,listaExplosaoForaDoObjeto,colisao,bala,listaInimigo,inimigosQTD,matouInimigo,jogo,x,y

	#minha bala no Inimigo
	for i in range(len(listaInimigo)):
		for j in range(len(bala)):
			if(colisao.colisorQuadrado([5,bala[j].x,bala[j].y],[30,listaInimigo[i].x,listaInimigo[i].y])==True):
				somExplosao.play(0)
				somExplosao.set_volume(0.5)
				listaExplosaoForaDoObjeto.append(Explosao(bala[j].x,bala[j].y,(0,255,0),DISPLAYSURF))				
				del bala[j]
				matouInimigo=True
				break
		if(matouInimigo==True):
			score+=5
			tanksAbatidos+=1
			del listaInimigo[i]
			if(inimigosQTD>5):
				matouInimigo=False
			break

	if(matouInimigo==True and inimigosQTD<=5):
		inimigosQTD+=1
		for aux in range(nivel):
			listaInimigo.append(Inimigo(DISPLAYSURF))
		matouInimigo=False

	#bala do inimigo em mim
	for k in range(len(listaInimigo)):
		for l in range(len(listaInimigo[k].bala)):

			if(colisao.colisorQuadrado([5,listaInimigo[k].bala[l].x,listaInimigo[k].bala[l].y],[30,x,y])==True):
				jogo="gameover"
				somExplosao.play(0)
				somExplosao.set_volume(0.5)
				zera()
				banco.inserir(score)
				break
		if(jogo=="gameover"):
			zera()
			break
	#inimigo em mim
	for m in range(len(listaInimigo)):
		if(colisao.colisorQuadrado([30,listaInimigo[m].x,listaInimigo[m].y],[30,x,y])==True):
				jogo="gameover"
				somExplosao.play(0)
				somExplosao.set_volume(0.5)
				zera()
				banco.inserir(score)
				break
		if(jogo=="gameover"):
			zera()
			break

	for n in range(len(listaExplosaoForaDoObjeto)):
		listaExplosaoForaDoObjeto[n].explode()

def telaJogoPrincipal():
	global event,pygame,keyPressed,orientacaoTiro

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
	controleDeColisao()
	controlePersonagem()
	tanque(orientacao,30)
	controleDeInimigo()

def telaGameOver():
	global score,tanksAbatidos,nivel,jogo,auxMusicadeFundo
	img = pygame.display.set_mode((500, 500))
	#importar imagem
	image = pygame.image.load("url.png")
	img.blit(image, (110, 150))
	telaDePontuacao(False)
	palavraPiscando("PRESSIONE TECLA TAB PARA VOLTAR!");

	for event in pygame.event.get():	
		if event.type == QUIT:
			finaliza()
		
		if(event.key==K_TAB):
			auxMusicadeFundo=True
			nivel=1
			tanksAbatidos=0
			score=0
			jogo="begin"

def telaDePontuacao(vitoria):
	global banco,score,tanksAbatidos,DISPLAYSURF,nivel

	minhaFont = pygame.font.SysFont("monospace", 20)
	
	if(vitoria==True):
		label = minhaFont.render("NIVEL: "+str(nivel), 1, (255,255,0))
		DISPLAYSURF.blit(label, (20, 300))
		label = minhaFont.render("PONTOS ACUMULADO: "+str(score), 1, (255,255,0))
		DISPLAYSURF.blit(label, (20, 400))	
		label = minhaFont.render("INIMIGOS ABATIDOS: "+str(tanksAbatidos), 1, (255,255,0))
		DISPLAYSURF.blit(label, (20, 350))
	else:
		label = minhaFont.render("RECORD: "+str(banco.busca()[0][1]), 1, (255,255,0))
		DISPLAYSURF.blit(label, (20, 50))
		label = minhaFont.render("PONTOS ACUMULADO: "+str(score), 1, (255,255,0))
		DISPLAYSURF.blit(label, (20, 80))
		label = minhaFont.render("INIMIGOS ABATIDOS: "+str(tanksAbatidos), 1, (255,255,0))
		DISPLAYSURF.blit(label, (20, 110))


def palavraPiscando(texto):
	global piscaLetra
	piscaLetra+=1
	minhaFont = pygame.font.SysFont("monospace", 20)
	label = minhaFont.render(texto, 1, (255,255,0))
	if(piscaLetra%5<=3):
		DISPLAYSURF.blit(label, (20, 450))

def paginaInicial():
	global jogo,pygame,DISPLAYSURF,piscaLetra,auxMusicadeFundo
	img = pygame.display.set_mode((500, 500))
	if(auxMusicadeFundo==True):
		auxMusicadeFundo=False
		pygame.mixer.music.load("music.mp3")
		pygame.mixer.music.play(-1)

	#importar imagem
	image = pygame.image.load("fundoInicial.png")
	img.blit(image, (0, 0))

	palavraPiscando("PRESSIONE TECLA TAB PARA INICIAR!")

	for event in pygame.event.get():	
		if event.type == QUIT:
			finaliza()
		if(event.type==KEYDOWN):
			if(event.key==K_TAB):
				jogo="play"

def paginaVitoria():
	global jogo,auxMusicadeFundo

	img = pygame.display.set_mode((500, 500))
	#importar imagem
	image = pygame.image.load("vitoria.png")
	img.blit(image, (0, 0))
	palavraPiscando("PRESSIONE TECLA TAB PARA CONTINUAR!");

	telaDePontuacao(True)
	for event in pygame.event.get():	
		if event.type == QUIT:
			finaliza()
		if(event.key==K_TAB):
			auxMusicadeFundo=True
			zera()
			jogo="play"

def menuTela():
	global jogo
	if(jogo=="play"):
		telaJogoPrincipal()
	elif(jogo=="gameover"):
		telaGameOver()
	elif(jogo=="begin"):
		paginaInicial()
	elif(jogo=="vitoria"):
		paginaVitoria()

#jogo="gameover"
while True:
	#limpa Tela
	DISPLAYSURF.fill((0, 0, 0))
	menuTela();

	pygame.display.update()
	fpsClock.tick(35)
