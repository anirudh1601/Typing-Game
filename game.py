import pygame
import sys
import random
from pygame.locals import *
import tkinter
from tkinter import messagebox

pygame.init()
background=(200,200,255)
blue=(30,30,255)
green=(30,120,30)
X=600
Y=400
speed=0.03
points=0

def new_word():
	global choosenword,pressedword,word_x,word_y,point,speed,text
	word_x=random.randint(100,200)
	word_y=0
	word=open ("words.txt").read().splitlines()
	choosenword=random.choice(word)
	text=font.render(choosenword,True,blue)
	speed+=0.0003
	pressedword=""



win=pygame.display.set_mode((X,Y))
pygame.display.set_caption("TYPING GAME")

PLAY=True
font=pygame.font.SysFont("Comicsans",32)
font_point=pygame.font.SysFont("Comicsans",32)
new_word()

while PLAY:
	win.fill(background)
	word_y += speed
	win.blit(text,(word_x,word_y))
	

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			PLAY=False
		elif event.type==pygame.KEYDOWN:
			pressedword+=pygame.key.name(event.key)
			if choosenword.startswith(pressedword):
				if choosenword==pressedword and word_y<=360:
					new_word()
					points+=1
					speed+=0.03

				elif (choosenword==pressedword or choosenword!= pressedword or choosenword not in pressedword) and word_y>=360:
					messagebox.showwarning("game over","your game is over and your point is " + str(points))
					pygame.quit()


				

			else:
				pressedword= ""

			

	pointCaption=font.render(str(points),True,green)
	win.blit(pointCaption,(10,5))

			

	pygame.display.update()

pygame.quit()