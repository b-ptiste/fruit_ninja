from utils.config import cfg
import cv2
import time
import pygame


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
    success, img = game.cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = game.hands.process(img_rgb)
    if results.multi_hand_landmarks:
        cx, cy = get_position(results)
    else:
        cx, cy = game.fgame.player.rect.x, game.fgame.player.rect.y
    game.fgame.player.move(cx, cy)


def update_bonus(game, font, SCREEN):
    text_bonus_speed = font.render("BONUS fruit", True, (255, 255, 255))
    text_bonus_multiplicative = font.render("BONUS Score x2", True, (255, 255, 255))
    # text_bonus_freeze = font.render("BONUS + 2 Temps", True, (255, 255, 255))

    if game.fgame.bonus_speed:
        if time.time() - game.begin_time_speed < 2:
            SCREEN.blit(text_bonus_speed, (cfg.GAME_SETTING.WIDTH/2 - 100, 200))
        if time.time() - game.begin_time_speed > 10:
            game.fgame.bonus_speed = False
    if game.fgame.bonus_multiplicative:
        if time.time() - game.begin_time_multiplicative < 2:
            SCREEN.blit(text_bonus_multiplicative, (cfg.GAME_SETTING.WIDTH/2 - 100, 600))
        if time.time() - game.begin_time_multiplicative > 10:
            game.fgame.bonus_multiplicative = False


def check_exit(game):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                print("fermeture du jeu")


