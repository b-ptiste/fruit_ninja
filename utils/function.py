import os
import cv2
import time
import pygame

from utils.config import cfg


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font(os.path.join(cfg.PATHS.ASSET_PATH, "font.ttf"), size)


def get_position(results):
    cx, cy = 0, 0
    for handLms in results.multi_hand_landmarks:
        for index, lm in enumerate(handLms.landmark):
            if index == 9:
                h = cfg.GAME_SETTING.HIGH
                w = cfg.GAME_SETTING.WIDTH
                cx, cy = int((1 - lm.x) * w), int(lm.y * h)
                break
        break
    return cx, cy


def move_player(game):
    _, img = game.cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = game.hands.process(img_rgb)
    if results.multi_hand_landmarks:
        cx, cy = get_position(results)
    else:
        cx, cy = game.fgame.player.rect.x, game.fgame.player.rect.y
    game.fgame.player.move(cx, cy)


def update_bonus(game, font, SCREEN):
    text_bonus_speed = font.render("BONUS FRUIT", True, "White")
    text_bonus_multiplicative = font.render("BONUS SCORE x2", True, "White")
    # text_bonus_freeze = font.render("BONUS + 2 Temps", True, (255, 255, 255))

    if game.fgame.bonus_speed:
        if time.time() - game.begin_time_speed < 2:
            SCREEN.blit(text_bonus_speed, (cfg.GAME_SETTING.WIDTH / 2 - 100, 200))
        if time.time() - game.begin_time_speed > cfg.GAME_SETTING.END_TIME_BONUS_SPEED:
            game.fgame.bonus_speed = False
    if game.fgame.bonus_multiplicative:
        if time.time() - game.begin_time_multiplicative < 2:
            SCREEN.blit(
                text_bonus_multiplicative, (cfg.GAME_SETTING.WIDTH / 2 - 100, 600)
            )
        if (
            time.time() - game.begin_time_multiplicative
            > cfg.GAME_SETTING.END_TIME_BONUS_MULT
        ):
            game.fgame.bonus_multiplicative = False


def check_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                print("END GAME")
