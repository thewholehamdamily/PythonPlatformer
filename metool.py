import pygame
import enemyparent

class Metool(EnemyParent):
	def __init__(self,d,x,y):
		super().__init__(x,y)
		self.image.fill((255,255,0))
		self.hp = 1
		power = 4
		self.vulnerable = 0
		self.alarm = 0
		fireRate = 300
		self.id = 1
		self.direct = -1
	
	def update(self):
		self.alarm += 1
	
	def attack(self):
		if vulnerable = 0:
			vulnerable = 1
			self.image.fill((255,255,255))
		else
			vulnerable = 0
			self.image.fill((255,255,0))
			
