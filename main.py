import pygame
import ui
import player
import board

from const import WHITE, BLACK


class Main:
    """
    Game main class.
    """

    def __init__(self) -> None:
        """
        Initialize options and game screen, and sets up two white
        stones and two black stones in the middle of the board.
        """

        # start
        self.gui = ui.Gui()
        self.board = board.Board()
        self.get_options()
