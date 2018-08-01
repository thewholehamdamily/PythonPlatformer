import pygame
import player
import bullet
import level
import hud

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
enemyBullets = pygame.sprite.Group()
plr.level = currentL
	
plr.rect.x = 340
plr.rect.y = HEIGHT - plr.rect.height
active_sprites.add(plr)
	
close = False
	
clock = pygame.time.Clock()

camPos = 0
HUD = hud.HUD("monospace",15,plr,screen)

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
				if e.vulnerable == 1:
					e.hurt();
				b.kill();

	#Enemies attacking
	for e in enemies:
		if e.alarm > e.fireRate:
			e.attack()
			#Metool bullets
			if e.id == 1 and e.vulnerable == 0:
				b = bullet.Bullet(315,e.rect.x,e.rect.y+16)
				active_sprites.add(b)
				bullets.add(b)
				b = bullet.Bullet(270,e.rect.x,e.rect.y+16)
				active_sprites.add(b)
				bullets.add(b)
				b = bullet.Bullet(225,e.rect.x,e.rect.y+16)
				active_sprites.add(b)
				bullets.add(b)
			#Chaser spawning
			if e.id == 3:
				c = chaser.Chaser(e.rect.x,e.rect.y)
				active_sprites.add(c)
				enemies.add(c)
			#Chaser chasing
			if e.id == 4:
				if e.rect.x > plr.rect.x:
					e.rect.x -= 2
				if e.rect.x < plr.rect.x:
					e.rect.x += 2
				if e.rect.y > plr.rect.y:
					e.rect.y -= 2
				if e.rect.y < plr.rect.y:
					e.rect.y += 2
			#Big Eye jump direction
			if e.id == 5:
				if plr.rect.x > e.rect.x:
					e.direct = 1
				else
					e.direct = -1
				e.change_x = 6*e.direct
			e.alarm = 0
		#Big Eye Jump Collision
		if e.id == 5:
			block_hit_list = pygame.sprite.spritecollide(e,plr.level.plats,False)
			for block in block_hit_list:
				if e.change_y > 0:
					e.rect.bottom = block.rect.top
					e.jumping = 0
				elif e.change_y < 0:
					e.rect.top = block.rect.top
				e.change_y = 0
				if e.change_x > 0:
					e.rect.right = block.rect.left
				elif e.change_x < 0:
					e.rect.left = block.rect.right
			if e.rect.bottom > HEIGHT:
				e.rect.bottom = HEIGHT:
				e.jumping = 0


	active_sprites.update()
	currentL.update()
	if plr.rect.right >= 416:
		diff = plr.rect.right - 416
		plr.rect.right = 416
		ShiftCamera(-diff)
		currentL.ShiftCamera(-diff)
		camPos += diff
	if plr.rect.left <= 384 and camPos > 0:
		diff = 384 - plr.rect.left
		plr.rect.left = 384
		ShiftCamera(diff)
		currentL.ShiftCamera(diff)
		camPos -= diff
	
	current_pos = plr.rect.x + currentL.cam_shift
	if current_pos < currentL.limit:
		plr.rect.x = 120
		if currentLN < len(levels) - 1:
			currentLN += 1
			currentL = levels[currentLN]
			plr.level = currentL
			
	currentL.draw(screen)
	active_sprites.draw(screen)
	HUD.update()
	clock.tick(60)
		
	pygame.display.flip()
pygame.quit()
