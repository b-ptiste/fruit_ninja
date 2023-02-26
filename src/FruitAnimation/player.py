import pygame.sprite
import os

# comport constant
from utils.constant import WIDTH, HIGH, IMAGE_PATH


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(IMAGE_PATH, "kunai.png"))

        # image zone
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HIGH / 2

        self.point = 0

    def move(self, cx, cy):
        if (0 <= cy) and (cy <= HIGH - self.rect.height):
            self.rect.y = cy
        if (0 <= cx) and (cx <= WIDTH + self.rect.width / 2):
            self.rect.x = cx
