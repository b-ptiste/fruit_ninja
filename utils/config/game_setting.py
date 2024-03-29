from yacs.config import CfgNode as CN
from src.database.dataBase_sql import find_setting

GAME_SETTING = CN()


# picture dimension
GAME_SETTING.HIGH = 1080
GAME_SETTING.WIDTH = 1920


GAME_SETTING.HOST = None
GAME_SETTING.USER = None
GAME_SETTING.PASSWORD = None
GAME_SETTING.DATABASE = None


# ratio
GAME_SETTING.RATIO_BONUS = None
GAME_SETTING.RATIO_BOMB = None

# AMOUNT CREATION BY IT
GAME_SETTING.AMOUNT_IT = None

# time
GAME_SETTING.END_TIME = 30

# name
GAME_SETTING.NAME = "default user"

# level
GAME_SETTING.LEVEL = "EASY"

# bonus
GAME_SETTING.END_TIME_BONUS_SPEED = 10
GAME_SETTING.END_TIME_BONUS_MULT = 10
