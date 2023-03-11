import time
import uuid
import pygame
import random

from src.database.dataBase_sql import add_score
from src.gameLauncher import GameLauncher
from src.FruitAnimation.explose import Explose
from src.screens import score_menu
from utils.config import cfg
from utils.function import move_player, update_bonus, check_exit


def screen(SCREEN):
    game = GameLauncher()

    running = True
    font = pygame.font.SysFont("Potta One", 60, 2)

    while running:
        SCREEN.blit(cfg.IMAGES.BG_JUNGLE[0], (0, 0))  # show background
        SCREEN.blit(game.fgame.player.image, game.fgame.player.rect)  # show kunai
        score_text = font.render(
            f"Score : {game.fgame.player.point}", True, (255, 255, 255)
        )  # show score
        SCREEN.blit(score_text, (40, 20))

        for i in range(4):
            if i > game.bomb_collusion:
                SCREEN.blit(
                    cfg.IMAGES.CROSS_GREEN[0], (cfg.GAME_SETTING.WIDTH - i * 150, 100)
                )
            else:
                SCREEN.blit(
                    cfg.IMAGES.CROSS_RED[0], (cfg.GAME_SETTING.WIDTH - i * 150, 100)
                )

        # show remaining time
        time_text = font.render(
            f"Temps : {round(time.time() - game.startTime - game.fgame.bonus_freeze, 2)}",
            True,
            (255, 255, 255),
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
                    game.fgame.player.point += fruit.point * (
                        1 + game.fgame.bonus_multiplicative
                    )
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
        cond_stop = (game.bomb_collusion >= 3) or (
            time.time() - game.startTime - game.fgame.bonus_freeze
            > cfg.GAME_SETTING.END_TIME
        )
        if cond_stop:
            u_id = str(uuid.uuid4())
            add_score(
                cfg.GAME_SETTING.NAME,
                int(game.fgame.player.point),
                u_id,
                cfg.GAME_SETTING.HOST,
                cfg.GAME_SETTING.USER,
                cfg.GAME_SETTING.PASSWORD,
                cfg.GAME_SETTING.DATABASE,
            )
            score_menu.screen(
                cfg.GAME_SETTING.NAME, int(game.fgame.player.point), u_id, SCREEN
            )

        check_exit()
