import pygame


class Fruit(pygame.sprite.Sprite):
    def __init__(self, path, speed, direction, sens, cx, cy, bonus=None):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.direction = direction
        self.sens = sens
        self.point = speed
        self.origin_image = self.image
        self.angle = 0
        self.rect.x = cx
        self.rect.y = cy
        self.bonus = bonus

    def rotate(self):
        self.angle += 30
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
