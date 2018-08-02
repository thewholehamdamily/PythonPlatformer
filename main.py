import pygame
import player
import bullet
import enemybullet
import level
import hud

HEIGHT = 480
WIDTH = 640

pygame.init()
	
size = [WIDTH,HEIGHT]
screen = pygame.display.set_mode(size)
	
pygame.display.set_caption("PythonPlatformer")
plr = player.Player()
	
levels = []
levels.append(level.Level1(player))
	
currentLN = 0
currentL = levels[currentLN]
	
active_sprites = currentL.active_sprites
bullets = pygame.sprite.Group()
enemyBullets = pygame.sprite.Group()
plr.level = currentL
	
plr.rect.x = 200
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
	for e in currentL.enemies:
		if e.alarm > e.fireRate:
			#Metool bullets
			if e.id == 1 and e.vulnerable == 0:
				b = enemybullet.EnemyBullet(45,e.rect.x,e.rect.y+16)
				active_sprites.add(b)
				enemyBullets.add(b)
				b = enemybullet.EnemyBullet(90,e.rect.x,e.rect.y+16)
				active_sprites.add(b)
				enemyBullets.add(b)
				b = enemybullet.EnemyBullet(135,e.rect.x,e.rect.y+16)
				active_sprites.add(b)
				enemyBullets.add(b)
				
			#Chaser spawning
			if e.id == 3:
				c = chaser.Chaser(e.rect.x,e.rect.y)
				active_sprites.add(c)
				currentL.enemies.add(c)
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
			if e.id == 5 and e.rect.x <= WIDTH:
				if plr.rect.x > e.rect.x:
					e.direct = 1
				else:
					e.direct = -1
				e.change_x = 6*e.direct
			#Choose which attack to do for Sniper Joe
			if e.id == 6:
				if plr.rect.y > e.rect.y:
					e.state = 1
				else:
					e.state = 0
					if e.vulnerable == 0:
						b = bullet.Bullet(270,e.rect.x,e.rect.y,y+16)
						active_sprites.add(b)
						enemyBullets.add(b)
			e.attack()
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
				e.rect.bottom = HEIGHT
				e.jumping = 0
		#Sniper Joe jump collision
		if e.id == 6:
			block_hit_list = pygame.sprite.spritecollide(e,plr.level.plats,False)
			for block in block_hit_list:
				if e.change_y > 0:
					e.rect.bottom = block.rect.top
					e.jumping = 0
				if e.rect.bottom > HEIGHT:
					e.rect.bottom = HEIGHT
					e.jumping = 0

	plr.level.active_sprites.update()
	plr.level.update()
	if plr.rect.right >= WIDTH/2 + 16:
		diff = plr.rect.right - (WIDTH/2 + 16)
		plr.rect.right = WIDTH/2 + 16
		ShiftCamera(-diff)
		currentL.ShiftCamera(-diff)
		camPos += diff
	if plr.rect.left <= WIDTH/2 - 16 and camPos > 0:
		diff = (WIDTH/2 - 16) - plr.rect.left
		plr.rect.left = WIDTH/2 - 16
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
