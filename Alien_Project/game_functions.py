import sys
import pygame
from bullet import Bullet


def check_events(ship,screen,ai_settings,bullets):
	# 响应键盘和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			pass
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship,ai_settings,screen,bullets)
			pass
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			pass	
		pass      

	pass


# 键盘事件监听
def check_keydown_events(event,ship,ai_setting,screen,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
		ship.moving_left  = False
		pass
	elif event.key == pygame.K_LEFT:
		ship.moving_right = False
		ship.moving_left  = True
		pass
	elif event.key == pygame.K_SPACE:
		fire_bullets(ai_setting,screen,ship,bullets)
	pass

def check_keyup_events(event,ship):
	ship.moving_right = False
	ship.moving_left  = False
	pass

def update_screen(ai_settings,screen,ship,bullets):
	#更新屏幕上的图片，并切换到新的屏幕
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	#绘制子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	pygame.display.flip()

def fire_bullets(ai_settings,screen,ship,bullets):

	if len(bullets)<ai_settings.bullets_allowed:
		print("space")
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
	pass


def update_bullets(bullets):
	# 删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			pass
		pass
		print(len(bullets))
	pass

