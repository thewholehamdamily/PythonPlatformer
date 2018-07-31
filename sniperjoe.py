import pygame
import enemyparent

class SniperJoe(pygame.sprite.Sprite):
	def __init__(self,x,y):
		width = 32
		height = 64
		super().__init__(x,y)
		self.hp = 3
		power = 4
		self.vulnerable = 0
		self.alarm = 0
		self.jumping = 0
		self.shooting = 0

	def update(self):
		self.alarm += 1
		if self.alarm >= 120:
			self.attack()

	def attack():
		

	def get_gravity(self):
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .35
		if self.rect.y >= 600 - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = 600 - self.rect.height

	def jump(self):
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self,self.level.plats,False)
		self.rect.y -= 2
		if len(platform_hit_list) > 0 or self.rect.bottom >= 600:
			self.change_y = -10

	def shoot(self):
		

