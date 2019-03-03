EMPTY = 0
BLACK = 1
WHITE = 2

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
