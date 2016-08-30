# coding: utf8
import pygame, sys
from pygame.locals import *
class Tiro(object):
	#construtor do objeto com 3 parametros proposital e um padrão 'self'(padrão da linguagem em cada metodo criado)
	def __init__(self,x,y,posicao,cor):
		#atribuição de variaveis passadas como parametro no construtor para variaveis(atributo) do objeto
		self.x=x
		self.y=y
		self.posicao=posicao
		self.cor=cor
		
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
			pygame.draw.rect(DISPLAYSURF,  self.cor, (self.x+12, self.y+30, 5, 5))
		elif(self.posicao=="CIMA"):
			pygame.draw.rect(DISPLAYSURF,  self.cor, (self.x+12, self.y, 5, 5))
		elif(self.posicao=="DIREITA"):
			pygame.draw.rect(DISPLAYSURF,  self.cor, (self.x+30, self.y+12, 5, 5))
		elif(self.posicao=="ESQUERDA"):	
			pygame.draw.rect(DISPLAYSURF,  self.cor, (self.x, self.y+12, 5, 5))