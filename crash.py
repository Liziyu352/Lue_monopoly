"""
三连关注
"""

import pygame


class Crash:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("pic/crash.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def update(self):
        self.screen.blit(self.image, self.rect)
