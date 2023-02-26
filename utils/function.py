from utils.constant import HIGH, WIDTH
import cv2
import time
import pygame

def get_position(results):
    cx, cy = 0, 0
    for handLms in results.multi_hand_landmarks:

        for index, lm in enumerate(handLms.landmark):
            if index == 9:
                h = HIGH
                w = WIDTH
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


def move_fruit(game):
    for fruit in game.fgame.all_fruit.sprites():

        if game.fgame.check_collision(game.fgame.player, fruit):
            if fruit.bonus is None:
                game.fgame.player.point += fruit.point * (1 + game.fgame.bonus_multiplicative)
            elif fruit.bonus == "banane":
                game.fgame.bonus_multiplicative = True
                game.begin_time_multiplicative = time.time()
            elif fruit.bonus == "banane_glace":
                game.fgame.bonus_freeze += 1
            elif fruit.bonus == "piment":
                game.fgame.bonus_speed = True
                game.begin_time_speed = time.time()
            game.fgame.all_fruit.remove(fruit)


def update_bonus(game, font):
    text_bonus_speed = font.render("BONUS fruit", True, (255, 255, 255))
    text_bonus_multiplicative = font.render("BONUS Score x2", True, (255, 255, 255))
    # text_bonus_freeze = font.render("BONUS + 2 Temps", True, (255, 255, 255))

    if game.fgame.bonus_speed:
        if time.time() - game.begin_time_speed < 2:
            game.screen.blit(text_bonus_speed, (220, 200))
        if time.time() - game.begin_time_speed > 10:
            game.fgame.bonus_speed = False
    if game.fgame.bonus_multiplicative:
        if time.time() - game.begin_time_multiplicative < 2:
            game.screen.blit(text_bonus_multiplicative, (220, 220))
        if time.time() - game.begin_time_multiplicative > 10:
            game.fgame.bonus_multiplicative = False


def check_end(game):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                print("fermeture du jeu")

    if time.time() - game.startTime - 2 * game.fgame.bonus_freeze > 60:
        running = False
        print(f"Le score est de {game.fgame.player.point}")
        pygame.quit()
