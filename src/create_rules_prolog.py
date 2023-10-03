# constants definition
END = 3
START = 2
WALL = 0
EMPTY = 1


def create_rules(pixel_value):
    """Rules prolog creation

    This function translate a numpy array of 3 positions (Red, Greens and Blues) and 
    decide if the vector is a wall, an empty space, the start or the end of a maze.

    Args:
        pixel_value (np.array): numpyArray of int[3] (Red, Greens and Blues) with the color coded 
            as a value between 0 and 255 on the RGB scale

    Returns:
        int: The simbol we are using to identify a element of the maze; a wall, 
        an empty space, the start or the end.
    """
    if pixel_value[0] > 150 and pixel_value[1] > 150 and pixel_value[2] > 150:
        # if white color, empty
        return EMPTY
    if pixel_value[0] < 150 and pixel_value[1] > 150 and pixel_value[2] < 150:
        # If green color, end
        return END
    if pixel_value[0] < 150 and pixel_value[1] < 150 and pixel_value[2] > 150:
        # If blue color, start
        return START
    if pixel_value[0] == 0 and pixel_value[1] == 0 and pixel_value[2] == 0:
        # if black  color, wall
        return WALL

    # If is different from above (an strange value), wall
    return WALL