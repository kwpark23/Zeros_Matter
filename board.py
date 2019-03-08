EMPTY = 0
BLACK = 1
WHITE = 2
NORTH = 1
NORTHEAST = 2
EAST = 3
SOUTHEAST = 4
SOUTH = 4
SOUTHWEST = 6
WEST = 7
NORTHWEST = 8


class Board:
    """ Grid for which game will be played on """

    def __init__(self):
        """ Creates the board """

        # creates an 8x8 game board using a list of lists
        self.board = [[EMPTY]*8 for n in range(8)]
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        self.board[3][3] = WHITE
        self.board[4][4] = WHITE
        self.logical_moves = []

    def count_tiles(self):
        """
        Create and return a list of numbers that contains the amount of
        white, black and free tiles on the board, in this order.
        """

        blacks = 0
        whites = 0
        empty = 0
        for row in range(8):
            for col in range(8): # Traversal of game board
                if self.board[row][col] == blacks:
                    blacks += 1
                elif self.board[row][col] == whites:
                    whites += 1
                else:
                    empty += 1
        # Add all totals to a list
        return whites, blacks, empty

    def apply_move(self, move, cur_player_color):
        """ Determine if the move is valid and apply the move."""

        if move in self.logical_moves:
            self.board[move[0]][move[1]] = cur_player_color
            for row in range(1, 9):
                self.flip_disks(row, move, cur_player_color)

    def game_end(self):
        """ Determines if game is over """

        whites, blacks, empty = self.count_tiles()
        if whites == 0 or blacks == 0 or empty == 0:
            return True

        # no valid moves for both players
        if self.find_valid_moves(BLACK) == [] and \
                self.find_valid_moves(WHITE) == []:
            return True

    def find_valid_moves(self, cur_player_color):
        """
        Find the available positions to place a disk of the given color. We call this method before
        apply_move.
        """

        avail_pos = []

        for row in range(8):
            for column in range(8):
                if self.board[row][column] == cur_player_color:
                    avail_pos = avail_pos + self.lookup_position(row, column, cur_player_color)

        avail_pos = list(set(avail_pos))
        self.logical_moves = avail_pos
        return avail_pos

    def flip_disks(self, direction, cur_pos, cur_player_color):
        """
        Flips (changes colour) of the disks in the given direction and
        current_player_color from the curr_position.
        """

        incr_row = 0
        incr_col = 0

        # check every direction and incrementing row and column accordingly
        if direction == NORTH or direction == NORTHEAST or direction == NORTHWEST:
            incr_row = -1

        if direction == SOUTHEAST or direction == SOUTH or direction == SOUTHWEST:
            incr_row = 1

        if direction == NORTHEAST or direction == EAST or direction == SOUTHEAST:
            incr_col = 1

        if direction == SOUTHWEST or direction == WEST or direction == NORTHWEST:
            incr_col = -1

        # Save locations of disks to flip
        locations = []
        x_index = cur_pos[0] + incr_row
        y_index = cur_pos[1] + incr_col

        # set color of other_player_color
        if cur_player_color == WHITE:
            other_player_color = BLACK
        else:
            other_player_color = WHITE

        # flip disks; change their color
        if (0 <= x_index < 8) and (0 <= y_index < 8) and self.board[x_index][y_index] == other_player_color:
            # Ensures there is at least one disk to be flipped
            locations = locations + [(x_index, y_index)]
            x_index += incr_row
            y_index += incr_col

            while (0 <= x_index < 8) and (0 <= y_index < 8) and self.board[x_index][y_index] == other_player_color:
                # Searches for more disks to be flipped
                locations = locations + [(x_index, y_index)]
                x_index += incr_row
                y_index += incr_col

            if  (0 <= x_index < 8) and (0 <= y_index < 8) and self.board[x_index][y_index] == cur_player_color:
                # Found a disk of the same color as current_player_color, flips the pieces between
                for location in locations:
                    # flips the disk color
                    self.board[location[0]][location[1]] = cur_player_color

    def lookup_position(self, cur_row, cur_col, cur_player_color):
        """
        Returns the possible positions for a stone of current color
        to be placed to form at least one straight line between another
        piece of the same color on board.
        """

        if cur_player_color == BLACK:
            other_player_color = WHITE
        else:
            other_player_color = WHITE

        avail_pos = []

        # valid rows and columns are between 0 and 7 inclusive
        if cur_row < 0 or cur_row > 7 or \
                cur_col < 0 or cur_col > 7:
            return avail_pos

        # north
        new_row = cur_row - 1
        if new_row >= 0 and self.board[new_row][cur_col] == other_player_color:
            new_row = new_row - 1
            while new_row >= 0 and self.board[new_row][cur_col] == other_player_color:
                new_row = new_row - 1
            if new_row >= 0 and self.board[new_row][cur_col] == EMPTY:
                avail_pos = avail_pos + [(new_row, cur_col)]

        # northeast
        new_row = cur_row - 1
        new_col = cur_col + 1
        if new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == other_player_color:
            new_row = new_row - 1
            new_col = new_col + 1
            while new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == other_player_color:
                new_row = new_row - 1
                new_col = new_col + 1
            if new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == EMPTY:
                avail_pos = avail_pos + [(new_row, new_col)]

        # east
        new_col = cur_col + 1
        if new_col < 8 and self.board[cur_row][new_col] == other_player_color:
            new_col = new_col + 1
            while new_col < 8 and self.board[cur_row][new_col] == other_player_color:
                new_col = new_col + 1
            if new_col < 8 and self.board[cur_row][new_col] == EMPTY:
                avail_pos = avail_pos + [(cur_row, new_col)]

        # southeast
        new_row = cur_row + 1
        new_col = cur_col + 1
        if new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == other_player_color:
            new_row = new_row + 1
            new_col = new_col + 1
            while new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == other_player_color:
                new_row = new_row + 1
                new_col = new_col + 1
            if new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == EMPTY:
                avail_pos = avail_pos + [(new_row, new_col)]

        # south
        new_row = cur_row + 1
        if new_row < 8 and self.board[new_row][cur_col] == other_player_color:
            new_row = new_row + 1
            while new_row < 8 and self.board[new_row][cur_col] == other_player_color:
                new_row = new_row + 1
            if new_row < 8 and self.board[new_row][cur_col] == EMPTY:
                avail_pos = avail_pos + [(new_row, cur_col)]

        # southwest
        new_row = cur_row + 1
        new_col = cur_col - 1
        if new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == other_player_color:
            new_row = new_row + 1
            new_col = new_col - 1
            while new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == other_player_color:
                new_row = new_row + 1
                new_col = new_col - 1
            if new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == EMPTY:
                avail_pos = avail_pos + [(new_row, new_col)]

        # west
        new_col = cur_col - 1
        if new_col >= 0 and self.board[cur_row][new_col] == other_player_color:
            new_col = new_col - 1
            while new_col >= 0 and self.board[cur_row][new_col] == other_player_color:
                new_col = new_col - 1
            if new_col >= 0 and self.board[cur_row][new_col] == EMPTY:
                avail_pos = avail_pos + [(cur_row, new_col)]

        # northwest
        new_row = cur_row - 1
        new_col = cur_col - 1
        if new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == other_player_color:
            new_row = new_row - 1
            new_col = new_col - 1
            while new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == other_player_color:
                new_row = new_row - 1
                new_col = new_col - 1
            if new_row >= 0 and new_col < 8 and self.board[new_row][new_col] == EMPTY:
                avail_pos = avail_pos + [(new_row, new_col)]

        return avail_pos
