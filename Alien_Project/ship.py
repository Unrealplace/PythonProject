import pygame

class Ship():
	"""初始化飞船并设置其位置"""
	def __init__(self, screen,ai_setting):
		super(Ship, self).__init__()
		self.screen = screen
		# 加载飞船，并获取其外接矩形
		self.image  = pygame.image.load('images/ship.bmp')
		self.rect   = self.image.get_rect()
		self.screen_rect = screen.get_rect()

        # 设置飞船的坐标
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom  = self.screen_rect.bottom
        
        # 判断是否向右边移动的标志，默认为false
		self.moving_right = False
		self.moving_left  = False

        #获取飞船的中心点
		self.center = float(self.rect.centerx)

		self.ai_setting = ai_setting


		
    #在指定位置绘制飞船
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		pass

    # 根据移动标志调整飞船的位置
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_setting.ship_speed_factor
			pass
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.center -= self.ai_setting.ship_speed_factor
			pass
		pass
		self.rect.centerx = self.center