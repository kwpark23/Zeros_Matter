from const import BLACK, WHITE, EMPTY, NORTH, NORTHWEST, \
    NORTHEAST, WEST, EAST, SOUTHWEST, SOUTH, SOUTHEAST

class Board:

    """ Rules of the game """

    def __init__(self):
        self.board = [[EMPTY] * 8 for n in range(8)]
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        self.board[3][3] = WHITE
        self.board[4][4] = WHITE
        self.valid_moves = []

    def __getitem__(self, i, j):
        return self.board[i][j]

    def get_valid_moves(self, color):
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

    def apply_move(self, move, color):
        """ Determine if the move is correct and apply the changes in the game.
        """
        if move in self.valid_moves:
            self.board[move[0]][move[1]] = color
            for i in range(1, 9):
                self.flip(i, move, color)

    def flip(self, direction, position, color):
        """ Flips the pieces of the given color in the given direction
        (1=North,2=Northeast...) from position. """
        row_inc = 0
        col_inc = 0

        # check every direction and incrementing row and column accordingly
        if direction == NORTH or direction == NORTHEAST or direction == NORTHWEST:
            row_inc = -1
        if direction == SOUTHEAST or direction == SOUTH or direction == SOUTHWEST:
            row_inc = 1
        if direction == NORTHEAST or direction == EAST or direction == SOUTHEAST:
            col_inc = 1
        if direction == SOUTHWEST or direction == WEST or direction == NORTHWEST:
            col_inc = -1

        places = []     # pieces to flip
        i = position[0] + row_inc
        j = position[1] + col_inc

        if color == WHITE:
            other = BLACK
        else:
            other = WHITE

        if i in range(8) and j in range(8) and self.board[i][j] == other:
            # assures there is at least one piece to flip
            places = places + [(i, j)]
            i = i + row_inc
            j = j + col_inc
            while i in range(8) and j in range(8) and self.board[i][j] == other:
                # search for more pieces to flip
                places = places + [(i, j)]
                i = i + row_inc
                j = j + col_inc
            if i in range(8) and j in range(8) and self.board[i][j] == color:
                # found a piece of the right color to flip the pieces between
                for pos in places:
                    # flips
                    self.board[pos[0]][pos[1]] = color

    def game_ended(self):
        """ Returns True if the board is full, which means, there are no empty spots
        left on the board. Also, this method will check if there are any valid moves
        left for both players. If there are no valid moves left, it will return True,
        since the game cannot be continued.
        """

        # board full or wipeout
        whites, blacks, empty = self.count_stones()
        if whites == 0 or blacks == 0 or empty == 0:
            return True

        # no valid moves for both players
        if self.get_valid_moves(BLACK) == [] and \
                self.get_valid_moves(WHITE) == []:
            return True

        return False

    def count_stones(self):
        """ Returns the number of white pieces, black pieces and empty squares, in
        this order.
        """
        whites = 0
        blacks = 0
        empty = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == WHITE:
                    whites += 1
                elif self.board[i][j] == BLACK:
                    blacks += 1
                else:
                    empty += 1
        return whites, blacks, empty

    def lookup(self, row, column, color):
        """Returns the possible positions that there exists at least one
        straight (horizontal, vertical, or diagonal) line between the
        piece specified by (row, column, color) and another piece of
        the same color.
        """

        places = []

        if color == BLACK:
            other = WHITE
        else:
            other = BLACK

        # invalid rows and columns
        if row < 0 or row > 7 or column < 0 or column > 7:
            return places

        while 0 <= row < 7 and 0 <= column < 7:
            new_row = row - 1
            while new_row >= 0 and self.board[new_row][column] == other:
                new_row = new_row - 1
                places = places + [(new_row, column)]  # returns north positions
            new_col = column + 1
            while new_col < 8 and self.board[row][new_col] == other:
                new_col = new_col + 1
                places = places + [(row, new_col)]  # returns east positions
            new_col = column - 1
            while new_col >= 0 and self.board[row][new_col] == other:
                new_col = new_col - 1
                places = places + [(row, new_col)]  # returns west positions
            new_row = new_row + 1
            while new_row < 8 and self.board[new_row][column] == other:
                new_row = new_row + 1
                places = places + [(new_row, column)]  # returns south positions

            new_row = row - 1
            new_col = column + 1
            while new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == other:
                new_row = new_row - 1
                new_col = new_col + 1
                places = places + [(new_row, new_col)]  # returns northeast
            new_row = row - 1
            new_col = column - 1
            while new_row >= 0 and new_col >= 0 and self.board[new_row][new_col] == other:
                new_row = new_row - 1
                new_col = new_col - 1
                places = places + [(new_row, new_col)]  # returns northwest
            new_row = new_row + 1
            new_col = new_col + 1
            while new_row < 8 and new_col < 8 and self.board[new_row][new_col] == other:
                new_row = new_row + 1
                new_col = new_col + 1
                places = places + [(new_row, new_col)]  # returns southeast
            new_row = new_row + 1
            new_col = new_col - 1
            while new_row < 8 and new_col >= 0 and self.board[new_row][new_col] == other:
                new_row = new_row + 1
                new_col = new_col - 1
                places = places + [(new_row, new_col)  # returns southwest

        return places