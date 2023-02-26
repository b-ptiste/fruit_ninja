import pygame
import cv2
import os
import time
import mediapipe as mp
from src.FruitAnimation.fruitgame import FruitGame
from utils.constant import WIDTH, HIGH, IMAGE_PATH


class GameLauncher:
    def __init__(self):
        # set game
        pygame.init()
        pygame.display.set_caption("Own_First_Game")
        self.screen = pygame.display.set_mode((WIDTH, HIGH))

        # create back-ground
        self.background = pygame.image.load(os.path.join(IMAGE_PATH, "background_jungle.jpg"))

        # create game
        self.fgame = FruitGame()

        self.cap = cv2.VideoCapture(0)
        mp_hands = mp.solutions.hands
        self.hands = mp_hands.Hands(True)

        self.currTime = time.time()
        self.startTime = time.time()
        self.begin_time_multiplicative = time.time()
        self.begin_time_speed = time.time()
        self.all_explosion = pygame.sprite.Group()
        self.bomb_collusion = False











