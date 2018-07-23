import pygame
import player

HEIGHT = 600
WIDTH = 800

def main():
	pygame.init()
	
	size = [WIDTH,HEIGHT]
	screen = pygame.display.set_mode(size)
	
	pygame.display.set_caption("PythonPlatformer")
	plr = player.Player()
	
	levels = []
	levels.append(Level1(player))
	
	currentLN = 0
	currentL = levels[currentLN]
	
	active_sprites = pygame.sprite.Group()
	plr.level = currentL
	
	plr.rect.x = 340
	plr.rect.y = HEIGHT - player.rect.height
	active_sprites.add(plr)
	
	close = False
	
	clock = pygame.time.Clock()
	
	while not close:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				close = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					plr.go_left()
				if event.key == pygame.K_RIGHT:
					plr.go_right()
				if event.key ==pygame.K_UP:
					player.jump()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					player.stop()
				if event.key == pygame.K_RIGHT
					player.stop()

		active_sprites.update()
		currentL.update()
		if plr.rect.right >= 500:
			diff = player.rect.right - 500
			plr.rect.right = 500
			currentL.shift_world(-diff)
		if player.rect.left <= 120:
			diff = 120 - plr.rect.left
			player.rect.left = 120
			currentL.shift_world(diff)
		
		current_pos = plr.rect.x + currentL.world_shift
		if current_pos < currentL.level_limit:
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
	
if __name__ == "__main__":
	main()