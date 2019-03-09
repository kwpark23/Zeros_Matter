import pygame
import sys
import time
import os
from pygame.locals import *


HUMAN = "human"
BLACK = 1
WHITE = 2


class Gui:
    def __init__(self):
        """ Initializes graphics. """

        pygame.init()

        # colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.TEAL = (112, 174, 199)

        # display
        self.SCREEN_SIZE = (640, 480)
        self.BOARD_POS = (100, 20)  #8 by 8 board
        self.BOARD = (120, 40) #pieces
        self.BOARD_SIZE = 400
        self.SQUARE_SIZE = 50
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)

        # messages
        self.BLACK_LABEL_POS = (25, self.SCREEN_SIZE[1] / 4)
        self.WHITE_LABEL_POS = (540, self.SCREEN_SIZE[1] / 4)
        self.font = pygame.font.SysFont("Avenir", 50)
        self.scoreFont = pygame.font.SysFont("Avenir", 58)

        # image files
        self.board_img = pygame.image.load(os.path.join("images", "board.bmp")).convert()
        self.black_img = pygame.image.load(os.path.join("images", "black.bmp")).convert()
        self.white_img = pygame.image.load(os.path.join("images", "white.bmp")).convert()
        self.clear_img = pygame.image.load(os.path.join("images", "blank.bmp")).convert()

    def show_options(self):
        """
        Shows game options screen and returns chosen options
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
            
    def update(self, board, blacks, whites, current_player_color):
        """Updates screen with positions of new tiles after a move
        has been made. Also calls to update score of current_player_color.
    
        """
        
        for x in range(8):
            for y in range(8):
                if board[x][y] != 0:
                    self.put_stone((x, y), board[x][y])

        blacks_str = '%02d ' % int(blacks)
        whites_str = '%02d ' % int(whites)
        self.show_score(blacks_str, whites_str, current_player_color)
        pygame.display.flip()
       
    def show_score(self, blackStr, whiteStr, current_player_color):
        """Updates the score board of current_player_color after a
        move has been placed.

        """
        
        black_background = self.BACKGROUND
        white_background = self.BACKGROUND


        font = pygame.font.SysFont("ariel", 30)
        msgw = font.render("White", True, self.WHITE)
        msgb = font.render("Black", True, self.BLACK)
        self.screen.blit(msgw, (self.WHITE_LABEL_POS[0], self.WHITE_LABEL_POS[1] + 15))
        self.screen.blit(msgb, (self.BLACK_LABEL_POS[0], self.BLACK_LABEL_POS[1] + 15))


        text = self.scoreFont.render(blackStr, True, self.BLACK, black_background)
        text2 = self.scoreFont.render(whiteStr, True, self.WHITE, white_background)
        self.screen.blit(text, (self.BLACK_LABEL_POS[0], self.BLACK_LABEL_POS[1] + 40))
        self.screen.blit(text2, (self.WHITE_LABEL_POS[0], self.WHITE_LABEL_POS[1] + 40))
        
    def wait_quit(self):
        """
        Waits until a player has chosen to quit, then
        quits game.
        """

        # wait user to close window
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                break
