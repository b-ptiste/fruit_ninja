import pygame
from src.gameLauncher import GameLauncher
import time
import random
import uuid
from utils.config import cfg
from utils.function import move_player, update_bonus, check_exit
from src.FruitAnimation.explose import Explose
import sys
import os
from src.tools.button import Button
from src.database.dataBase_sql import add_score, get_best_score
from src.screens import play, score_menu, main_menu, name_menu, option

from src.database.dataBase_sql import find_setting

pygame.init()

SCREEN = pygame.display.set_mode((cfg.GAME_SETTING.WIDTH, cfg.GAME_SETTING.HIGH))
pygame.display.set_caption("Menu")

BG_JUNGLE = pygame.image.load(
    os.path.join(cfg.PATHS.IMAGE_PATH, "background_jungle.jpg")
)
BG_SCORE = pygame.image.load(os.path.join(cfg.PATHS.IMAGE_PATH, "ranking.jpg"))
BG_OPTION = pygame.image.load(os.path.join(cfg.PATHS.IMAGE_PATH, "option.png"))
CROSS_GREEN = pygame.image.load(os.path.join(cfg.PATHS.IMAGE_PATH, "cross_green.png"))
CROSS_RED = pygame.image.load(os.path.join(cfg.PATHS.IMAGE_PATH, "cross_red.png"))








if __name__ == "__main__":
    main_menu.screen()
