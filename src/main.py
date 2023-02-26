import pygame
from jeu import Game
import mediapipe as mp
import cv2
import time
import random

pygame.init()

# generer la fenetre du jeu

# on peut aussi mettre une icone
pygame.display.set_caption("Own_First_Game")
screen = pygame.display.set_mode((628, 417))

# arrière plan
background = pygame.image.load("image/fond_jungle.jpg")

# charger le jeu

game = Game()

running = True

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(True)


cTime = time.time()
bTime = time.time()

# texte quand il y a un bonus
font = pygame.font.SysFont("Potta One", 30, 2)

text_bonus_speed = font.render("BONUS fruit", True, (0, 0, 0))
text_bonus_multiplicatif = font.render("BONUS Score x2", True, (0, 0, 0))
text_bonus_freeze = font.render("BONUS + 2 Temps", True, (0, 0, 0))

while running:
    # appliquer le background
    screen.blit(background, (0, 0))

    # appliquer le joueur
    screen.blit(game.player.kunai, game.player.rect1)
    screen.blit(game.player.image, game.player.rect)

    # afficher le score

    score_text = font.render(f"Score : {game.player.point}", True, (0, 0, 0))
    screen.blit(score_text, (20, 20))

    # afficher le temps restant
    time_text = font.render(f"Temps : {round(time.time()-bTime-2*game.bonus_freeze,2)}", True, (0, 0, 0))
    screen.blit(time_text, (450, 20))

    # creation des fruits
    with_bonus = random.randint(1, 100)
    if time.time() - cTime > 1 - 0.75 * game.bonus_speed:
        game.launch_fruit()
        cTime = time.time()
    if with_bonus == 1:
        game.launch_fruit(True)

    # animation des fruits
    game.move()
    # afficher les fruits

    game.all_fruit.draw(screen)

    # si le joueur ferme cette fenêtre
    # dans pygame.event.get() on a une liste d'évemenents

    # position du doigt
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            for index, lm in enumerate(handLms.landmark):
                if index == 9:
                    h = 417
                    w = 618

                    cx, cy = int((1-lm.x) * w), int(lm.y * h)
    else:
        cx, cy = game.player.rect1.x, game.player.rect1.y
    game.player.move(cx, cy)
    for fruit in game.all_fruit.sprites():

        if game.check_collision(game.player, fruit):
            if fruit.bonus is None:
                game.player.point += fruit.point * (1 + game.bonus_multiplicatif)
            elif fruit.bonus == "banane":
                game.bonus_multiplicatif = True
                begin_time_multiplicatif = time.time()
            elif fruit.bonus == "banane_glace":
                game.bonus_freeze += 1
            elif fruit.bonus == "piment":
                game.bonus_speed = True
                begin_time_speed = time.time()
            game.all_fruit.remove(fruit)

    # on arrête les bonus
    if game.bonus_speed:
        if time.time() - begin_time_speed < 2:
            screen.blit(text_bonus_speed, (220, 200))
        if time.time()-begin_time_speed > 10:
            game.bonus_speed = False
    if game.bonus_multiplicatif:
        if time.time() - begin_time_multiplicatif < 2:
            screen.blit(text_bonus_multiplicatif, (220, 220))
        if time.time()-begin_time_multiplicatif > 10:
            game.bonus_multiplicatif = False

    game.all_fruit.draw(screen)

    # mettre à jour l'écran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")

    if time.time()-bTime-2*game.bonus_freeze > 60:
        running = False
        print(f"Le score est de {game.player.point}")
        pygame.quit()
