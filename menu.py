"""
开始菜单
管理游戏的菜单界面，包含动态背景动画
"""

import pathlib
import pygame


class Menu:
    """菜单类，负责显示和更新开始菜单的动态背景"""

    def __init__(self, game):
        """初始化菜单对象"""
        self.game = game
        self.screen = self.game.screen
        self.screen_rect = self.game.screen.get_rect()

        self.last_update = pygame.time.get_ticks()  # 上次切帧的刻
        self.frame_delay = 80  # 每帧间隔80ms

        # 加载背景帧
        self.frame_path = pathlib.Path("pic/background")
        self.frames = []

        for item in sorted(self.frame_path.glob("*.png")):  # 仅加载图像
            frame = pygame.image.load(str(item)).convert_alpha()  # 支持透明度
            rect = frame.get_rect()
            rect.center = self.screen_rect.center  # 居中!!!!!
            self.frames.append((frame, rect))

        # 帧计数器
        self.frame_num = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.frame_delay:  # 间隔足够80ms时
            self.screen.blit(
                self.frames[self.frame_num][0], self.frames[self.frame_num][1]  # image
            )  # rect

            self.frame_num = (self.frame_num + 1) % len(self.frames)  # 到了6自动变0

            self.last_update = current_time
        else:
            self.screen.blit(
                self.frames[self.frame_num][0], self.frames[self.frame_num][1]
            )
