# coding: utf8
import pygame, sys
from pygame.locals import *
import random 

#------ inicia padrão do pygame --------------------------------------
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('THE TANK')
fpsClock = pygame.time.Clock()
#------ fim dos principios iniciais padrão do pygame ------------------



#inicio dos objetos-----------------------------------

class Colisao(object):
	def colisorQuadrado(self,objeto1,objeto2):
		tamanhoObjeto1=objeto1[0]
		tamanhoObjeto2=objeto2[0]
		xObjeto1=objeto1[1]-(objeto1[0]/2)
		yObjeto1=objeto1[2]-(objeto1[0]/2)
		xObjeto2=objeto2[1]-(objeto2[0]/2)
		yObjeto2=objeto2[2]-(objeto2[0]/2)
		if(xObjeto1+tamanhoObjeto1<xObjeto2):
			return False
		if(xObjeto1>xObjeto2+tamanhoObjeto2):
			return False
		if(yObjeto1+tamanhoObjeto1<yObjeto2):
			return False
		if(yObjeto1>yObjeto2+tamanhoObjeto2):
			return False
		return True



#objeto para controlar os inimigos, aqui iniciamos um paradigma de POO
class Inimigo(object):
	def __init__(self,DISPLAYSURF):
		self.DISPLAYSURF=DISPLAYSURF
		self.x=random.randint(1, 450);
		self.y=random.randint(1, 450);
		self.posicao="DIREITA";
		self.bala=list()
		self.cont=1

	def controleDeMovimento(self):
		self.cont+=1
		if(self.cont>=1000):
			self.cont=1


		if(self.x>=450):
			self.x-=1
			self.posicao="CIMA";
		if(self.x<=10):
			self.x+=1
			self.posicao="BAIXO";
		if(self.y>=450):
			self.y-=1
			self.posicao="DIREITA";
		if(self.y<10):
			self.y+=1
			self.posicao="ESQUERDA";
		
		
		

		if(float(random.randint(1, 1000)) % 100 ==0):
			self.posicao="CIMA";
			self.bala.append(Tiro(self.x,self.y,self.posicao))
		if(float(random.randint(1, 1000)) % 200 ==0):
			self.posicao="BAIXO";
			self.bala.append(Tiro(self.x,self.y,self.posicao))
		if(float(random.randint(1, 1000)) % 300 ==0):
			self.posicao="DIREITA";
			self.bala.append(Tiro(self.x,self.y,self.posicao))
		if(float(random.randint(1, 1000)) % 400 ==0):
			self.posicao="ESQUERDA";
			self.bala.append(Tiro(self.x,self.y,self.posicao))


		if(self.cont % 20 ==0):
			self.bala.append(Tiro(self.x,self.y,self.posicao))


		for i in range(len(self.bala)):
			self.bala[i].atira()
			self.bala[i].drawBala(self.DISPLAYSURF)
			if(self.bala[i].x > 550 or self.bala[i].x < -50):
				del self.bala[i]
				break
			if(self.bala[i].y > 550 or self.bala[i].y < -50):
				del self.bala[i]
				break




		if(self.posicao=="DIREITA"):
			self.x+=3
		if(self.posicao=="ESQUERDA"):
			self.x-=3
		if(self.posicao=="CIMA"):
			self.y-=3
		if(self.posicao=="BAIXO"):
			self.y+=3


	def draw(self,tamanho):
		pygame.draw.rect(self.DISPLAYSURF,  (255, 0, 0), (self.x, self.y, tamanho, tamanho))
		if(self.posicao=="BAIXO"):
			pygame.draw.rect(self.DISPLAYSURF,  (255, 0, 0), (self.x+(tamanho/3), self.y+tamanho, tamanho/3, tamanho/3))
		elif(self.posicao=="CIMA"):
			pygame.draw.rect(self.DISPLAYSURF,  (255, 0, 0), (self.x+(tamanho/3), self.y-(tamanho/3), tamanho/3, tamanho/3))
		elif(self.posicao=="DIREITA"):
			pygame.draw.rect(self.DISPLAYSURF,  (255, 0, 0), (self.x+tamanho, self.y+(tamanho/3), tamanho/3, tamanho/3))
		elif(self.posicao=="ESQUERDA"):
			pygame.draw.rect(self.DISPLAYSURF,  (255, 0, 0), (self.x-(tamanho/3), self.y+(tamanho/3), tamanho/3, tamanho/3))




#objeto para controlar as balas, aqui iniciamos um paradigma de POO
class Tiro(object):
	#construtor do objeto com 3 parametros proposital e um padrão 'self'(padrão da linguagem em cada metodo criado)
	def __init__(self,x,y,posicao):
		#atribuição de variaveis passadas como parametro no construtor para variaveis(atributo) do objeto
		self.x=x
		self.y=y
		self.posicao=posicao

	#metodo que controla a velocidade e direção das balas ao da um tiro
	def atira(self):
		if(self.posicao=="BAIXO"):
			self.y+=5
		elif(self.posicao=="CIMA"):
			self.y-=5
		elif(self.posicao=="DIREITA"):
			self.x+=5
		elif(self.posicao=="ESQUERDA"):	
			self.x-=5



	#metodo que imprime de forma grafica na tela uma bala, seguindo uma regra 
	#condicionada para que der a impressão da bala esta saindo do cano do tank. 
	#O valor 12 significa a metade do tamanho total do tank menos(-) mais ou menos a metade da bala,
	#sabendo que a metade do tank é: 15 e mais ou menos a metade da bala é 3, logo  15 - 3 = 12.
	#O valor 30 é referente ao tamanho total do tank, poderia ser somado ao tamanho do cano
	#do tank para deixar mais exato, porem o tanho é tão pequeno que a velocidade da saida da
	#bala compensa a diferença fazendo com que não seja necessario fazer a somatoria dos tamanhos.
	#O numero 5 é simplesmente a largura e a altura que a bala vai assumir ao ser instanciada.
	
	def drawBala(self,DISPLAYSURF):
		if(self.posicao=="BAIXO"):
			pygame.draw.rect(DISPLAYSURF,  (255, 0, 0), (self.x+12, self.y+30, 5, 5))
		elif(self.posicao=="CIMA"):
			pygame.draw.rect(DISPLAYSURF,  (255, 0, 0), (self.x+12, self.y, 5, 5))
		elif(self.posicao=="DIREITA"):
			pygame.draw.rect(DISPLAYSURF,  (255, 0, 0), (self.x+30, self.y+12, 5, 5))
		elif(self.posicao=="ESQUERDA"):	
			pygame.draw.rect(DISPLAYSURF,  (255, 0, 0), (self.x, self.y+12, 5, 5))



