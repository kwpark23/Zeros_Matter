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
        
        
    def get_options(self) -> None:
        """
        Sets up two players who will participate in the game.
        """
        # set up players
        player1, player2 = self.gui.title_screen()
        if player1 == "human":
            self.now_playing = player.Human(self.gui, BLACK)

        if player2 == "human":
            self.other_player = player.Human(self.gui, WHITE)

        self.gui.show_game()
        self.gui.update_screen(self.board.board, 2, 2, self.now_playing.color)
