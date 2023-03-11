import pygame
from utils.config import cfg
from utils.function import move_player, update_bonus, check_exit
from src.tools.button import Button
from src.database.dataBase_sql import add_score, get_best_score
from src.screens import main_menu

from src.database.dataBase_sql import find_setting

pygame.init()

SCREEN = pygame.display.set_mode((cfg.GAME_SETTING.WIDTH, cfg.GAME_SETTING.HIGH))
pygame.display.set_caption("Menu")


if __name__ == "__main__":
    main_menu.screen(SCREEN)