#fim objetos----------------------------------------------------------------------------


#variaveis globais---------------------------------------
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
#variaveis globais---------------------------------------




def zera():
	global bala,x,y,keyPressed,orientacao,orientacaoTiro,jogo,listaInimigo,inimigosQTD,matouInimigo,colisao,piscaLetra
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
	jogo="gameover"
	listaInimigo=list()
	listaInimigo.append(Inimigo(DISPLAYSURF))
	inimigosQTD=1
	matouInimigo=False
	colisao=Colisao()
	piscaLetra=float(0)


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
		#instancia o objeto tiro
		bala.append(Tiro(x,y,orientacao))
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
	
	if(keyPressed==True and orientacao=="DIREITA" and orientacaoTiro=="NOT"):
		x+=4
	if(keyPressed==True and orientacao=="ESQUERDA" and orientacaoTiro=="NOT"):
		x-=4
	if(keyPressed==True and orientacao=="CIMA" and orientacaoTiro=="NOT"):
		y-=4
	if(keyPressed==True and orientacao=="BAIXO" and orientacaoTiro=="NOT"):
		y+=4


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


def controleDeInimigo():
	global colisao,bala,listaInimigo,inimigosQTD,matouInimigo
	for i in range(len(listaInimigo)):
		listaInimigo[i].draw(30);
		listaInimigo[i].controleDeMovimento();


def controleDeColisao():
	global colisao,bala,listaInimigo,inimigosQTD,matouInimigo,jogo,x,y

	#minha bala no Inimigo
	for i in range(len(listaInimigo)):
		for j in range(len(bala)):
			if(colisao.colisorQuadrado([5,bala[j].x,bala[j].y],[30,listaInimigo[i].x,listaInimigo[i].y])==True):
				del bala[j]
				matouInimigo=True
				break
		if(matouInimigo==True):
			del listaInimigo[i]
			if(inimigosQTD>5):
				matouInimigo=False
			break

	if(matouInimigo==True and inimigosQTD<=5):
		inimigosQTD+=1
		for aux in range(3):
			listaInimigo.append(Inimigo(DISPLAYSURF))
		matouInimigo=False

	#bala do inimigo em mim
	for k in range(len(listaInimigo)):
		for l in range(len(listaInimigo[k].bala)):

			if(colisao.colisorQuadrado([5,listaInimigo[k].bala[l].x,listaInimigo[k].bala[l].y],[30,x,y])==True):
				jogo="gameover"
				zera()
				break
		if(jogo=="gameover"):
			zera()
			break
	#inimigo em mim
	for m in range(len(listaInimigo)):
		if(colisao.colisorQuadrado([30,listaInimigo[m].x,listaInimigo[m].y],[30,x,y])==True):
				jogo="gameover"
				zera()
				break
		if(jogo=="gameover"):
			zera()
			break




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
	global jogo
	img = pygame.display.set_mode((500, 500))
	#importar imagem
	image = pygame.image.load("url.png")
	img.blit(image, (110, 150))
	palavraPiscando("PRESSIONE QUALQUER TECLA PARA VOLTAR!");

	for event in pygame.event.get():	
		if event.type == QUIT:
			finaliza()
		if(event.type==KEYDOWN):
			jogo="begin"


def palavraPiscando(texto):
	global piscaLetra
	piscaLetra+=1
	minhaFont = pygame.font.SysFont("monospace", 20)
	label = minhaFont.render(texto, 1, (255,255,0))
	if(piscaLetra%5<=3):
		DISPLAYSURF.blit(label, (30, 450))

def paginaInicial():
	global jogo,pygame,DISPLAYSURF,piscaLetra
	img = pygame.display.set_mode((500, 500))
	#importar imagem
	image = pygame.image.load("fundoInicial.png")
	img.blit(image, (0, 0))

	palavraPiscando("PRESSIONE QUALQUER TECLA PARA INICIAR!");

	for event in pygame.event.get():	
		if event.type == QUIT:
			finaliza()
		if(event.type==KEYDOWN):
			jogo="play"


def menuTela():
	global jogo
	if(jogo=="play"):
		telaJogoPrincipal()
	elif(jogo=="gameover"):
		telaGameOver()
	elif(jogo=="begin"):
		paginaInicial()


#jogo="gameover"
while True:
	#limpa Tela
	DISPLAYSURF.fill((0, 0, 0))

	menuTela();

	pygame.display.update()
	fpsClock.tick(30)