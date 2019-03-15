import pygame
import ui
import player
import board

from const import WHITE, BLACK


class Othello:
    """
    Game main class.
    """

    def __init__(self):
        """
        Initialize options and game screen, and sets up two white
        stones and two black stones in the middle of the board.
        """

        # start
        self.gui = ui.Gui()
        self.board = board.Board()
        self.get_options()

    def get_options(self):
        """
        Sets up two players who will participate in the game.
        """
        # set up players
        player1, player2 = self.gui.show_options()
        if player1 == "human":
            self.now_playing = player.Human(self.gui, BLACK)

        if player2 == "human":
            self.other_player = player.Human(self.gui, WHITE)

        self.gui.show_game()
        self.gui.update(self.board.board, 2, 2, self.now_playing.color)

    def run(self):
        """
        Runs the game.
        """
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            if self.board.game_ended():
                whites, blacks, empty = self.board.count_stones()
                if whites > blacks:
                    winner = WHITE
                elif blacks > whites:
                    winner = BLACK
                else:
                    winner = None
                break
            self.now_playing.get_current_board(self.board)
            if self.board.get_valid_moves(self.now_playing.color) != []:
                score, self.board = self.now_playing.get_move()
                whites, blacks, empty = self.board.count_stones()
                self.gui.update(self.board.board, blacks, whites, self.now_playing.color)
            self.now_playing, self.other_player = self.other_player, self.now_playing
        self.gui.show_winner(winner)
        pygame.time.wait(3000)
        self.restart()

    def restart(self):
        """
        Reinitialize the board for a new game.
        """
        self.board = board.Board()
        self.get_options()
        self.run()


def main():
    game = Othello()
    game.run()


if __name__ == '__main__':
    main()
