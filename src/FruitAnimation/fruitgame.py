from src.FruitAnimation.player import Player
from src.FruitAnimation.fruit import *
from utils.config import cfg
import random
import os


class FruitGame:
    def __init__(self):
        self.player = Player()
        self.all_fruit = pygame.sprite.Group()
        self.bonus_speed = False
        self.bonus_freeze = 0
        self.bonus_multiplicative = False

    def launch_fruit(self, specials=None):
        side = random.randint(1, 4)
        speed_min = 5
        speed_max = 20
        dir_min = -1
        dir_max = 1
        cx_min = 500
        cx_max = cfg.GAME_SETTING.WIDTH - 500
        cy_min = 500
        cy_max = cfg.GAME_SETTING.HIGH - 500

        fruits = cfg.OBJ_LIST.FRUIT_LIST
        bonus = cfg.OBJ_LIST.BONUS_LIST
        bomb = cfg.OBJ_LIST.BOMB_LIST

        if specials == "bonus":
            speed = 5
            rand_bonus = random.choice(bonus)
            path = os.path.join(cfg.PATHS.IMAGE_PATH, rand_bonus + ".png")
        elif specials == "bomb":
            speed = 5
            rand_bonus = random.choice(bomb)
            path = os.path.join(cfg.PATHS.IMAGE_PATH, rand_bonus + ".png")
        else:
            speed = random.randint(speed_min, speed_max)
            rand_bonus = None
            path = os.path.join(cfg.PATHS.IMAGE_PATH, random.choice(fruits) + ".png")

        if side == 1:
            direction = random.randint(dir_min, dir_max)
            sens = 1
            cx = 0
            cy = random.randint(cy_min, cy_max)

        elif side == 2:
            direction = random.randint(dir_min, dir_max)
            sens = -1
            cx = cfg.GAME_SETTING.WIDTH
            cy = random.randint(cy_min, cy_max)

        elif side == 3:
            direction = random.randint(0, dir_max)
            sens = -1
            cx = random.randint(cx_min, cx_max)
            cy = -20

        else:
            direction = random.randint(dir_min, 0)
            sens = 1
            cx = random.randint(cx_min, cx_max)
            cy = cfg.GAME_SETTING.HIGH

        self.all_fruit.add(Fruit(path, speed, direction, sens, cx, cy, rand_bonus))

    def move(self):
        for fruit in self.all_fruit:
            cx = fruit.sens
            cy = fruit.direction
            fruit.rect.x += cx * (
                fruit.speed - fruit.speed / 2 * (self.bonus_freeze >= 1)
            )
            fruit.rect.y += cy * (
                fruit.speed - fruit.speed / 2 * (self.bonus_freeze >= 1)
            )
            fruit.rotate()
            if (fruit.rect.x > cfg.GAME_SETTING.WIDTH) or (
                fruit.rect.x + fruit.rect.width < 0
            ):
                self.all_fruit.remove(fruit)
            if (fruit.rect.y > cfg.GAME_SETTING.HIGH) or (
                fruit.rect.y + fruit.rect.height < 0
            ):
                self.all_fruit.remove(fruit)

    @staticmethod
    def check_collision(player, fruit):
        return pygame.sprite.collide_mask(player, fruit)
