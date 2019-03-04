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
        self.grid = [[EMPTY]*8 for n in range(8)]
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
        # Add all totals to a list
        space_count.extend(white, black, free)
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
            
    def apply_move(self, move, color):
        """ Determine if the move is correct and apply the changes in the game.
        """
        
        if move in self.logical_moves:
            self.grid[move[0]][move[1]] = color
            for i in range(1, 9):
                self.flip_disks(i, move, color)

    def get_changes(self):
        """ Return white and black tiles. """

        whites, blacks, empty = self.count_tiles()

        return (self.grid, blacks, whites)

    def game_end(self):
        """ Determines if game is over """

        # colour wipeout or board is full
        whites, blacks, empty = self.count_tiles()
        if whites == 0 or blacks == 0 or empty == 0:
            return True

        # no valid moves for both players
        if self.find_valid_moves(BLACK) == [] and \
        self.find_valid_moves(WHITE) == []:
            return True

        return False

    def find_valid_moves(self, current_player_color):
        """Find the available positions to place a disk of the given color. We call this method before
        apply_move."""

        if current_player_color == BLACK:
            other_player_color = WHITE
        else:
            other_player_color = BLACK

        available_positions = []

        for row in range(8):
            for column in range(8):
                if self.board[row][column] == current_player_color:
                    available_positions = available_positions +  self.lookup_position(row, column, current_player_color)
                    # using Jin's lookup_position function

        available_positions = list(set(available_positions))
        self.find_valid_moves = available_positions
        return available_positions

    def apply_move(self, move, current_player_color):
        """ Determine if the move is valid and apply the move.
        """
        if move in self.find_valid_moves:
            self.board[move[0]][move[1]] = current_player_color
            for row in range(1, 9):
                # the changes are executed using Maha's flip_disks function
                self.flip_disks(row, move, current_player_color)

    def flip_disks(self, direction, curr_position, current_player_color):
        """Flips (changes colour) of the disks in the given direction and
        current_player_color from the curr_position.

        """

        incr_row = 0
        incr_colmn = 0

        # check every direction and incrementing row and column accordingly
        if direction == NORTH or direction == NORTHEAST or direction == NORTHWEST:
            incr_row = -1

        if direction == SOUTHEAST or direction == SOUTH or direction == SOUTHWEST:
            incr_row = 1

        if direction == NORTHEAST or direction == EAST or direction == SOUTHEAST:
            incr_colmn = 1

        if direction == SOUTHWEST or direction == WEST or direction == NORTHWEST:
            incr_colmn = -1

        # Save locations of disks to flip
        locations = []
        x_index = curr_position[0] + incr_row
        y_index = curr_position[1] + incr_colmn

        # set color of other_player_color
        if current_player_color == WHITE:
            other_player_color = BLACK
        else:
            other_player_color = WHITE

        # flip disks; change their color
        if (0 <= x_index < 8) and (0 <= y_index < 8) and self.board[x_index][y_index] == other_player_color:
            # Ensures there is at least one disk to be flipped
            locations = locations + [(x_index, y_index)]
            x_index += incr_row
            y_index += incr_colmn

            while (0 <= x_index < 8) and (0 <= y_index < 8) and self.board[x_index][y_index] == other_player_color:
                # Searches for more disks to be flipped
                locations = locations + [(x_index, y_index)]
                x_index += incr_row
                y_index += incr_colmn

            if  (0 <= x_index < 8) and (0 <= y_index < 8) and self.board[x_index][y_index] == current_player_color:
                # Found a disk of the same color as current_player_color, flips the pieces between
                for location in locations:
                    # flips the disk color
                    self.board[location[0]][location[1]] = current_player_colour

    def lookup_position(self, current_row, current_column, current_player_color):
        """Returns the possible positions for a stone of current color
        to be placed to form at least one straight line between another
        piece of the same color on board.
        """

        if current_player_color == BLACK:
            other_player_color = WHITE
        else:
            other_player_color = WHITE

        available_positions = []

        # valid rows and columns are between 0 and 7 inclusive
        if current_row < 0 or current_row > 7 or \
                current_column < 0 or current_column > 7:
            return available_positions

        # search for possible positions to put a stone in each direction

        # north
        new_row = current_row - 1
        if new_row >= 0 and self.board[new_row][current_column] == other_player_color:
            new_row = new_row - 1
            while new_row >= 0 and self.board[new_row][current_column] == other_player_color:
                new_row = new_row - 1
            if new_row >= 0 and self.board[new_row][current_column] == EMPTY:
                available_positions = available_positions + [(new_row, current_column)]

        # northeast
        new_row = current_row - 1
        new_column = current_column + 1
        if new_row >= 0 and new_column < 8 and self.board[new_row][new_column] == other_player_color:
            new_row = new_row - 1
            new_column = new_column + 1
            while new_row >= 0 and new_column < 8 and self.board[new_row][new_column] == other_player_color:
                new_row = new_row - 1
                new_column = new_column + 1
            if new_row >= 0 and new_column < 8 and self.baord[new_row][new_column] == EMPTY:
                available_positions = available_positions + [(new_row, new_column)]

        # east
        new_column = current_column + 1
        if new_column < 8 and self.board[current_row][new_column] == other_player_color:
            new_column = new_column + 1
            while new_column < 8 and self.board[current_row][new_column] == other_player_color:
                new_column = new_column + 1
            if new_column < 8 and self.board[current_row][new_column] == EMPTY:
                available_positions = available_positions + [(current_row, new_column)]

        # southeast
        new_row = current_row + 1
        new_column = current_column + 1
        if new_row >= 0 and new_column < 8 and self.board[new_row][new_column] == other_player_color:
            new_row = new_row + 1
            new_column = new_column + 1
            while new_row >= 0 and new_column < 8 and self.board[new_row][new_column] == other_player_color:
                new_row = new_row + 1
                new_column = new_column + 1
            if new_row >= 0 and new_column < 8 and self.baord[new_row][new_column] == EMPTY:
                available_positions = available_positions + [(new_row, new_column)]

        # south
        new_row = current_row + 1
        if new_row < 8 and self.board[new_row][current_column] == other_player_color:
            new_row = new_row + 1
            while new_row < 8 and self.board[new_row][current_column] == other_player_color:
                new_row = new_row + 1
            if new_row < 8 and self.board[new_row][current_column] == EMPTY:
                available_positions = available_positions + [(new_row, current_column)]

        # southwest
        new_row = current_row + 1
        new_column = current_column - 1
        if new_row >= 0 and new_column < 8 and self.board[new_row][new_column] == other_player_color:
            new_row = new_row + 1
            new_column = new_column - 1
            while new_row >= 0 and new_column < 8 and self.board[new_row][new_column] == other_player_color:
                new_row = new_row + 1
                new_column = new_column - 1
            if new_row >= 0 and new_column < 8 and self.baord[new_row][new_column] == EMPTY:
                available_positions = available_positions + [(new_row, new_column)]

        # west
        new_column = current_column - 1
        if new_column >= 0 and self.board[current_row][new_column] == other_player_color:
            new_column = new_column - 1
            while new_column >= 0 and self.board[current_row][new_column] == other_player_color:
                new_column = new_column - 1
            if new_column >= 0 and self.board[current_row][new_column] == EMPTY:
                available_positions = available_positions + [(current_row, new_column)]

        # northwest
        new_row = current_row - 1
        new_column = current_column - 1
        if new_row >= 0 and new_column < 8 and self.board[new_row][new_column] == other_player_color:
            new_row = new_row - 1
            new_column = new_column - 1
            while new_row >= 0 and new_column < 8 and self.board[new_row][new_column] == other_player_color:
                new_row = new_row - 1
                new_column = new_column - 1
            if new_row >= 0 and new_column < 8 and self.baord[new_row][new_column] == EMPTY:
                available_positions = available_positions + [(new_row, new_column)]

        return available_positions
