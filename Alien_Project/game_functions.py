import sys
import pygame

def check_events(ship):
	# 响应键盘和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			pass
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.rect.centerx+=1
				pass
			elif event.key == pygame.K_LEFT:
				ship.rect.centerx-=1
				pass
			pass
		pass

	pass

def update_screen(ai_settings,screen,ship):
	#更新屏幕上的图片，并切换到新的屏幕
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	pygame.display.flip()
	pass