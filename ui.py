from __future__ import annotations
import pygame
import sys
import time
import os
from pygame.locals import *
from typing import Tuple

class Gui:
    """
    Creates the entire graphical component of the game.
    
    === Attributes ===
    Colours: black, white, theme
    Display: screen_size, board_size, square_size, board_pos, board, screen
    Messages: black_label_pos, white_label_pos, font, score_font
    Images: board_img, black_img, white_img
    """
    
    def __init__(self) -> None:
        
        pygame.init()
        
        # Colours
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.theme = (112, 174, 199)

        # Display
        self.screen_size = (640, 480)
        self.board_pos = (100, 20)
        self.board = (120, 40) 
        self.board_size = 400
        self.square_size = 50
        self.screen = pygame.display.set_mode(self.screen_size)

        # Messages
        self.black_label_pos = (25, self.screen_size[1] / 4)
        self.white_label_pos = (540, self.screen_size[1] / 4)
        self.font = pygame.font.SysFont("Avenir", 50)
        self.scoreFont = pygame.font.SysFont("Avenir", 58)

        # Images
        self.board_img = pygame.image.load(os.path.join("images", "board.bmp")).convert()
        self.black_img = pygame.image.load(os.path.join("images", "black.bmp")).convert()
        self.white_img = pygame.image.load(os.path.join("images", "white.bmp")).convert()
