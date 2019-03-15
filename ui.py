import pygame
import sys
import time
import os
from __future__ import annotations
from typing import Tuple 
from pygame.locals import *
from const import HUMAN, BLACK, WHITE

class Gui:
    """
    This class is responsible for all the graphics of the game. Instantiate
    it as early as possible.
    
    === Attributes ===
    Colours: BLACK, WHITE, TEAL
    Display: SCREEN_SIZE, BOARD_POS, BOARD, BOARD_SIZE, SQUARE_SIZE, screen
    Messages: BLACK_LABEL_POS, WHITE_LABEL_POS, font, scoreFont
    Images: board_img, black_img, white_img, clear_img
    """

    def __init__(self):
        pygame.init()

        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.TEAL = (112, 174, 199)

        # Display
        self.SCREEN_SIZE = (640, 480)
        self.BOARD_POS = (100, 20) #8 by 8 board
        self.BOARD = (120, 40) #pieces
        self.BOARD_SIZE = 400
        self.SQUARE_SIZE = 50
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)

        # Messages
        self.BLACK_LABEL_POS = (25, self.SCREEN_SIZE[1] / 4)
        self.WHITE_LABEL_POS = (540, self.SCREEN_SIZE[1] / 4)
        self.font = pygame.font.SysFont("Avenir", 50)
        self.scoreFont = pygame.font.SysFont("Avenir", 58)

        # Image files
        self.board_img = pygame.image.load(os.path.join("images", "board.bmp")).convert()
        self.black_img = pygame.image.load(os.path.join("images", "black.bmp")).convert()
        self.white_img = pygame.image.load(os.path.join("images", "white.bmp")).convert()
        self.clear_img = pygame.image.load(os.path.join("images", "blank.bmp")).convert()
