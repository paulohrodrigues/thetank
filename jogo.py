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





while True:

	pygame.display.update()
	fpsClock.tick(30)