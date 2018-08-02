'''Module levels.py
includes classes Platform, Level, and Level1'''
import pygame
import player
import metool
import slideblade
import chaserspawner
import bigeye
import sniperjoe

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
		self.enemies = pygame.sprite.Group()
		self.active_sprites = pygame.sprite.Group()
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
		
		s1=["                    ",
			"                    ",
			"                    ",
			"                    ",
			"                    ",
			"                    ",
			"                    ",
			"                    ",
			"                    ",
			"                    ",
			"                    ",
			"                s   ",
			"           ppppppppp",
			"                    ",
			"                    "]
		
		level = [s1]

		#Level generation loop
		for h in range(0,len(level)):
			for i in range(0,15):
				for j in range(0,20):
					#Platforms
					if level[h][i][j] == "p":
						plat = Platform(32,32)
						plat.rect.x = j*32 + h*640
						plat.rect.y = i*32
						plat.player = self.player
						self.plats.add(plat)
					#Metool
					elif level[h][i][j] == "m":
						met = metool.Metool(j*32 + h*640,i*32)
						self.enemies.add(met)
						self.active_sprites.add(met)
					#Up Slide Blade
					elif level[h][i][j] == "^":
						blade = slideblade.SlideBlade(1,0,-1,j*32 + h*640,i*32)
						self.enemies.add(blade)
						self.active_sprites.add(blade)
					#Down Slide Blade
					elif level[h][i][j] == "^":
						blade = slideblade.SlideBlade(1,0,1,j*32 + h*640,i*32)
						self.enemies.add(blade)
						self.active_sprites.add(blade)
					#Left Slide Blade
					elif level[h][i][j] == "<":
						blade = slideblade.SlideBlade(0,1,-1,j*32 + h*640,i*32)
						self.enemies.add(blade)
						self.active_sprites.add(blade)
					#Right Slide Blade
					elif level[h][i][j] == "^":
						blade = slideblade.SlideBlade(0,1,1,j*32 + h*640,i*32)
						self.enemies.add(blade)
						self.active_sprites.add(blade)
					#Left Diagonal Slide Blade
					elif level[h][i][j] == "l":
						blade = slideblade.SlideBlade(1,1,-1,j*32 + h*640,i*32)
						self.enemies.add(blade)
						self.active_sprites.add(blade)
					#Right Diagonal Slide Blade
					elif level[h][i][j] == "r":
						blade = slideblade.SlideBlade(1,1,1,j*32 + h*640,i*32)
						self.enemies.add(blade)
						self.active_sprites.add(blade)
					#Chaser Spawner
					elif level[h][i][j] == "c":
						chase = chaserspawner.ChaserSpawner(j*32 + h*640,i*32)
						self.enemies.add(chase)
						self.active_sprites.add(chase)
					#Big Eye
					elif level[h][i][j] == "b":
						eye = bigeye.BigEye(j*32 + h*640,i*32-32)
						self.enemies.add(eye)
						self.active_sprites.add(eye)
					#Sniper Joe
					elif level[h][i][j] == "s":
						joe = sniperjoe.SniperJoe(j*32 + h*640,i*32-32)
						self.enemies.add(joe)
						self.active_sprites.add(joe)
		'''
		for platform in level:
			plat = Platform(platform[0],platform[1])
			plat.rect.x = platform[2]
			plat.rect.y = platform[3]
			plat.player = self.player
			self.plats.add(plat)
		'''
	'''	mplat = MovingPlat(self.player,70,40,MPLATFORM_COLOR)
		mplat.rect.x = 1350
		mplat.rect.y = 280
		mplat.left_bound = 1350
		mplat.right_bound = 1600
		mplat.move_x = 1
		mplat.level = self
		self.plats.add(mplat)'''
