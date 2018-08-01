import pygame
import enemyparent

class Chaser(EnemyParent):
	def __init__(self,x,y):
		super().__init__(self,x,y)
		self.image.fill((255,255,0))
		self.hp = 1
		power = 4
		self.vulnerable = 1
		self.alarm = 0
		fireRate = 1
		self.id = 4
		self.direct = -1
		
	def update(self):
		self.alarm += 1
