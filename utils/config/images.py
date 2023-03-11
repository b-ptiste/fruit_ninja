import os
import pygame
from yacs.config import CfgNode as CN
from utils.config.paths_catalog import PATHS

IMAGES = CN()

IMAGES.BG_JUNGLE = [
    pygame.image.load(os.path.join(PATHS.IMAGE_PATH, "background_jungle.jpg"))
]
IMAGES.BG_SCORE = [pygame.image.load(os.path.join(PATHS.IMAGE_PATH, "ranking.jpg"))]
IMAGES.BG_OPTION = [pygame.image.load(os.path.join(PATHS.IMAGE_PATH, "option.png"))]
IMAGES.CROSS_GREEN = [
    pygame.image.load(os.path.join(PATHS.IMAGE_PATH, "cross_green.png"))
]
IMAGES.CROSS_RED = [pygame.image.load(os.path.join(PATHS.IMAGE_PATH, "cross_red.png"))]
