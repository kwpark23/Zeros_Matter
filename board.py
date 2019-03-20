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
        
    def __getitem__(self, row: int, column: int) -> int:
        return self.board[row][column]
    
    def lookup(self, row: int, column: int, color: int) -> List[Tuple(int, int)]:
        """Returns the possible positions that there exists at least one
        straight (horizontal, vertical, or diagonal) line between the
        piece specified by (row, column, color) and another piece of
        the same color.

        """
        if color == BLACK:
            other = WHITE
        else:
            other = BLACK

        places = []

        # invalid rows and columns
        if row < 0 or row > 7 or column < 0 or column > 7:
            return places

    # For each direction search for possible positions to put a piece.

        # north
        new_row = row - 1
        if new_row >= 0 and self.board[new_row][column] == other:
            new_row = new_row - 1
            while new_row >= 0 and self.board[new_row][column] == other:
                new_row = new_row - 1
            if new_row >= 0 and self.board[new_row][column] == 0:
                places = places + [(new_row, column)]

        # northeast
        new_row = row - 1
        new_col = column + 1
        if new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == other:
            new_row = new_row - 1
            new_col = new_col + 1
            while new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == other:
                new_row = new_row - 1
                new_col = new_col + 1
            if new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == 0:
                places = places + [(new_row, new_col)]

        # east
        new_col = column + 1
        if new_col < 8 and self.board[row][new_col] == other:
            new_col = new_col + 1
            while new_col < 8 and self.board[row][new_col] == other:
                new_col = new_col + 1
            if new_col < 8 and self.board[row][new_col] == 0:
                places = places + [(row, new_col)]

        # southeast
        new_row = row + 1
        new_col = column + 1
        if new_row < 8 and new_col < 8 and self.board[new_row][new_col] == other:
            new_row = new_row + 1
            new_col = new_col + 1
            while new_row < 8 and new_col < 8 and self.board[new_row][new_col] == other:
                new_row = new_row + 1
                new_col = new_col + 1
            if new_row < 8 and new_col < 8 and self.board[new_row][new_col] == 0:
                places = places + [(new_row, new_col)]

        # south
        new_row = row + 1
        if new_row < 8 and self.board[new_row][column] == other:
            new_row = new_row + 1
            while new_row < 8 and self.board[new_row][column] == other:
                new_row = new_row + 1
            if new_row < 8 and self.board[new_row][column] == 0:
                places = places + [(new_row, column)]

        # southwest
        new_row = row + 1
        new_col = column - 1
        if new_row < 8 and new_col >= 0 and self.board[new_row][new_col] == other:
            new_row = new_row + 1
            new_col = new_col - 1
            while new_row < 8 and new_col >= 0 and self.board[new_row][new_col] == other:
                new_row = new_row + 1
                new_col = new_col - 1
            if new_row < 8 and new_col >= 0 and self.board[new_row][new_col] == 0:
                places = places + [(new_row, new_col)]

        # west
        new_col = column - 1
        if new_col >= 0 and self.board[row][new_col] == other:
            new_col = new_col - 1
            while new_col >= 0 and self.board[row][new_col] == other:
                new_col = new_col - 1
            if new_col >= 0 and self.board[row][new_col] == 0:
                places = places + [(row, new_col)]

        # northwest
        new_row = row - 1
        new_col = column - 1
        if new_row >= 0 and new_col >= 0 and self.board[new_row][new_col] == other:
            new_row = new_row - 1
            new_col = new_col - 1
            while new_row >= 0 and new_col >= 0 and self.board[new_row][new_col] == other:
                new_row = new_row - 1
                new_col = new_col - 1
            if new_row >= 0 and new_col >= 0 and self.board[new_row][new_col] == 0:
                places = places + [(new_row, new_col)]

        return places

    def get_valid_moves(self, color: int) -> List[Tuple(int, int)]:
        """Get the available positions to put a piece of the given color. For
        each piece of the given color we search its neighbours,
        searching for pieces of the other color to determine if is
        possible to make a move. This method must be called before
        apply_move.

        """
        places = []

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == color:
                    places = places + self.lookup(i, j, color)

        places = list(set(places))
        self.valid_moves = places
        return places

