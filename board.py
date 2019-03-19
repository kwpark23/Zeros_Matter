EMPTY = 0
BLACK = 1
WHITE = 2
class Board:

    """ Rules of the game """

    def __init__(self):
        self.board = [[EMPTY] * 8 for n in range(8)]
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        self.board[3][3] = WHITE
        self.board[4][4] = WHITE
        self.valid_moves = []
