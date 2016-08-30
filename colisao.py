# coding: utf8
import pygame, sys
from pygame.locals import *
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