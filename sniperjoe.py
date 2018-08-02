import pygame
import enemyparent

class SniperJoe(enemyparent.EnemyParent):
	def __init__(self,x,y):
		width = 32
		height = 64
		super().__init__(x,y)
		self.hp = 3
		self.fireRate = 120
		self.power = 4
		self.vulnerable = 0
		self.alarm = 0
		self.state = 0
		self.jumping = 0
		self.id = 6
		
	def update(self):
		if self.jumping == 0:
			self.alarm += 1
			self.rect.x += 0
			self.rect.y += 0
		else:
			self.change_y += .35
			self.rect.x += self.change_x
			self.rect.y += self.change_y

	def attack(self):
		if self.state == 0 and self.vulnerable == 0:
			self.vulnerable = 1
		elif self.state == 1:
			jump()
		else:
			vulnerable = 0

	def jump(self):
		self.change_y = -10
		self.vulnerable = 1
		self.jumping = 1		
