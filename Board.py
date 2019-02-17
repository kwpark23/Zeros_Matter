FREE = 0
WHITE = 1
BLACK = 2


class Board:

    """ Grid for which game will be played on """

    def __init__(self):

        """ Creates the board """

        # creates an 8x8 game board using a list of lists
        self.grid = [[FREE]*8 for n in range(8)]
        self.grid[3][4] = BLACK
        self.grid[4][3] = BLACK
        self.grid[3][3] = WHITE
        self.grid[4][4] = WHITE
        self.logical_moves = []

    def get_placeholder(self, row, col):
        
        """ return value on board at specific row / col """
        
        return self.grid[row][col]
