from const import WHITE, BLACK

def switch_color(color) -> None:
    """
    Assigns opposite color.
    """
    if color == BLACK:
        return WHITE
    else:
        return BLACK

class Player:

    """ Human player """

    def __init__(self, gui, color="black"):
        self.color = color
        self.gui = gui
        
    def get_move(self) -> None:
        """ Uses gui to handle mouse
        """
        valid_moves = self.current_board.get_valid_moves(self.color)
        while True:
            move = self.gui.get_mouse_input()
            if move in valid_moves:
                break
        self.current_board.apply_move(move, self.color)
        return 0, self.current_board
    
    def get_current_board(self, board) -> None:
        """Shows the updated board after the move is made"""
        self.current_board = board

