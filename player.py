import pygame
HEIGHT = 480
WIDTH = 640
RED = (255,0,0)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		width = 32
		height = 64
		self.health = 3
		self.image = pygame.Surface([width,height])
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.fall_speed_cap = 10
		self.change_x = 0
		self.change_y = 0
		self.direct = 1
		self.level = None
		self.jumped = False
	def update(self):
		self.get_gravity()
		self.rect.x += self.change_x

		block_hit_list = pygame.sprite.spritecollide(self,self.level.plats,False)
		for block in block_hit_list:
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				self.rect.left = block.rect.right
		self.rect.y += self.change_y
		block_hit_list = pygame.sprite.spritecollide(self,self.level.plats,False)
		for block in block_hit_list:
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom
			self.change_y = 0
			'''if isinstance(block, MovingPlatform):
				self.rect.x += block.move_x'''
		if self.rect.x <= 0:
			self.rect.x = 0

	def get_gravity(self):
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .35
		if self.rect.y >= HEIGHT - self.rect.height and self.change_y >= 0:
			self.jumped = False
			self.change_y = 0
			self.rect.y = HEIGHT - self.rect.height
		elif self.jumped:
			key = pygame.key.get_pressed() 
			if key[pygame.K_UP] == False and key[pygame.K_x] == False:
				if self.change_y == self.fall_speed_cap:
					self.change_y += 0
				elif (self.change_y + .65) > self.fall_speed_cap:
					self.change_y += (self.fall_speed_cap - self.change_y)
				else:
					self.change_y += .65

	def jump(self):
		self.jumped = True
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self,self.level.plats,False)
		self.rect.y -= 2
		if len(platform_hit_list) > 0 or self.rect.bottom >= HEIGHT:
			self.change_y = -10

	def left(self):
		self.change_x = -4
		self.direct = -1
	def right(self):
		self.change_x = 4
		self.direct = 1
	def stop(self):
		self.change_x = 0
