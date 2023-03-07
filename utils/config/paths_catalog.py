import os
from yacs.config import CfgNode as CN

PATHS = CN()

PATHS.IMAGE_PATH = os.path.join("data", "images")
PATHS.ASSET_PATH = os.path.join("data", "assets")
PATHS.SOUND_PATH = os.path.join("data", "sonor_effects")