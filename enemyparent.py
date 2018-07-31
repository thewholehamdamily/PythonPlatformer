import pygame

class EnemyParent(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		width = 32
		height = 32
		self.hp = 1
		self.power = 4
		self.image = pygame.Surface([width,height])
		self.image.fill((0,255,0))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.vulnerable = 1
		self.id = 0
	def hurt(self):
		self.hp -= 1
		if self.hp <= 0:
			self.kill()
	def attack(self):
		pass
