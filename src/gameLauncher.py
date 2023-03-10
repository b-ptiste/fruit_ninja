import pygame
import cv2
import os
import time
import mediapipe as mp
from src.FruitAnimation.fruitgame import FruitGame


class GameLauncher:
    def __init__(self):
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
        self.bomb_collusion = 0
