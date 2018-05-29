import pygame

class Ship():
	"""初始化飞船并设置其位置"""
	def __init__(self, screen):
		super(Ship, self).__init__()
		self.screen = screen
		# 加载飞船，并获取其外接矩形
		self.image  = pygame.image.load('images/ship.bmp')
		self.rect   = self.image.get_rect()
		self.screen_rect = screen.get_rect()

        # 设置飞船的坐标
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom  = self.screen_rect.bottom

    #在指定位置绘制飞船
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		pass