import pygame
from src.gameLauncher import GameLauncher
import time
import random
from utils.constant import WIDTH
from utils.function import move_player, check_collusion, update_bonus, check_end

# create game
game = GameLauncher()

running = True
font = pygame.font.SysFont("Potta One", 60, 2)

while running:

    game.screen.blit(game.background, (0, 0))  # show background
    game.screen.blit(game.fgame.player.image, game.fgame.player.rect)  # show kunai
    score_text = font.render(f"Score : {game.fgame.player.point}", True, (255, 255, 255))  # show score
    game.screen.blit(score_text, (40, 20))

    # show remaining time
    time_text = font.render(f"Temps : {round(time.time() - game.startTime - 2 * game.fgame.bonus_freeze, 2)}",
                            True,
                            (255, 255, 255)
                            )
    game.screen.blit(time_text, (WIDTH - 400, 20))

    # creation des fruits
    with_bonus = random.randint(1, 50)
    if time.time() - game.currTime > 1 - 0.75 * game.fgame.bonus_speed:
        game.fgame.launch_fruit()
        game.currTime = time.time()
    if with_bonus == 1:
        game.fgame.launch_fruit(True)

    game.fgame.move()  # animation des fruits
    game.fgame.all_fruit.draw(game.screen)  # afficher les fruits

    # position du doigt
    move_player(game)
    check_collusion(game)
    game.all_explosion.draw(game.screen)
    update_bonus(game, font)

    game.fgame.all_fruit.draw(game.screen)
    pygame.display.flip()
    # screen update

    check_end(game)

#TODO add 3 lifes
#TODO entry menu
#TODO exit menu
#TODO refactoring code
