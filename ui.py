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
        self.BACKGROUND = (0, 162, 232)
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 255, 0)
        self.RED = (255, 0, 0)

        # display
        self.SCREEN_SIZE = (640, 480)
        self.BOARD_POS = (100, 20) #8 by 8 board
        self.BOARD = (120, 40) #pieces
        self.BOARD_SIZE = 400
        self.SQUARE_SIZE = 50
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)

        # messages
        self.BLACK_LABEL_POS = (25, self.SCREEN_SIZE[1] / 4)
        self.WHITE_LABEL_POS = (540, self.SCREEN_SIZE[1] / 4)
        self.font = pygame.font.SysFont("Times New Roman", 50)
        self.scoreFont = pygame.font.SysFont("Serif", 58)

        # image files
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
            self.screen.fill(self.BACKGROUND)

            title_fnt = pygame.font.SysFont("Times New Roman", 150)
            title = title_fnt.render("Othello", True, self.WHITE)
            title_pos = title.get_rect(centerx=self.screen.get_width() / 2, centery=160)
            start_txt = self.font.render("Press Start", True, self.WHITE)
            start_pos = start_txt.get_rect(centerx=self.screen.get_width() / 2, centery=280)
            self.screen.blit(title, title_pos)
            self.screen.blit(start_txt, start_pos)

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
        self.background.fill(self.BACKGROUND)
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

    def put_stone(self, pos, color):
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
            pass
        x = pos[0] * self.SQUARE_SIZE + self.BOARD[0]
        y = pos[1] * self.SQUARE_SIZE + self.BOARD[1]
        self.screen.blit(img, (x, y), img.get_rect())
        pygame.display.flip()

    def clear_square(self, pos):
        """ Puts in the given position a background image, to simulate that the
        piece was removed.
        """
        # flip orientation
        pos = (pos[1], pos[0])
        x = pos[0] * self.SQUARE_SIZE + self.BOARD[0]
        y = pos[1] * self.SQUARE_SIZE + self.BOARD[1]
        self.screen.blit(self.clear_img, (x, y), self.clear_img.get_rect())
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
        # wait user to close window
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                break
