from yacs.config import CfgNode as CN

GAME_SETTING = CN()

from src.database.dataBase_sql import find_setting
settings = find_setting("EASY")


# picture dimension
GAME_SETTING.HIGH = 1080
GAME_SETTING.WIDTH = 1920

settings = find_setting("EASY")
# ratio
GAME_SETTING.RATIO_BONUS = settings[1]
GAME_SETTING.RATIO_BOMB = settings[2]

# AMOUNT CREATION BY IT
GAME_SETTING.AMOUNT_IT = settings[3]

# time
GAME_SETTING.END_TIME = 15

# name

GAME_SETTING.NAME = "default user"