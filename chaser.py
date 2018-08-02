import pygame
import enemyparent

class Chaser(enemyparent.EnemyParent):
	def __init__(self,x,y):
		super().__init__(x,y)
		self.image.fill((255,255,0))
		self.hp = 1
		self.power = 4
		self.vulnerable = 1
		self.alarm = 0
		self.fireRate = 1
		self.id = 4
		self.direct = -1
		
	def update(self):
		self.alarm += 1
		if self.rect.x < 32 or self.rect.x > 640:
			self.kill()
