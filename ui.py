import pygame
import sys
import time
import os
from __future__ import annotations
from typing import Tuple 
from pygame.locals import *
from const import HUMAN, WHITE, BLACK


class Gui:
    """
    This class is responsible for all the graphics of the game. Instantiate it as early as possible.
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

    def show_options(self):
        """ Shows game options screen and returns chosen options
        """
        # default values
        player1 = HUMAN
        player2 = HUMAN

        while True:
            pygame.draw.rect(self.screen, self.TEAL, pygame.Rect(20, 20, 610, 430), 10)
            pygame.draw.circle(self.screen, self.WHITE, (340, 270), 30, 0)
            pygame.draw.circle(self.screen, self.WHITE, (300, 250), 33, 3)
            pygame.draw.circle(self.screen, self.BLACK, (300, 250), 30, 0)

            # Title
            title_fnt = pygame.font.SysFont("Avenir", 150)
            title = title_fnt.render("Flipsies", True, self.TEAL)
            title_pos = title.get_rect(centerx=self.screen.get_width() / 2, centery=160)

            # Start Button
            start_fnt = pygame.font.SysFont("Avenir", 80)
            start_txt = start_fnt.render("PLAY", True, self.TEAL)
            start_pos = start_txt.get_rect(centerx=self.screen.get_width() / 2, centery=350)

            # Instructions label
            ins_fnt = pygame.font.SysFont("Avenir", 50)
            ins_txt = ins_fnt.render("How to play", True, (97, 148, 175))
            ins_pos = start_txt.get_rect(centerx=self.screen.get_width() / 2.3, centery=430)

            # Add all to screen
            self.screen.blit(title, title_pos)
            self.screen.blit(start_txt, start_pos)
            self.screen.blit(ins_txt, ins_pos)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    if start_pos.collidepoint(mouse_x, mouse_y):
                        return player1, player2

            pygame.display.flip()

    def show_winner(self, player_color):
        self.screen.fill(self.YELLOW)
        font = pygame.font.SysFont("ariel", 80)
        if player_color == WHITE:
            msg = font.render("WHITE WINS!", True, self.BLACK)
        elif player_color == BLACK:
            msg = font.render("BLACK WINS", True, self.BLACK)
        else:
            msg = font.render("Tie !", True, self.WHITE)
        self.screen.blit(msg, msg.get_rect(centerx=self.screen.get_width() / 2, centery=120))
        pygame.display.flip()

    def show_game(self):
        """ Game screen. """

        # draws initial screen
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill(self.TEAL)
        self.score_size = 50
        self.score1 = pygame.Surface((self.score_size, self.score_size))
        self.score2 = pygame.Surface((self.score_size, self.score_size))
        self.screen.blit(self.background, (0, 0), self.background.get_rect())
        self.screen.blit(self.board_img, self.BOARD_POS, self.board_img.get_rect())
        self.put_stone((3, 3), WHITE)
        self.put_stone((4, 4), WHITE)
        self.put_stone((3, 4), BLACK)
        self.put_stone((4, 3), BLACK)
        pygame.display.flip()

    def put_stone(self, pos: tuple, color):
        """ draws piece with given position and color """
        if pos == None:
            return

        # flip orientation (because xy screen orientation)
        pos = (pos[1], pos[0])

        if color == BLACK:
            img = self.black_img
        elif color == WHITE:
            img = self.white_img
        else:
            img = self.tip_img
        x = pos[0] * self.SQUARE_SIZE + self.BOARD[0]
        y = pos[1] * self.SQUARE_SIZE + self.BOARD[1]
        self.screen.blit(img, (x, y), img.get_rect())
        pygame.display.flip()

    def get_mouse_input(self):
        """ Get place clicked by mouse
        """
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()

                    # click was out of board, ignores
                    if mouse_x > self.BOARD_SIZE + self.BOARD[0] or \
                       mouse_x < self.BOARD[0] or \
                       mouse_y > self.BOARD_SIZE + self.BOARD[1] or \
                       mouse_y < self.BOARD[1]:
                        continue

                    # find place
                    position = ((mouse_x - self.BOARD[0]) // self.SQUARE_SIZE), \
                               ((mouse_y - self.BOARD[1]) // self.SQUARE_SIZE)
                    # flip orientation
                    position = (position[1], position[0])
                    return position

                elif event.type == QUIT:
                    sys.exit(0)

            time.sleep(.05)

    def update(self, board, blacks, whites, current_player_color):
        """Updates screen
        """
        for i in range(8):
            for j in range(8):
                if board[i][j] != 0:
                    self.put_stone((i, j), board[i][j])

        blacks_str = '%02d ' % int(blacks)
        whites_str = '%02d ' % int(whites)
        self.showScore(blacks_str, whites_str, current_player_color)
        pygame.display.flip()

    def showScore(self, blackStr, whiteStr, current_player_color):
        font = pygame.font.SysFont("ariel", 30)
        msgw = font.render("Player 1", True, self.WHITE)
        msgb = font.render("Player 2", True, self.BLACK)
        self.screen.blit(msgw, (self.WHITE_LABEL_POS[0], self.WHITE_LABEL_POS[1] + 15))
        self.screen.blit(msgb, (self.BLACK_LABEL_POS[0], self.BLACK_LABEL_POS[1] + 15))


        blackscore = self.scoreFont.render(blackStr, True, self.BLACK, self.TEAL)
        whitescore = self.scoreFont.render(whiteStr, True, self.WHITE, self.TEAL)
        self.screen.blit(blackscore, (self.BLACK_LABEL_POS[0], self.BLACK_LABEL_POS[1] + 40))
        self.screen.blit(whitescore, (self.WHITE_LABEL_POS[0], self.WHITE_LABEL_POS[1] + 40))

    def wait_quit(self):
        # wait user to close window
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                break
