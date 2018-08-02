import pygame
from math import sin, cos, pi

BULLET_COLOR = (255,255,255)	#WHITE

class EnemyBullet(pygame.sprite.Sprite):
	def __init__(self,d,x,y):
		super().__init__()
		width = 16
		height = 16
		self.image = pygame.Surface([width,height])
		self.image.fill(BULLET_COLOR)
		self.rect = self.image.get_rect()
		self.direct = d
		self.rect.x = x
		self.rect.y = y

	def update(self):
		#Move the bullet
		self.rect.x += sin(self.direct) * 3
		self.rect.y += cos(self.direct) * 3
		#If the bullet goes offscreen, destroy it
		if self.rect.x < -16 or self.rect.x > 640 or self.rect.y < 0 or self.rect.y > 480:
			self.kill()
