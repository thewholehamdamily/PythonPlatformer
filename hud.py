import pygame
import player

BORDER_COLOR = (255,255,255)	#white
HEALTH_COLOR = (255,215,0)		#gold
class HUD():
	def __init__(self,f,size,p,screen):
		self.screen = screen
		self.plr = p
		#self.health_font = pygame.font.SysFont(f,size)
	def update(self):
		if self.plr.health < 0:
			self.plr.health = 0
		HEALTH_WIDTH = 20
		HEALTH_HEIGHT = 200
		fill = ((HEALTH_HEIGHT/32) * self.plr.health)
		outer_bar = pygame.Rect(50,50,HEALTH_WIDTH,HEALTH_HEIGHT)
		fill_bar = pygame.Rect(50,50,fill,HEALTH_HEIGHT)
		pygame.draw.rect(self.screen,HEALTH_COLOR,fill_bar)
		pygame.draw.rect(self.screen,BORDER_COLOR, outer_bar,2)
		#hud = self.health_font.render("HEALTH: " + str(self.plr.health),1,(255,255,0))
		#self.screen.blit(hud,(100,100))