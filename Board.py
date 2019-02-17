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
    
    def count_tiles(self):

    """ Create and return a list of numbers that contains the amount of
    white, black and free tiles on the board, in this order.
    """
    
    space_count = []
    black = 0
    white = 0
    free = 0
    for row in range(8):
        for col in range(8): # Traversal of game board 
            if self.grid[row][col] == black:
                black += 1
            elif self.grid[row][col] == white:
                white += 1
            else:
                free += 1
    space_count.extend(white, black, free) # Add all totals to a list 
    return space_count
    
    def print_grid(self):
        
        """ Prints grid """
        
        for row in range(8):
            print(row, ' |', end=' ')
            for col in range(8):
                if self.gird[row][col] == WHITE:
                    print('W', end=' ')
                elif self.grid[row][col] == BLACK:
                    print('B', end=' ')
                else:
                    print(' ', end=' ')
                print('|', end=' ')
            print()
