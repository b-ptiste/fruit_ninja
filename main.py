import pygame
from src.gameLauncher import GameLauncher
import time
import random
from utils.config import cfg
from utils.function import move_player, update_bonus, check_exit
from src.FruitAnimation.explose import Explose
import sys
import os
from src.tools.button import Button
from src.database.dataBase_sql import add_score, get_best_score

from src.database.dataBase_sql import find_setting
pygame.init()

SCREEN = pygame.display.set_mode((cfg.GAME_SETTING.WIDTH, cfg.GAME_SETTING.HIGH))
pygame.display.set_caption("Menu")

BG_JUNGLE = pygame.image.load(os.path.join(cfg.PATHS.IMAGE_PATH, "background_jungle.jpg"))
BG_SCORE = pygame.image.load(os.path.join(cfg.PATHS.IMAGE_PATH, "ranking.jpg"))
BG_OPTION = pygame.image.load(os.path.join(cfg.PATHS.IMAGE_PATH, "option.png"))
CROSS_GREEN = pygame.image.load(os.path.join(cfg.PATHS.IMAGE_PATH, "cross_green.png"))
CROSS_RED = pygame.image.load(os.path.join(cfg.PATHS.IMAGE_PATH, "cross_red.png"))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font(os.path.join(cfg.PATHS.ASSET_PATH, "font.ttf"), size)


