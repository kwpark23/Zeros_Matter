import pygame
import ui
import player
import board
 
 
BLACK = 1
WHITE = 2
 
 
class Main:
    """Game main class."""
 
    def __init__(self):
        """ Show options screen and start game modules"""
        # start
        self.gui = ui.Gui()
        self.board = board.Board()
        self.get_options()

    def restart_flipsies(self):
        self.board = board.Board()
        self.get_options()
        self.run()
