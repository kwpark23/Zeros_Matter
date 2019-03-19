from const import WHITE, BLACK

def switch_color(color) -> None:
    """
    Assigns opposite color.
    """
    if color == BLACK:
        return WHITE
    else:
        return BLACK

class Human:

    """ Human player """

    def __init__(self, gui, color="black"):
        self.color = color
        self.gui = gui
