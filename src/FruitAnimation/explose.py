import pygame
import os
from utils.config import cfg


class Explose(pygame.sprite.Sprite):
    def __init__(self, rect_x, rect_y):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(cfg.PATHS.IMAGE_PATH, "explose1.png")
        )
        self.images = animations["explose"]
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.current_image = 0
        self.animation = True

    def animate(self, loop=False):
        if self.animation:
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False
            self.image = self.images[self.current_image]


def load_animation_images():
    images = []
    for i in range(1, 46):
        image_path = os.path.join(cfg.PATHS.IMAGE_PATH, "explose" + str(i) + ".png")
        img = pygame.image.load(image_path)
        img_scale = pygame.transform.scale(img, (130, 130))
        images.append(img_scale)
    return images


animations = {"explose": load_animation_images()}
