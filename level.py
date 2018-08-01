'''Module levels.py
includes classes Platform, Level, and Level1'''
import pygame
import player

BACKGROUND_COLOR = (3,3,3) #black
PLATFORM_COLOR = (191,62,255) #purple
MPLATFORM_COLOR = (127,255,0) #green

class Platform(pygame.sprite.Sprite):
	def __init__(self,width,height,color = PLATFORM_COLOR):
		super().__init__()
		self.image = pygame.Surface([width,height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

'''class MovingPlat(Platform):
	move_x = 0
	move_y = 0
	top_bound = 0
	bottom_bound = 0
	left_bound = 0
	right_bound = 0
	plr = None
	level = None
	def __init__(self,p,w,h,c):
		super().__init__(w,h,c)
		self.plr = p
	def update(self):
		self.rect.x += self.move_x
		hit = pygame.sprite.collide_rect(self,self.plr)
		if hit:
			if self.move_x < 0:
				self.plr.rect.right = self.rect.left
			else:
				self.plr.rect.left = self.rect.right
		self.rect.y += self.move_y
		hit = pygame.sprite.collide_rect(self,self.plr)
		if hit:
			if self.move_y < 0:
				self.plr.rect.bottom = self.rect.top
			else:
				self.plr.rect.top = self.rect.bottom
		if self.rect.bottom > self.bottom_bound or self.rect.top < self.top_bound:
			self.move_y *= -1
		current = self.rect.x - self.level.cam_shift
		if self.rect.bottom > self.left_bound or cur_pos > self.right_bound:
			self.move_x *= -1
'''			
class Level():
	def __init__(self,player):
		self.plats = pygame.sprite.Group()
		self.player = player
		self.cam_shift  = 0
	def update(self):
		self.plats.update()
	def draw(self,screen):
		screen.fill(BACKGROUND_COLOR)
		self.plats.draw(screen)
	def ShiftCamera(self,shift):
		self.cam_shift += shift
		for platform in self.plats:
			platform.rect.x += shift
			
class Level1(Level):
	def __init__(self,player):
		Level.__init__(self,player)
		self.limit = -1000
		
		level = [[210,70,500,500],
				 [210,70,800,400],
				 [210,70,1000,500],
				 [210,70,1120,280]]
		
		
		for platform in level:
			plat = Platform(platform[0],platform[1])
			plat.rect.x = platform[2]
			plat.rect.y = platform[3]
			plat.player = self.player
			self.plats.add(plat)
	'''	mplat = MovingPlat(self.player,70,40,MPLATFORM_COLOR)
		mplat.rect.x = 1350
		mplat.rect.y = 280
		mplat.left_bound = 1350
		mplat.right_bound = 1600
		mplat.move_x = 1
		mplat.level = self
		self.plats.add(mplat)'''
