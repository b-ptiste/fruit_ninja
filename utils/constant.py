import os
import pygame
# picture dimension
HIGH = 1080
WIDTH = 1920

# data path
IMAGE_PATH = os.path.join("..", "data", "images")
ASSET_PATH = os.path.join("..", "data", "assets")
SOUND_PATH = os.path.join("..", "data", "sonor_effects")

# fruit list
FRUIT_LIST = ["ananas", "fraise", "fruit_passion", "kiwi", "pasteque", "poivron_jaune", "poivron_rouge",
              "poivron_vert", "pomme_verte"]

# bonus list
BONUS_LIST = ["banane", "banane_glace", "piment"]

#bomb list
BOMB_LIST = ["bomb"]

# ratio
RATIO_BONUS = 40
RATIO_BOMB = 40

# AMOUNT CREATION BY IT
AMOUNT_IT = 5

# mode : EASY, MEDIUM, HARD
MODE = "EASY"

# time
END_TIME = 15





