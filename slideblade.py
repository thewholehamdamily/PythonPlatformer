import pygame
import enemyparent

#Slides back and forth
class SlideBlade(enemyparent.EnemyParent):
	def __init__(self,v,h,d,x,y):
		super().__init__(x,y)
		self.image.fill((0,255,0))
		self.hp = 5
		power = 4
		self.vulnerable = 1
		self.alarm = 0
		fireRate = 120
		self.id = 2
		self.direct = d		#Which direction does it start going?
		self.change_x = 0
		self.change_y = 0
		self.vertical = v	#Does the blade move vertically?
		self.horizontal = h	#Does the blade move horizontally?
		self.moving = 0
	
	def update(self):
		self.rect.x += self.change_x
		self.rect.y += self.change_y
		self.alarm += 1
	
	def attack(self):
		if self.moving == 0:
			self.change_x = self.horizontal * self.direct
			self.change_y = self.horizontal * self.direct
			self.moving = 1
		else
			self.direct *= -1
			self.change_x = 0
			self.change_y = 0
			self.moving = 0
