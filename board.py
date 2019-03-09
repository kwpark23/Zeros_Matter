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

    def __getitem__(self, i, j):
        return self.board[i][j]

    def lookup(self, row, column, color):
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
        """ Flips (capturates) the pieces of the given color in the given direction
        (1=North,2=Northeast...) from position. """
        row_inc = 0
        col_inc = 0

        if direction == 1:
            # north
            row_inc = -1
            col_inc = 0
        elif direction == 2:
            # northeast
            row_inc = -1
            col_inc = 1
        elif direction == 3:
            # east
            row_inc = 0
            col_inc = 1
        elif direction == 4:
            # southeast
            row_inc = 1
            col_inc = 1
        elif direction == 5:
            # south
            row_inc = 1
            col_inc = 0
        elif direction == 6:
            # southwest
            row_inc = 1
            col_inc = -1
        elif direction == 7:
            # west
            row_inc = 0
            col_inc = -1
        elif direction == 8:
            # northwest
            row_inc = -1
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

