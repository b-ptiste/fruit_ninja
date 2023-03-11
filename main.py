import pygame
import argparse

from src.screens import main_menu
from src.database.dataBase_sql import find_setting
from utils.config import cfg


def parse_args():
    parser = argparse.ArgumentParser(description="Testing")

    parser.add_argument(
        "--host", required=False, type=str, help="host of your mysql DB"
    )

    parser.add_argument("--user", required=True, type=str, help="root of your mysql DB")

    parser.add_argument(
        "--password", required=True, type=str, help="password of your mysql DB"
    )

    parser.add_argument(
        "--database", required=True, type=str, help="name to store the results"
    )

    args = parser.parse_args()

    return args


pygame.init()

SCREEN = pygame.display.set_mode((cfg.GAME_SETTING.WIDTH, cfg.GAME_SETTING.HIGH))
pygame.display.set_caption("Menu")


if __name__ == "__main__":
    args = parse_args()
    cfg.GAME_SETTING.HOST = args.host
    cfg.GAME_SETTING.USER = args.user
    cfg.GAME_SETTING.PASSWORD = args.password
    cfg.GAME_SETTING.DATABASE = args.database

    settings = find_setting(
        "EASY",
        cfg.GAME_SETTING.HOST,
        cfg.GAME_SETTING.USER,
        cfg.GAME_SETTING.PASSWORD,
        cfg.GAME_SETTING.DATABASE,
    )

    cfg.GAME_SETTING.RATIO_BONUS = settings[1]
    cfg.GAME_SETTING.RATIO_BOMB = settings[2]

    # AMOUNT CREATION BY IT
    cfg.GAME_SETTING.AMOUNT_IT = settings[3]

    print(settings[0])
    main_menu.screen(SCREEN)
