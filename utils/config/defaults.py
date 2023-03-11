from yacs.config import CfgNode as CN
from .game_setting import GAME_SETTING
from .obj_list import OBJ_LIST
from .paths_catalog import PATHS
from .images import IMAGES

cfg = CN()
cfg.GAME_SETTING = GAME_SETTING
cfg.OBJ_LIST = OBJ_LIST
cfg.PATHS = PATHS
cfg.IMAGES = IMAGES
