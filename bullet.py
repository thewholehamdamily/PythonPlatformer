import pygame

BULLET_COLOR = (255,255,255)	#WHITE

class Bullet(pygame.sprite.Sprite):
	def __init__(self,d,x,y):
		super().__init__()
		width = 16
		height = 16
		self.image = pygame.Surface([width,height])
		self.image.fill(BULLET_COLOR)
		self.rect = self.image.get_rect()
		self.direct = d
		self.change_x = 8*d
		self.rect.x = x
		self.rect.y = y

	def update(self):
		#Move the bullet
		self.rect.x += self.change_x
		#If the bullet goes offscreen, destroy it
		if self.rect.x < -16 or self.rect.x > 640:
			self.kill()
