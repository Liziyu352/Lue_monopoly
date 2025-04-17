import pathlib

import pygame


class Petpet:
    def __init__(self, game):
        self.screen = game.screen
        self.setting = game.setting
        self.tilemap = game.tilemap
        self.screen_rect = game.screen.get_rect()
        self.tile_frames = {}
        for num, pos in self.setting.petpet_stats:
            texture = self.tilemap.get_texture(pos)
            self.tile_frames[num] = texture

    def placeButton(self, screen, center=(55,645)):
        tile = self.setting.buttons[screen][center]  # 得到贴图(x,y)
        texture = self.tilemap.get_texture(tile)
        self.image = pygame.transform.scale(texture, self.setting.buttonRect)
        self.rect.center = center

    def update(self):
        pygame.draw.rect(self.screen, self.bg_color, self.rect)
        self.screen.blit(self.image, self.rect)