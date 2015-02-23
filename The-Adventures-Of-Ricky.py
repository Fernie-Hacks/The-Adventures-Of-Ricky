#! /usr/bin/env python

import random, os.path

#Game Developed during SB Hacks 
#Fernando Gonzalez
#Ricardo Morones

#Import over to Python interpreter
import pygame
from pygame.locals import *

#see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

#Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255,0)
RED = (255, 0, 0)

#Game Variables
SCREENRECT     = Rect(0, 0, 800, 600)
size = (800, 600)

#Game Logistics
screen = pygame.display.set_mode(size)
pygame.display.set_caption("The Adventures of Third Leg Ricky")
backgroundImage = pygame.image.load("ThirdLeg.jpg").convert()
screen.blit(backgroundImage, [0, 0])
playerImage = pygame.image.load("soccerRicky.png").convert()
screen.blit(playerImage, [0, 410])
pygame.display.flip()

clock=pygame.time.Clock()
pygame.init()
running = 1

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = 0
	#Limit to 60 frames per second
	clock.tick(60)

pygame.time.wait(1000)
pygame.quit()