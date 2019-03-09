BLACK = 1
WHITE = 2


def switch_color(color):
    """Decides to change the color of the disk"""

    if color == BLACK:
        return WHITE
    else:
        return BLACK


class Human:

    """ Human player """

    def __init__(self, gui, color="black"):
        self.color = color
        self.gui = gui
        self.current_board = None
        
    def get_moves(self):
        """
        Uses gui to handle mouse
        """

        valid_moves = self.current_board.find_valid_moves(self.color)
        while True:
            move = self.gui.get_mouse_input()
            if move in valid_moves:
                break
        self.current_board.apply_move(move, self.color)
        return 0, self.current_board
      
    def get_current_board(self, board):
        self.current_board = board

