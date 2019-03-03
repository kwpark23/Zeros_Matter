BLACK = 1
WHITE = 2


def switch_color(color):
  """Decides to change the color of the disk"""
    if color == BLACK:
        return WHITE
    else:
        return BLACK
