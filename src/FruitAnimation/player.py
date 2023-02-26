import pygame.sprite
import os

# path
IMAGE_PATH = os.path.join("..", "..", "data", "images")
SOUND_PATH = os.path.join("..","..", "data", "sonor_effects")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.kunai =  pygame.image.load(os.path.join(IMAGE_PATH, "kunai.png"))
        self.image = pygame.image.load(os.path.join(IMAGE_PATH, "lame_test.png"))
        # image zone
        self.rect1 = self.kunai.get_rect()
        self.rect1.x = 628/2
        self.rect1.y = 417/2

        self.rect = self.image.get_rect()
        self.rect.x = 628 / 2 + 14.5
        self.rect.y = 417 / 2 + 9
        self.point = 0

    def move(self,cx,cy):
        if (0 <= cy) and (cy <= 417 - self.rect1.height):
            self.rect1.y = cy
        if (0 <= cx) and (cx <= 628 + self.rect1.width / 2):
            self.rect1.x = cx

        self.rect.y = cy + 14.5
        self.rect.x = cx + 9
