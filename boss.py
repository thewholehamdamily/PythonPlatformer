import pygame as pg 


SPRITESHEET = "spritesheet_jumper.png"

class Loader: 									 	# Loads the image to the program
	
	def __init__(self):

		pg.init()
		self.Load_The_Data()
	
	def Load_The_Data(self): 

		img_folder = path.join(self.dir, 'img')

		self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))

class Boss_Sprite_Sheet:
	
	def __init__(self, filename):
	
		self.spritesheet = pg.image.load(filename).convert()

	def get_image(self, x, y, width, height):

		image = pygame.Surface((width, height)) 
		image.blit(self.spritesheet, (0,0), (x, y, width, height)) 
		image = pg.transform.scale(image, (width // 2, height // 2)) 
		
		return image;

class Boss(pg.sprite.Sprite):

	def __init__(self):
		pg.sprite.Sprite.__init__(self, self.groups)  
											 # Creating the image for boss
		self.image_up = self.game.spritesheet.get_image(566, 510, 122, 139)
		self.image_up.set_colorkey(BLACK)
		self.image_down = self.game.spritesheet.get_image(568, 1534, 122, 135)
		self.image_down.set_colorkey(BLACK)
		self.hp = 30
		self.power = 8

		self.image = self.image_up
		self.rect.centerx = choice([-100, WIDTH + 100]) 			# Where the boss will appear
		self.vx = randrange(1,4)						# A random speed 

		if self.rect.centerx > WIDTH:						#If spawned from the the left, goes to the right 
			self.vx += -1

		self.rect.u = randrange(HEIGHT / 2) 					# spawn in the top half of the screen above the player
		self.vy = 0
		self.dy = 1

	def update(self):

		self.rect.x += self.vx
		self.vy += self.dy 

		if self.vy > 3 or self.vy < -3:						# Makes the enemy hover 
		
			self.dy += -1 

		center = self.rect.center
		if self.dy < 0: 											# For movement 

			self.image = self.image_up 

		else:

			self.image = self.image_down
			self.rect = self.image.get_rect()
			self.rect.center = center 
			self.rect.y += self.vy
	

	def hurt(self):
	
		self.hp -= 1
		if self.hp <= 0:

			self.kill()  



		



		

