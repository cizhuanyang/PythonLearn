import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """表示雨滴的类"""

    def __init__(self, ai_settings, screen):
        """初始化雨滴并设置起始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        """加载雨滴图像，并设置rect属性"""
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y=float(self.rect.y)

    def blitme(self):
        """绘制雨滴"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.ai_settings.raindrop_drop_speed
        self.rect.y = self.y

    def check_edges(self):
        """雨滴到达底部返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom>=screen_rect.bottom:
            return True