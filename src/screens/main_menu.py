import pygame
import os
import sys
from src.tools.button import Button
from src.screens import name_menu, option
from utils.config import cfg
from utils.function import get_font


def screen(SCREEN):
    while True:
        SCREEN.blit(cfg.IMAGES.BG_JUNGLE[0], (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(120).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(cfg.GAME_SETTING.WIDTH / 2, 200))

        NAME_BUTTON = Button(
            image=pygame.image.load(
                os.path.join(cfg.PATHS.ASSET_PATH, "Play Rect.png")
            ),
            pos=(cfg.GAME_SETTING.WIDTH / 2, 500),
            text_input="PLAY",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        OPTIONS_BUTTON = Button(
            image=pygame.image.load(
                os.path.join(cfg.PATHS.ASSET_PATH, "Options Rect.png")
            ),
            pos=(cfg.GAME_SETTING.WIDTH / 2, 750),
            text_input="OPTIONS",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        QUIT_BUTTON = Button(
            image=pygame.image.load(
                os.path.join(cfg.PATHS.ASSET_PATH, "Quit Rect.png")
            ),
            pos=(cfg.GAME_SETTING.WIDTH / 2, 900),
            text_input="QUIT",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [NAME_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NAME_BUTTON.checkForInput(MENU_MOUSE_POS):
                    name_menu.screen(SCREEN)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    option.screen(SCREEN)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
