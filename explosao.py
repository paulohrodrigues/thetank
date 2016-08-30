# coding: utf8
import pygame, sys
from pygame.locals import *
import random
class Explosao(object):
	def __init__(self,x,y,cor,DISPLAYSURF):
		self.DISPLAYSURF=DISPLAYSURF
		self.cor  =(random.randint(25,255),random.randint(25,255),random.randint(25,255))
		self.x 	  =x
		self.y    =y
		self.listaExplosao=list()
		for i in range(20):
			self.listaExplosao.append([random.randint(-4,4),random.randint(-4,4),self.x,self.y])
	def explode(self):
		for i in range(20):
			self.listaExplosao[i][2]+=self.listaExplosao[i][0]
			self.listaExplosao[i][3]+=self.listaExplosao[i][1]
			pygame.draw.rect(self.DISPLAYSURF,self.cor,(self.listaExplosao[i][2],self.listaExplosao[i][3],8,8))