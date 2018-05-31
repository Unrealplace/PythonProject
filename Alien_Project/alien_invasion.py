import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():

	pygame.init()
	# 设置类
	alien_setting = Settings()
    # 屏幕对象
	screen = pygame.display.set_mode(
		(alien_setting.screen_width,alien_setting.screen_height))
	pygame.display.set_caption("Alien Invasion")
	# 创建一个飞船
	ship = Ship(screen,alien_setting)

    # 创建一个子弹编组
	bullets = Group()

	while True:
		# 检测事件
		gf.check_events(ship,screen,alien_setting,bullets)
        # 检测完成位置后更新坐标
		ship.update()
		bullets.update()
		gf.update_bullets(bullets)
		# 重新绘制屏幕
		gf.update_screen(ai_settings=alien_setting,screen=screen,ship=ship,bullets=bullets)
	pass

run_game()