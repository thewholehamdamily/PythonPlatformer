import pygame
import player
import bullet
import level

HEIGHT = 600
WIDTH = 800

pygame.init()
	
size = [WIDTH,HEIGHT]
screen = pygame.display.set_mode(size)
	
pygame.display.set_caption("PythonPlatformer")
plr = player.Player()
	
levels = []
levels.append(level.Level1(player))
	
currentLN = 0
currentL = levels[currentLN]
	
active_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
plr.level = currentL
	
plr.rect.x = 340
plr.rect.y = HEIGHT - plr.rect.height
active_sprites.add(plr)
	
close = False
	
clock = pygame.time.Clock()

def ShiftCamera(shift):
		for a in active_sprites:
			if a != plr:
				a.rect.x += shift
	
while not close:
	#Movement
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			close = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				plr.left()
			if event.key == pygame.K_RIGHT:
				plr.right()
			if event.key == pygame.K_UP or event.key == pygame.K_x:
				plr.jump()
			if event.key == pygame.K_z and len(bullets.sprites()) < 3:
				b = bullet.Bullet(plr.direct,plr.rect.x+20,plr.rect.y+30)
				active_sprites.add(b)
				bullets.add(b)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT and plr.change_x < 0:
				plr.stop()
			if event.key == pygame.K_RIGHT and plr.change_x > 0:
				plr.stop()

	#Bullets colliding w/ enemies
	for b in bullets:
		for e in enemies:
			if b.rect.colliderect(e.rect):
				e.hurt();
				b.kill();


	active_sprites.update()
	currentL.update()
	if plr.rect.right >= 500:
		diff = plr.rect.right - 500
		plr.rect.right = 500
		ShiftCamera(-diff)
		currentL.ShiftCamera(-diff)
	if plr.rect.left <= 120:
		diff = 120 - plr.rect.left
		plr.rect.left = 120
		ShiftCamera(diff)
		currentL.ShiftCamera(diff)
	
	current_pos = plr.rect.x + currentL.cam_shift
	if current_pos < currentL.limit:
		plr.rect.x = 120
		if currentLN < len(levels) - 1:
			currentLN += 1
			currentL = levels[currentLN]
			plr.level = currentL
			
	currentL.draw(screen)
	active_sprites.draw(screen)
		
	clock.tick(60)
		
	pygame.display.flip()
pygame.quit()
