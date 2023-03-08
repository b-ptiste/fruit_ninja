from player import Player
from fruit import *
import random
import os
from utils.config import cfg

class Game:
    def __init__(self):
        self.player = Player()
        self.all_fruit = pygame.sprite.Group()
        self.bonus_speed = False
        self.bonus_freeze = 0
        self.bonus_multiplicatif = False

    def launch_fruit(self, with_bonus=False):
        side = random.randint(1, 4)
        speed_min = 2
        speed_max = 5
        dir_min = -1
        dir_max = 1
        cx_min = 250
        cx_max = 300
        cy_min = 200
        cy_max = 250

        fruits = cfg.OBJ_LIST.fruit_list

        bonus = cfg.OBJ_LIST.bonus_list
        if with_bonus:
            speed = 5
            rand_bonus = random.choice(bonus)
            path = os.path.join(cfg.PATHS.IMAGE_PATH, rand_bonus+".png")
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
            cx = 628
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
            cy = 417
        self.all_fruit.add(Fruit(path, speed, direction, sens, cx, cy, rand_bonus))

    def move(self):
        for fruit in self.all_fruit:
            cx = fruit.sens
            cy = fruit.direction
            fruit.rect.x += cx*(fruit.speed - fruit.speed / 2 * (self.bonus_freeze >= 1))
            fruit.rect.y += cy*(fruit.speed - fruit.speed / 2 * (self.bonus_freeze >= 1))
            fruit.rotate()
            if (fruit.rect.x > 628) or (fruit.rect.x+fruit.rect.width < 0):
                self.all_fruit.remove(fruit)
            if (fruit.rect.y > 417) or (fruit.rect.y+fruit.rect.height < 0):
                self.all_fruit.remove(fruit)

    def check_collision(self, player, fruit):
        return pygame.sprite.collide_mask(player, fruit)
