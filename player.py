BLACK = 1
WHITE = 2


def change_color(color):
    if color == BLACK:
        return WHITE
    else:
        return BLACK


class Human:

    """ Human player """

    def __init__(self, gui, color="black"):
        self.color = color
        self.gui = gui

    def get_move(self):
        """ Uses gui to handle mouse
        """
        validMoves = self.current_board.get_valid_moves(self.color)
        while True:
            move = self.gui.get_mouse_input()
            if move in validMoves:
                break
        self.current_board.apply_move(move, self.color)
        return 0, self.current_board

    def get_current_board(self, board):
        self.current_board = board
