"""
按钮碰撞箱
由于游戏中可能有多个按钮，使用 Pygame 的 Sprite 类进行管理
"""

import pygame


class ButtonBox(pygame.sprite.Sprite):
    """按钮碰撞箱类，用于检测点击并显示按钮"""

    def __init__(self, game):
        """初始化按钮的基本属性"""
        super().__init__()
        self.tilemap = game.tilemap
        self.screen = game.screen
        self.setting = game.setting

        self.rect = pygame.Rect(
            0, 0, self.setting.buttonRect[0], self.setting.buttonRect[1]
        )
        self.bg_color = self.setting.bg_color

        self.font = pygame.font.SysFont(None, 10)


    def placeButton(self, screen, center):
        tile = self.setting.buttons[screen][center] #得到贴图(x,y)
        texture = self.tilemap.get_texture(tile)
        self.image = pygame.transform.scale(texture, self.setting.buttonRect)
        self.rect.center = center

    def update(self):
        pygame.draw.rect(self.screen,self.bg_color,self.rect)
        self.screen.blit(self.image,self.rect)
