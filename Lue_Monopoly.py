"""
2024.2.4
大略翁1.0 pygame
感谢略nd给出的想法&贴图 刚好学完pygame 练个手
"""

import sys

import pygame

import buttonBox
import collection
import menu
import settings
import tilemap


class LueMonopoly:
    """主游戏类，负责初始化和管理游戏的核心功能"""

    def __init__(self):
        """初始化 Pygame 和游戏基本组件"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.setting = settings.Settings()

        self.screen = pygame.display.set_mode(self.setting.screen)
        pygame.display.set_caption("大略翁1.0")

        self.menu_buttons = pygame.sprite.Group()
        self.collections_buttons = pygame.sprite.Group()

        self.tilemap = tilemap.TileMap(self)
        self.menu = menu.Menu(self)
        self.collection = collection.Collection(self)

        # 跟踪按钮点击状态和当前显示的界面
        self.button_clicked = []  # 存储点击的按钮信息（目前未使用）
        self.onDisplay = "menu"  # 当前显示的界面，初始为菜单

        # 放置初始菜单界面的按钮
        self._place_button("menu")

    def _place_button(self, screen):
        for pos,tile in self.setting.buttons[screen].items():
            button = buttonBox.ButtonBox(self)
            button.placeButton(screen,pos)
            #print(screen,pos,tile)
            eval(f"self.{screen}_buttons.add(button)")

    def check_event(self):
        """处理游戏事件，如退出和鼠标点击"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)  # 点击窗口关闭按钮退出游戏
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # 获取鼠标点击位置
                # 检查菜单界面按钮点击
                for button in self.menu_buttons:
                    if button.rect.collidepoint(mouse_pos):
                        self.act_click(button.rect.center)
                # 检查收藏界面按钮点击
                for button in self.collections_buttons:
                    if button.rect.collidepoint(mouse_pos):
                        self.act_click(button.rect.center)

    def act_click(self, button_rect):
        """处理按钮点击后的行为"""
        # 根据当前界面和按钮位置执行相应操作
        #print(button_rect)
        if self.onDisplay == "menu":
            if button_rect == (34, 34):  # EXIT 按钮
                sys.exit(0)  # 退出游戏
            elif button_rect == (1000, 55):
                self.menu_buttons.empty()
                self._place_button("collections")
                self.onDisplay = "collections"
            # TODO: 更多按钮功能
        elif self.onDisplay == "collections":
            if button_rect == (34, 34):  # 返回菜单
                self.collections_buttons.empty()
                self._place_button("menu")
                self.onDisplay = "menu"

        # 清空点击记录（目前未使用）
        self.button_clicked.clear()

    def update_screen(self):
        """更新游戏屏幕内容"""
        self.screen.fill(self.setting.bg_color)

        # 根据当前界面更新显示内容
        if self.onDisplay == "menu":
            self.menu.update()
            self.menu_buttons.update()
        elif self.onDisplay == "collections":
            self.collection.update()
            self.collections_buttons.update()

        # 刷新屏幕显示
        pygame.display.flip()

    def start(self):
        """启动游戏主循环"""
        while True:
            self.check_event()
            self.update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    """程序入口，创建游戏实例并启动"""
    main = LueMonopoly()
    main.start()
