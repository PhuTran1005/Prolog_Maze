# constants definition
END = 3
START = 2
WALL = 0
EMPTY = 1


def init_state(maze):
    """Initial position rule

    This function search in a conceptual maze the position where we will start our steps
    to solve the maze and returns a string with the fact that it would indicate the 
    initial position written in prolog.

    Args:
        maze (np.array): numpyArray of int[][]
            The conceptual maze where we are looking the start point.

    Returns:
        str: The fact that it would indicate the initial position written in prolog.
    """
    for idx_row, row in enumerate(maze):
        for idx_col, col in enumerate(row):
            if col == START:
                return (f"initial_state( maze, p({idx_row},{idx_col}) )")
            

def end_state(maze):
    """End position rule

    This function search in a conceptual maze the position where we will stop to solve the maze and
    returns a string with the fact that it would indicate the final position written in prolog.

    Args:
        maze (np.array): numpyArray of int[][]
            The conceptual maze where we are looking the end point.

    Returns:
        str: The fact that it would indicate the end position written in prolog.
    """
    for idx_row, row in enumerate(maze):
        for idx_col, col in enumerate(row):
            if col == END:
                return (f"initial_state( maze, p({idx_row},{idx_col}) )")