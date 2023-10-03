# import necessary libraries
import numpy as np

from create_rules_prolog import create_rules


def convert_img2maze(image):
    """Image to matrix translator

    This function takes a cv2 image and translate it to a int matrix.

    Args:
        image (np.array): numpyArray[][] of numpyArray[3]
            The image with the RGB vectors that we are reading and we will translate to a conceptual maze.

    Returns:
        numpyArray of int[][]: The conceptual maze where we are looking the start point.
    """
    # Maze size == Image size
    width, height = image.shape[:2]
    # At the begining, our maze is a matrix of all ones
    maze = np.ones([width,height])

    # We iterate in the rows and columns
    for idx_row, row in enumerate(image):
        for idx_col, col in enumerate(row):
            # We translate the RGB vector of a pixel to a simbolic element (wall, empty space...) of our maze
            label = create_rules(col)
            maze[idx_row][idx_col] = float(label)
    
    return maze