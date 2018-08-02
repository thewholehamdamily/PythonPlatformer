import pygame
import enemyparent

class BigEye(enemyparent.EnemyParent):
	def __init__(self,x,y):
		height = 64
		width = 64
		super().__init__(x,y)
		self.image = pygame.Surface([width,height])
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		self.hp = 10
		self.power = 8
		self.vulnerable = 1
		self.alarm = 0
		self.fireRate = 60
		self.id = 5
		self.direct = -1
		self.change_x = 0
		self.change_y = 0
		self.jumping = 0
		self.count = 0
		self.rect.x = x
		self.rect.y = y

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
			self.change_y = -7
			self.count += 1
		else:
			self.change_y = -10
			self.count = 0
		self.change_x = 2*self.direct
		self.jumping = 1
