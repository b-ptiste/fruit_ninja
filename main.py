import pygame
from src.gameLauncher import GameLauncher
import time
import random
from utils.constant import WIDTH, HIGH, ASSET_PATH, IMAGE_PATH, END_TIME, RATIO_BONUS, RATIO_BOMB, AMOUNT_IT
from utils.function import move_player, update_bonus, check_exit
from src.FruitAnimation.explose import Explose
import sys
import os
from src.tools.button import Button
from src.database.dataBase_mongo import connect_to_db, add_score, disconect_to_db

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HIGH))
pygame.display.set_caption("Menu")

BG = pygame.image.load(os.path.join(IMAGE_PATH, "background_jungle.jpg"))
CROSS_GREEN = pygame.image.load(os.path.join(IMAGE_PATH, "cross_green.png"))
CROSS_RED = pygame.image.load(os.path.join(IMAGE_PATH, "cross_red.png"))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font(os.path.join(ASSET_PATH, "font.ttf"), size)


def play_temp():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))


        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH / 2, 200))

        PLAY_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH / 2, 500),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Options Rect.png")), pos=(WIDTH / 2, 750),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Quit Rect.png")), pos=(WIDTH / 2, 900),
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
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH / 2, 200))

        MAIN_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH / 2, 875),
                             text_input="MENU", font=get_font(75), base_color="#d7fcd4",
                             hovering_color="White")
        REPLAY_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Options Rect.png")),
                               pos=(WIDTH / 2, 1000), text_input="REPLAY", font=get_font(75), base_color="#d7fcd4",
                               hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

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
                SCREEN.blit(CROSS_GREEN, (WIDTH - i * 150, 100))
            else:
                SCREEN.blit(CROSS_RED, (WIDTH - i * 150, 100))

        # show remaining time
        time_text = font.render(f"Temps : {round(time.time() - game.startTime - game.fgame.bonus_freeze, 2)}",
                                True,
                                (255, 255, 255)
                                )
        SCREEN.blit(time_text, (WIDTH - 400, 20))

        # creation des fruits

        for _ in range(AMOUNT_IT):
            with_bonus = random.randint(1, RATIO_BONUS)
            with_bomb = random.randint(1, RATIO_BOMB)
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
            (time.time() - game.startTime - game.fgame.bonus_freeze > END_TIME)
        if cond_stop:
            client = connect_to_db()
            add_score(client['fruit_ninja'], "baptiste", game.fgame.player.point)
            disconect_to_db(client)
            score_menu()

        check_exit(game)

if __name__ == '__main__':
    main_menu()


#TODO change mode
#TODO save BDD
#TODO Display best score
#TODO Deploy
#TODO refactoring code
