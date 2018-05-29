import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

	pygame.init()
	# 设置类
	alien_setting = Settings()
    # 屏幕对象
	screen = pygame.display.set_mode(
		(alien_setting.screen_width,alien_setting.screen_height))
	pygame.display.set_caption("Alien Invasion")
	# 创建一个飞船
	ship = Ship(screen)

	while True:
		# 检测事件
		gf.check_events(ship=ship)
		pass
		# 重新绘制屏幕
		gf.update_screen(ai_settings=alien_setting,screen=screen,ship=ship)
	pass

run_game()