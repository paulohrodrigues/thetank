# coding: utf8
import pygame, sys
from pygame.locals import *
import random
from tiro import Tiro
class Inimigo(object):
	def __init__(self,DISPLAYSURF):
		self.DISPLAYSURF=DISPLAYSURF
		self.x=random.randint(1, 450);
		self.y=1
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
			self.bala.append(Tiro(self.x,self.y,self.posicao,(255,0,0)))
		if(float(random.randint(1, 1000)) % 200 ==0):
			self.posicao="BAIXO";
			self.bala.append(Tiro(self.x,self.y,self.posicao,(255,0,0)))
		if(float(random.randint(1, 1000)) % 300 ==0):
			self.posicao="DIREITA";
			self.bala.append(Tiro(self.x,self.y,self.posicao,(255,0,0)))
		if(float(random.randint(1, 1000)) % 400 ==0):
			self.posicao="ESQUERDA";
			self.bala.append(Tiro(self.x,self.y,self.posicao,(255,0,0)))


		if(self.cont % 20 ==0):
			self.bala.append(Tiro(self.x,self.y,self.posicao,(255,0,0)))


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