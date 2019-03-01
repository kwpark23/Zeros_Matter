EMPTY = 0
BLACK = 1
WHITE = 2


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
