import pygame

class ChaserSpawner(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		width = 32
		height = 32
		self.image = pygame.Surface([width,height])
		pygame.draw.rect(self.image,(255,255,255),(x,y,width,height),3)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.fireRate = 300
		self.alarm = 0
		self.id = 3
		self.vulnerable = 2

	def update(self):
		self.alarm += 1
	def attack(self):
		pass
		

	
		
