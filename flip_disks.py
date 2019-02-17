EMPTY = 0
BLACK = 1
WHITE = 2


def flip_disks(direction, curr_position, current_player_color):
    """Flips (changes colour) of the disks in the given direction and
    current_player_color from the curr_position. With the following
    conventions for directions:
    1=North, 2=NorthEast, 3=East, 4=SouthEast, 5=Sotuh, 6=SouthWest,
    7=West, 8=NorthWest.

    """

    incr_row = 0
    incr_colmn = 0

    #check every direction
    if direction == 1:
        # North
        incr_row = -1
        incr_colmn = 0
        
    elif direction == 2:
        # Northeast
        incr_row = -1
        incr_colmn = 1
        
    elif direction == 3:
        # East
        incr_row = 0
        incr_colmn = 1
        
    elif direction == 4:
        # Southeast
        incr_row = 1
        incr_colmn = 1
        
    elif direction == 5:
        # South
        incr_row = 1
        incr_colmn = 0
        
    elif direction == 6:
        # Southwest
        incr_row = 1
        incr_colmn = -1
        
    elif direction == 7:
        # West
        incr_row = 0
        incr_colmn = -1
        
    elif direction == 8:
        # Northwest
        incr_row = -1
        incr_colmn= -1

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
    if x_index in range(8) and y_index in range(8) and board[x_index][y_index] == other_player_color:
        # Ensures there is at least one disk to be flipped
        locations = locations + [(x_index, y_index)]
        x_index += incr_row
        y_index += incr_colmn

        while x_index in range(8) and y_index in range(8) and board[x_index][y_index] == other_player_color:
            # Searches for more disks to be flipped
            locations = locations + [(x_index, y_index)]
            x_index += incr_row
            y_index += incr_colmn

        if  x_index in range(8) and y_index in range(8) and board[x_index][y_index] == current_player_color:
            # Found a disk of the same color as current_player_color, flips the pieces between
            for location in locations:
                # flips the disk color
                board[location[0]][location[1]] = current_player_colour
        
