import pygame
import enemyparent

class BigEye(EnemyParent):
	def __init__(self,x,y):
		height = 64
		width = 64
		super().__init__(self,x,y)
		self.image.fill((255,0,0))
		self.hp = 10
		power = 8
		self.vulnerable = 1
		self.alarm = 0
		fireRate = 60
		self.id = 5
		self.direct = -1
		self.change_x = 0
		self.change_y = 0
		self.jumping = 0
		self.count = 0

	def update(self):
		if self.jumping == 0:
			self.alarm += 1
			self.rect.x += 0
			self.rect.y += 0
		else:
			self.change_y += 0.35
			self.rect.x += self.change_x
			self.rect.y += self.change_y

	def attack(self):
		#Every three hops, jump high
		if self.count < 3:
			self.change_y = -10
			self.count += 1
		else:
			self.change_y = -25
			self.count = 0
		self.change_x = 4*direct
		self.jumping = 1
