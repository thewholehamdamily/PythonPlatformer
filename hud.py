import pygame
import player
class HUD():
	def __init__(self,f,size,p,screen):
		self.screen = screen
		self.plr = p
		self.health_font = pygame.font.SysFont(f,size)
	def update(self):
		hud = self.health_font.render("HEALTH: " + str(self.plr.health),1,(255,255,0))
		self.screen.blit(hud,(100,100))