"""
重中之重
贴图检索模块
加载和管理游戏中的 tilemap
"""

import pygame


class TileMap:
    """TileMap 类，用于加载和检索贴图"""

    def __init__(self, game, tile_size=(130, 130)):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # 设置单个 tile 的尺寸
        self.tile_size = tile_size  # 默认 (130, 130)

        # 初始化 tiles 字典，用于存储贴图
        # 字典结构：键为 y 轴（字符串），值为对应 x 轴的贴图列表
        # 示例：{'0': [image#0,0, image#1,0, ...], '1': [image#0,1, image#1,1, ...]}
        self.tiles = {}

        # 加载并切割 tilemap 图像
        tilemap = pygame.image.load("./pic/tiles.png")
        self.load_tilemap(tilemap)

    def load_tilemap(self, tilemap):
        """
        加载并切割 tilemap 图像，将贴图存储到 tiles 字典中
        :param tilemap: Pygame Surface 对象，原始 tilemap 图像
        :return: None
        """
        # 支持 alpha(透明度)通道
        tilemap = tilemap.convert_alpha()
        tile_rect = tilemap.get_rect()

        # tiles信息
        tile_width, tile_height = self.tile_size
        tiles_width, tiles_height = tile_rect.width, tile_rect.height

        # 切割贴图
        for current_y in range(tiles_height // tile_height):
            tile_x = []  # 当前行的 tile
            for current_x in range(tiles_width // tile_width):
                rect = pygame.Rect(
                    current_x * tile_width, current_y * tile_height, *self.tile_size
                )
                tile_x.append(tilemap.subsurface(rect))
            # 将当前行的贴图列表存入字典，键为 y 坐标（字符串）
            self.tiles[str(current_y)] = tile_x

    def get_texture(self, tile_position):
        """
        根据 tilemap 中的 (x, y) 坐标获取对应的贴图
        :param tile_position: 元组 (x, y)，表示贴图在 tilemap 中的位置
        :return: Pygame Surface 对象（贴图），若未找到则返回 None
        """
        tile_x, tile_y = tile_position
        tile_column = self.tiles.get(str(tile_y))
        if tile_column and 0 <= tile_x < len(tile_column):
            #print(tile_x,tile_y)
            return tile_column[tile_x]
        return None  # 如果坐标无效或未找到，返回 None
