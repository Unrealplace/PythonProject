import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""子弹操作类	"""
	def __init__(self,ai_setting,screen,ship):
		super(Bullet, self).__init__()

		self.ai_setting = ai_setting
		self.screen = screen
		self.ship   = ship
        
        # 设置子弹的位置
		self.rect   = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
		self.rect.top = ship.rect.top
		self.rect.centerx = ship.rect.centerx

		# 存储子弹的位置
		self.y   = float(self.rect.y)
		self.color = ai_setting.bullet_color
		self.speed_factor = ai_setting.bullet_speed_factor

    # 更新位置
	def update(self):
		self.y -= self.speed_factor
		self.rect.y = self.y
		print(self.rect.y)
		pass

    # 绘制子弹
	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
		pass


