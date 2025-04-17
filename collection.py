"""
皮肤&涂鸦
"""

import pygame


class Collection:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("pic/collections.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def update(self):
        self.screen.blit(self.image, self.rect)
