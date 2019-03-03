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

def lookup_position(current_row, current_column, board, current_player_color):

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
    while new_row >= 0 and board[new_row][current_column] == other_player_color:
        new_row = new_row - 1
    if board[new_row][current_column] == EMPTY:
        available_positions = available_positions + [(new_row, current_column)]

    # east
    new_column = current_column + 1
    while new_column < 8 and board[current_row][new_column] == other_player_color:
        new_column = new_column + 1
    if board[current_row][new_column] == EMPTY:
        available_positions = available_positions + [(current_row, new_column)]

    # south
    new_row = current_row + 1
    while new_row < 8 and board[new_row][current_column] == other_player_color:
        new_row = new_row + 1
    if board[new_row][current_column] == EMPTY:
        available_positions = available_positions + [(new_row, current_column)]

    # west
    new_column = current_column - 1
    while new_column >= 0 and board[current_row][new_column] == other_player_color:
        new_column = new_column - 1
    if board[current_row][new_column] == EMPTY:
            available_positions = available_positions + [(current_row, new_column)]

    return available_positions



  def find_valid_moves(board, current_player_color):
        """Find the available positions to place a disk of the given color. We call this method before
        apply_move."""

        if current_player_color == BLACK:
            other_player_color = WHITE
        else:
            other_player_color = BLACK

        available_positions = []

        for row in range(8):
            for column in range(8):
                if board[row][column] == current_player_color:
                    available_positions = available_positions +  board.lookup_position(row, column, current_player_color)
                    #using Jin's lookup_position function

        available_positions = list(set(available_positions))
        board.find_valid_moves = available_positions
        return available_positions

    def apply_move(board, move, current_player_color):
        """ Determine if the move is valid and apply the move.
        """
        if move in find_valid_moves:
            board[move[0]][move[1]] = current_player_color
            for row in range(1, 9):
                #the changes are executed using Maha's flip_disks function
                board.flip_disks(row, move, current_player_color)
                
    def flip_disks(direction, curr_position, current_player_color):
    """Flips (changes colour) of the disks in the given direction and
    current_player_color from the curr_position. 
    
    """
    
    incr_row = 0
    incr_colmn = 0

    #check every direction and incrementing row and column accordingly
    if directin == NORTH or direction == NORTHEAST or direction == NORTHWEST:
        incr_row = -1

    if direction == SOUTHEAST or direction == SOUTH or direction == SOUTHWEST:
        incr_row = 1

    if drection == NORTHEAST or direction == EAST or direction == SOUTHEAST:
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
    if (0 <= x_index < 8) and (0 <= y_index < 8) and board[x_index][y_index] == other_player_color:
        # Ensures there is at least one disk to be flipped
        locations = locations + [(x_index, y_index)]
        x_index += incr_row
        y_index += incr_colmn

        while (0 <= x_index < 8) and (0 <= y_index < 8) and board[x_index][y_index] == other_player_color:
            # Searches for more disks to be flipped
            locations = locations + [(x_index, y_index)]
            x_index += incr_row
            y_index += incr_colmn

        if  (0 <= x_index < 8) and (0 <= y_index < 8) and board[x_index][y_index] == current_player_color:
            # Found a disk of the same color as current_player_color, flips the pieces between
            for location in locations:
                # flips the disk color
                board[location[0]][location[1]] = current_player_colour
