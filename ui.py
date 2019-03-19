from __future__ import annotations
import pygame
import sys
import time
import os
from pygame.locals import *
from typing import *

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
       
    def get_mouse_input(self) -> None:
        """ Returns the location of mouse clicks.
        """
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()

                    # Ignores if clicked outside of the board
                    if mouse_x > self.board_size + self.board[0] or \
                       mouse_x < self.board[0] or \
                       mouse_y > self.board_size + self.board[1] or \
                       mouse_y < self.board[1]:
                        continue

                    # Finds the location of click
                    position = ((mouse_x - self.board[0]) // self.square_size), \
                               ((mouse_y - self.board[1]) // self.square_size)

                    # Flips orientation
                    position = (position[1], position[0])
                    return position

                elif event.type == QUIT:
                    sys.exit(0)

            time.sleep(.05)
