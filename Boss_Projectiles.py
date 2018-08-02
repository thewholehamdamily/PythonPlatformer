import pygame 
from settings import *
from math import sin, cos, pi

RED = (255, 0, 0) 

class Boss_Projectiles(pygame.sprite.Sprite): 
	
	def __init__(self, d, x, y): 

		super().__init__()
		width = 20			        #Made the Width and Height larger for the boss
		height = 20
		self.image.Surface[width,height]) 
		self.image.fill(RED) 
		self.rect = self.image.get_rect() 
		self. = d
		self.rect.x = x
		self.rect.y = y

	def update(self): 
		
		self.rect.y += sin(self.direct) * 3 
		self.rect.y += cos(self.direct) * 3 

		if self.rect.x < -16 or self.rect.x > 800 or self.rect.y < 0 or self.rect.y > 600:
		
			self.kill()

