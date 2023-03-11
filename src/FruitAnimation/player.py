import os

import pygame.sprite
from utils.config import cfg


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(cfg.PATHS.IMAGE_PATH, "kunai.png"))

        # image zone
        self.rect = self.image.get_rect()
        self.rect.x = cfg.GAME_SETTING.WIDTH / 2
        self.rect.y = cfg.GAME_SETTING.HIGH / 2

        self.point = 0

    def move(self, cx, cy):
        if (0 <= cy) and (cy <= cfg.GAME_SETTING.HIGH - self.rect.height):
            self.rect.y = cy
        if (0 <= cx) and (cx <= cfg.GAME_SETTING.WIDTH + self.rect.width / 2):
            self.rect.x = cx
