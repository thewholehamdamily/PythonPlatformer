import pygame
import enemyparent

class Metool(enemyparent.EnemyParent):
	def __init__(self,x,y):
		super().__init__(x,y)
		self.image.fill((255,255,0))
		self.hp = 1
		self.power = 4
		self.vulnerable = 0
		self.alarm = 0
		self.fireRate = 180
		self.id = 1
		self.direct = -1
		
	def update(self):
		self.alarm += 1
	
	def attack(self):
		if self.vulnerable == 0:
			self.vulnerable = 1
			self.image.fill((255,255,255))
		else:
			self.vulnerable = 0
			self.image.fill((255,255,0))
			
