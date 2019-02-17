EMPTY = 0
BLACK = 1
WHITE = 2


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
