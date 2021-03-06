from __future__ import annotations
import pygame
import sys
import time
import os
from pygame.locals import *
from typing import *
from const import BLACK, WHITE

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
        
    def title_screen(self) -> Tuple(str, str):
        """
        Displays title screen containing title, 2 buttons, and logo.
        When you click "PLAY", this method returns the types of Player 1
        and Player 2 (as of now, both are humans).
        """

        while True:
            # Logo
            pygame.draw.rect(self.screen, self.theme, pygame.Rect(20, 20, 610, 430), 10)
            pygame.draw.circle(self.screen, self.white, (340, 270), 30, 0)
            pygame.draw.circle(self.screen, self.white, (300, 250), 33, 3)
            pygame.draw.circle(self.screen, self.black, (300, 250), 30, 0)

            # Title
            title_fnt = pygame.font.SysFont("Avenir", 150)
            title = title_fnt.render("Flipsies", True, self.theme)
            title_pos = title.get_rect(centerx=self.screen.get_width() / 2, centery=160)

            # Play button
            play_fnt = pygame.font.SysFont("Avenir", 80)
            play_txt = play_fnt.render("PLAY", True, self.theme)
            play_pos = play_txt.get_rect(centerx=self.screen.get_width() / 2, centery=350)

            # Instructions label
            ins_fnt = pygame.font.SysFont("Avenir", 50)
            ins_txt = ins_fnt.render("How to play", True, (97, 148, 175))
            ins_pos = start_txt.get_rect(centerx=self.screen.get_width() / 2.3, centery=430)

            # Add all to screen
            self.screen.blit(title, title_pos)
            self.screen.blit(play_txt, play_pos)
            self.screen.blit(ins_txt, ins_pos)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()

            pygame.display.flip()
            
    def show_game(self) -> None:
        """
        Creates board and adds 4 pieces in the initial positions.
        Game stays on this screen until a player wins.
        """
        
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill(self.theme)
        self.screen.blit(self.background, (0, 0), self.background.get_rect())
        self.screen.blit(self.board_img, self.board_pos, self.board_img.get_rect())
        
        # Place 2 white stones and 2 black stones in the center of the board
        self.put_stone((3, 3), 2)
        self.put_stone((4, 4), 2)
        self.put_stone((3, 4), 1)
        self.put_stone((4, 3), 1)
        
        pygame.display.flip()
       
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
            
    def show_score(self, black_score: int, white_score: int) -> None:
        """
        Returns the current score on the screen.
        """
        
        font = pygame.font.SysFont("ariel", 30)
        msg_white = font.render("Player 1", True, self.white)
        msg_black = font.render("Player 2", True, self.black)
        display_black = self.scoreFont.render(black_score, True, self.black, self.theme)
        display_white = self.scoreFont.render(white_score, True, self.white, self.theme)

        self.screen.blit(msg_white, (self.white_label_pos[0], self.white_label_pos[1] + 15))
        self.screen.blit(msg_black, (self.black_label_pos[0], self.black_label_pos[1] + 15))
        self.screen.blit(display_black, (self.black_label_pos[0], self.black_label_pos[1] + 40))
        self.screen.blit(display_white, (self.white_label_pos[0], self.white_label_pos[1] + 40))
        
    def put_stone(self, pos: Tuple[int, int], player_color: int) -> None:
        """
        Puts a piece of the given color in the given position. 
        """
        
        if pos == None:
            return
        
        pos = (pos[1], pos[0])

        if player_color == player1:
            img = self.black_img
        else:
            img = self.white_img
            
        x = pos[0] * self.square_size + self.board[0]
        y = pos[1] * self.square_size + self.board[1]
        
        # Place a stone
        self.screen.blit(img, (x, y), img.get_rect())
        pygame.display.flip()
       
    def update_screen(self, board: List[List[int]], black: float, white: float) -> None:
        """Display updated stone placement and scores of both players on screen.
        """
        
        # Place all the stones
        for i in range(8):
            for j in range(8):
                if board[i][j] != 0:
                    self.put_stone((i, j), board[i][j])

        # Converts float to integer values
        black_score = '%02d ' % int(black)
        white_score = '%02d ' % int(white)
        
        self.show_score(black_score, white_score)
        pygame.display.flip()
        
    def show_winner(self, player: int) -> None:
        """
        Shows winner of the game. If there is no winner,
        it defaults to a tie.
        """
        
        self.screen.fill(self.theme)
        font = pygame.font.SysFont("ariel", 80)
        if player == WHITE:
            msg = font.render("WHITE WINS!", True, self.black)
        elif player == BLACK:
            msg = font.render("BLACK WINS", True, self.black)
        else:
            msg = font.render("Tie!", True, self.white)
           
        self.screen.blit(msg, msg.get_rect(centerx=self.screen.get_width()/2, centery=120))
        pygame.display.flip()
        
    def quit_game(self) -> None:
        """
        When user closes the window, the system quits the game.
        """

        # Wait for user to close window
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                break