def options():
    while True:
        SCREEN.blit(BG_OPTION, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_BACK = Button(image=None, pos=(cfg.GAME_SETTING.WIDTH/2 + 50, 300),
                              text_input="BACK", font=get_font(80), base_color="White", hovering_color="White")
        OPTIONS_EASY = Button(image=None, pos=(cfg.GAME_SETTING.WIDTH/2 - 500, 100),
                              text_input="EASY", font=get_font(80), base_color="Green", hovering_color="White")
        OPTIONS_MEDIUM = Button(image=None, pos=(cfg.GAME_SETTING.WIDTH/2, 100),
                              text_input="MEDIUM", font=get_font(80), base_color="Orange", hovering_color="White")
        OPTIONS_HARD = Button(image=None, pos=(cfg.GAME_SETTING.WIDTH/2 + 500, 100),
                              text_input="HARD", font=get_font(80), base_color="Red", hovering_color="White")

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
                    clic = False
                    if OPTIONS_EASY.checkForInput(OPTIONS_MOUSE_POS):
                        clic = True
                        settings = find_setting()
                        cfg.GAME_SETTING.LEVEL = "EASY"
                    if OPTIONS_MEDIUM.checkForInput(OPTIONS_MOUSE_POS):
                        clic = True
                        settings = find_setting("MEDIUM")
                        cfg.GAME_SETTING.LEVEL = "MEDIUM"
                    if OPTIONS_HARD.checkForInput(OPTIONS_MOUSE_POS):
                        clic = True
                        settings = find_setting("HARD")
                        cfg.GAME_SETTING.LEVEL = "HARD"
                    # ratio
                    if clic:
                        cfg.GAME_SETTING.RATIO_BONUS = settings[1]
                        cfg.GAME_SETTING.RATIO_BOMB = settings[2]

                        # AMOUNT CREATION BY IT
                        cfg.GAME_SETTING.AMOUNT_IT = settings[3]
        

        pygame.display.update()



def name_menu():

    
    base_font = get_font(32)
    user_text = ''
    input_rect = pygame.Rect(cfg.GAME_SETTING.WIDTH / 2 - 50, 400, 200, 80)
    color_active = pygame.Color('lightskyblue3')

    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('white')
    color = color_passive
    
    active = False
    while True:
        SCREEN.blit(BG_JUNGLE, (0, 0))


        MENU_MOUSE_POS = pygame.mouse.get_pos()

        NAME_TEXT = get_font(50).render("CHOSE YOUR NAME", True, "white")
        MENU_RECT = NAME_TEXT.get_rect(center=(cfg.GAME_SETTING.WIDTH / 2, 300))

        LEVEL_TEXT = get_font(100).render(f"LEVEL {cfg.GAME_SETTING.LEVEL}", True, "#b68f40")
        LEVEL_RECT = NAME_TEXT.get_rect(center=(cfg.GAME_SETTING.WIDTH / 2 , 100))

        PLAY_BUTTON = Button(image=pygame.image.load(os.path.join(cfg.PATHS.ASSET_PATH, "Play Rect.png")), pos=(cfg.GAME_SETTING.WIDTH / 2, 700),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load(os.path.join(cfg.PATHS.ASSET_PATH, "Quit Rect.png")), pos=(cfg.GAME_SETTING.WIDTH / 2, 900),
                             text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")


        SCREEN.blit(NAME_TEXT, MENU_RECT)
        SCREEN.blit(LEVEL_TEXT, LEVEL_RECT)

        for button in [PLAY_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    cfg.GAME_SETTING.NAME = user_text
                    play()
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()

        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
    
            if event.type == pygame.KEYDOWN:
    
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
    
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
    
                # Unicode standard is used for string
                # formation
                elif event.key == pygame.K_RETURN:
                    cfg.GAME_SETTING.NAME = user_text
                    play()
    
                else:
                    user_text += event.unicode
            
        if active:
            color = color_active
        else:
            color = color_passive
            
        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(SCREEN, color, input_rect)
    
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        
        # render at position stated in arguments
        SCREEN.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)
        
        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG_JUNGLE, (0, 0))


        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(120).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(cfg.GAME_SETTING.WIDTH / 2, 200))

        NAME_BUTTON = Button(image=pygame.image.load(os.path.join(cfg.PATHS.ASSET_PATH, "Play Rect.png")), pos=(cfg.GAME_SETTING.WIDTH / 2, 500),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(os.path.join(cfg.PATHS.ASSET_PATH, "Options Rect.png")), pos=(cfg.GAME_SETTING.WIDTH / 2, 750),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(os.path.join(cfg.PATHS.ASSET_PATH, "Quit Rect.png")), pos=(cfg.GAME_SETTING.WIDTH / 2, 900),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

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
                    name_menu()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def score_menu():
    FIRST = True
    while True:
        SCREEN.blit(BG_SCORE, (0, 0))


        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MAIN_BUTTON = Button(image=pygame.image.load(os.path.join(cfg.PATHS.ASSET_PATH, "Play Rect.png")), pos=(cfg.GAME_SETTING.WIDTH / 2 - 300, 1000),
                             text_input="MENU", font=get_font(30), base_color="#d7fcd4",
                             hovering_color="White")
        REPLAY_BUTTON = Button(image=pygame.image.load(os.path.join(cfg.PATHS.ASSET_PATH, "Play Rect.png")),
                               pos=(cfg.GAME_SETTING.WIDTH / 2 + 300, 1000), text_input="REPLAY", font=get_font(30), base_color="#d7fcd4",
                               hovering_color="White")

        font = pygame.font.SysFont("Potta One", 60, 2)

        if FIRST:
            FIRST = False
            scores = get_best_score()
        
        for idx, score in enumerate(scores):
            SCREEN.blit(font.render(f"{score[1]}", True, (255, 255, 255)), (100, idx * 60 + 300))  # show score
            SCREEN.blit(font.render(f"{score[0]}", True, (255, 255, 255)), (300, idx * 60 + 250))  # show score
            
            

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

        SCREEN.blit(BG_JUNGLE, (0, 0))  # show background
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
            add_score(cfg.GAME_SETTING.NAME, int(game.fgame.player.point))
            score_menu()

        check_exit(game)

if __name__ == '__main__':
    main_menu()


#TODO change mode
#TODO save BDD
#TODO Display best score
#TODO Deploy
#TODO refactoring code
