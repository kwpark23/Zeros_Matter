import pygame
import ui
import player
import board
 
 
BLACK = 1
WHITE = 2
 
 
class Flipsies:
    """Game main class."""
 
    def __init__(self):
        """ Show options screen and start game modules"""
        # start
        self.gui = ui.Gui()
        self.board = board.Board()
        self.get_options()

    def get_options(self):
        # set up players
        player1, player2 = self.gui.show_options()
        if player1 == "human":
            self.now_playing = player.Human(self.gui, BLACK)

        if player2 == "human":
            self.other_player = player.Human(self.gui, WHITE)

        self.gui.show_game()
        self.gui.update(self.board.board, 2, 2, self.now_playing.color)

    def restart_flipsies(self):
        self.board = board.Board()
        self.get_options()
        self.run()

        
def main():
    game = Flipsies()
    game.run()


if __name__ == '__main__':
    main()
     
