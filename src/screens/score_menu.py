import os
import pygame
from utils.function import get_font
from src.tools.button import Button
from src.screens import main_menu, play
from src.database.dataBase_sql import get_best_score
import sys
from utils.config import cfg


def screen(player_score, player_name, u_id, SCREEN):
    FIRST = True
    while True:
        SCREEN.blit(cfg.IMAGES.BG_SCORE[0], (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MAIN_BUTTON = Button(
            image=pygame.image.load(
                os.path.join(cfg.PATHS.ASSET_PATH, "Play Rect.png")
            ),
            pos=(cfg.GAME_SETTING.WIDTH / 2 - 300, 1000),
            text_input="MENU",
            font=get_font(30),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        REPLAY_BUTTON = Button(
            image=pygame.image.load(
                os.path.join(cfg.PATHS.ASSET_PATH, "Play Rect.png")
            ),
            pos=(cfg.GAME_SETTING.WIDTH / 2 + 300, 1000),
            text_input="REPLAY",
            font=get_font(30),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        font = pygame.font.SysFont("Potta One", 60, 2)

        if FIRST:
            FIRST = False
            scores = get_best_score()
        score_curr_add = True
        for idx, score in enumerate(scores):
            if u_id == score[0]:
                score_curr_add = False
                SCREEN.blit(
                    font.render(f"{score[1]}", True, "Green"), (800, idx * 130 + 280)
                )  # show score
                SCREEN.blit(
                    font.render(f"{score[2]}", True, "Green"), (520, idx * 130 + 280)
                )  # show score
            elif score_curr_add and idx == 4:
                SCREEN.blit(
                    font.render(f"{player_score}", True, "Green"),
                    (800, idx * 130 + 280),
                )  # show score
                SCREEN.blit(
                    font.render(f"{player_name}", True, "Green"), (520, idx * 130 + 280)
                )  # show score
            else:
                SCREEN.blit(
                    font.render(f"{score[1]}", True, (255, 255, 255)),
                    (800, idx * 130 + 280),
                )  # show score
                SCREEN.blit(
                    font.render(f"{score[2]}", True, (255, 255, 255)),
                    (520, idx * 130 + 280),
                )  # show score

        for button in [MAIN_BUTTON, REPLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu.screen(SCREEN)
                if REPLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play.screen(SCREEN)

        pygame.display.update()
