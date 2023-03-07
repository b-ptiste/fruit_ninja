import pygame
import pymongo
from src.gameLauncher import GameLauncher
import time
import random
from utils.config import cfg
from utils.function import move_player, update_bonus, check_exit
from src.FruitAnimation.explose import Explose
import sys
import os
from src.tools.button import Button
from src.database.dataBase_sql import add_setting_score, get_best_score

from src.database.dataBase_sql import find_setting
pygame.init()

SCREEN = pygame.display.set_mode((cfg.GAME_SETTING.WIDTH, cfg.GAME_SETTING.HIGH))
pygame.display.set_caption("Menu")

BG = pygame.image.load(os.path.join(cfg.PATHS.IMAGE_PATH, "background_jungle.jpg"))
CROSS_GREEN = pygame.image.load(os.path.join(cfg.PATHS.IMAGE_PATH, "cross_green.png"))
CROSS_RED = pygame.image.load(os.path.join(cfg.PATHS.IMAGE_PATH, "cross_red.png"))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font(os.path.join(cfg.PATHS.ASSET_PATH, "font.ttf"), size)


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_EASY = Button(image=None, pos=(640, 660),
                              text_input="EASY", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_MEDIUM = Button(image=None, pos=(640, 860),
                              text_input="MEDIUM", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_HARD = Button(image=None, pos=(640, 1060),
                              text_input="HARD", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for button in [OPTIONS_BACK, OPTIONS_EASY, OPTIONS_MEDIUM, OPTIONS_HARD]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                else:
                    if OPTIONS_EASY.checkForInput(OPTIONS_MOUSE_POS):
                        settings = find_setting("EASY")
                    if OPTIONS_MEDIUM.checkForInput(OPTIONS_MOUSE_POS):
                        settings = find_setting("MEDIUM")
                    if OPTIONS_HARD.checkForInput(OPTIONS_MOUSE_POS):
                        settings = find_setting("HARD")
                    # ratio
                    cfg.GAME_SETTING.RATIO_BONUS = settings[1]
                    cfg.GAME_SETTING.RATIO_BOMB = settings[2]

                    # AMOUNT CREATION BY IT
                    cfg.GAME_SETTING.AMOUNT_IT = settings[3]
        

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))


        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(cfg.GAME_SETTING.WIDTH / 2, 200))

        PLAY_BUTTON = Button(image=pygame.image.load(os.path.join(cfg.PATHS.ASSET_PATH, "Play Rect.png")), pos=(cfg.GAME_SETTING.WIDTH / 2, 500),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(os.path.join(cfg.PATHS.ASSET_PATH, "Options Rect.png")), pos=(cfg.GAME_SETTING.WIDTH / 2, 750),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(os.path.join(cfg.PATHS.ASSET_PATH, "Quit Rect.png")), pos=(cfg.GAME_SETTING.WIDTH / 2, 900),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def score_menu():
    while True:
        SCREEN.blit(BG, (0, 0))


        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("SCORE", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(cfg.GAME_SETTING.WIDTH / 2, 200))

        MAIN_BUTTON = Button(image=pygame.image.load(os.path.join(cfg.PATHS.ASSET_PATH, "Play Rect.png")), pos=(cfg.GAME_SETTING.WIDTH / 2, 875),
                             text_input="MENU", font=get_font(75), base_color="#d7fcd4",
                             hovering_color="White")
        REPLAY_BUTTON = Button(image=pygame.image.load(os.path.join(cfg.PATHS.ASSET_PATH, "Options Rect.png")),
                               pos=(cfg.GAME_SETTING.WIDTH / 2, 1000), text_input="REPLAY", font=get_font(75), base_color="#d7fcd4",
                               hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        print(get_best_score(""))
        for button in [MAIN_BUTTON, REPLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                if REPLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()

        pygame.display.update()

def play():
    game = GameLauncher()

    running = True
    font = pygame.font.SysFont("Potta One", 60, 2)

    while running:

        SCREEN.blit(BG, (0, 0))  # show background
        SCREEN.blit(game.fgame.player.image, game.fgame.player.rect)  # show kunai
        score_text = font.render(f"Score : {game.fgame.player.point}", True, (255, 255, 255))  # show score
        SCREEN.blit(score_text, (40, 20))

        for i in range(4):
            if i > game.bomb_collusion:
                SCREEN.blit(CROSS_GREEN, (cfg.GAME_SETTING.WIDTH - i * 150, 100))
            else:
                SCREEN.blit(CROSS_RED, (cfg.GAME_SETTING.WIDTH - i * 150, 100))

        # show remaining time
        time_text = font.render(f"Temps : {round(time.time() - game.startTime - game.fgame.bonus_freeze, 2)}",
                                True,
                                (255, 255, 255)
                                )
        SCREEN.blit(time_text, (cfg.GAME_SETTING.WIDTH - 400, 20))

        # creation des fruits

        for _ in range(cfg.GAME_SETTING.AMOUNT_IT):
            with_bonus = random.randint(1, cfg.GAME_SETTING.RATIO_BONUS)
            with_bomb = random.randint(1, cfg.GAME_SETTING.RATIO_BOMB)
            if time.time() - game.currTime > 1 - 0.75 * game.fgame.bonus_speed:
                game.fgame.launch_fruit()
                game.currTime = time.time()
            if with_bonus == 1:
                game.fgame.launch_fruit("bonus")
            if with_bomb == 1:
                game.fgame.launch_fruit("bomb")

        game.fgame.move()  # animation des fruits
        game.fgame.all_fruit.draw(SCREEN)  # afficher les fruits

        # position du doigt
        move_player(game)
        for fruit in game.fgame.all_fruit.sprites():
            if game.fgame.check_collision(game.fgame.player, fruit):
                if fruit.bonus == "bomb":
                    game.all_explosion.add(Explose(fruit.rect.x, fruit.rect.y))
                    game.bomb_collusion += 1
                elif fruit.bonus is None:
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

        update_bonus(game, font, SCREEN)

        for explosion in game.all_explosion:
            if explosion.animation:
                explosion.animate()
            else:
                game.all_explosion.remove(explosion)
        game.all_explosion.draw(SCREEN)

        game.fgame.all_fruit.draw(SCREEN)
        pygame.display.flip()
        # screen update
        cond_stop = (game.bomb_collusion >= 3) or \
            (time.time() - game.startTime - game.fgame.bonus_freeze > cfg.GAME_SETTING.END_TIME)
        if cond_stop:
            add_setting_score("baptisye", int(game.fgame.player.point))
            score_menu()

        check_exit(game)

if __name__ == '__main__':
    main_menu()


#TODO change mode
#TODO save BDD
#TODO Display best score
#TODO Deploy
#TODO refactoring code
