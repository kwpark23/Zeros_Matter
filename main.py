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
        
    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            if self.board.game_ended():
                blacks, whites, empty = self.board.count_tiles()
                if blacks > whites:
                    winner = BLACK
                elif whites > blacks:
                    winner = WHITE
                else:
                    winner = None
                break
            self.now_playing.get_current_board(self.board)
            if self.board.find_valid_moves(self.now_playing.color) != []:
                score, self.board = self.now_playing.get_move()
                whites, blacks, empty = self.board.count_tiles()
                self.gui.update(self.board.board, blacks, whites, self.now_playing.color)
            self.now_playing, self.other_player = self.other_player, self.now_playing
        self.gui.show_winner(winner)
        pygame.time.wait(3000)
        self.restart_flipsies()

    def restart_flipsies(self):
        self.board = board.Board()
        self.get_options()
        self.run()

        
def main():
    game = Flipsies()
    game.run()


if __name__ == '__main__':
    main()
     
