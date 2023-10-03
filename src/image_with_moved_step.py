import cv2

from convert_image2maze import convert_img2maze


# constants definition
END = 3
START = 2
WALL = 0
EMPTY = 1


def translate_step(step):
    """Translate the order to a conceptual step

    This function takes the order pased as parameter and translates it to an array with dimension 2
    that is the conceptual step. This conceptual step will be added to the actual position in the
    conceptual maze, simulating a movement.

    Args:
        step (str): numpyArray of int[][]
            The str that represent the step. This can be "UP", "DOWN", "LEFT" or "RIGHT".

    Returns:
        array[2]: An array with dimension 2 that represent the movement in coordenades
        in a conceptual maze.
    """
    if(step == "UP"):
        return [-1,0]
    if(step == "DOWN"):
        return [1,0]
    if(step == "LEFT"):
        return [0,-1]
    if(step == "RIGHT"):
        return [0,+1]
    

def start_point(maze):
    """
    Look for the start point

    This function look in the conceptual maze for the start point.

    Args:
        maze : numpyArray of int[][]
            The conceptual maze where we are looking the start point.

    Returns
        int[2]
            An array with dimension 2 that represent the coordenade where the start point is.
    """
    for idx_row, row in enumerate(maze):
        for idx_col, col in enumerate(row):
            if(col == START):
                return [idx_row,idx_col]
            

def draw_path_on_maze(original_image_path,steps):
    """
    Drawer of steps in a maze

    This function takes the image of a maze and an array of steps to solve the maze. After 
    the translation of this information it draws in a new image the path in purple to solve the maze.
    
    The new image is saved in the same path of the image passed as parameter with 
    the original image name plus "-steps.png".

    Args:
        original_image_path : str
            The string path where the maze image is. This image must have one (or more) red pixel (start), 
            black pixels (walls), white pixels (empty spaces) and one (or more) green pixel (end).
        
        steps : array of str
            An array of strings that represent the correct path to solve the maze.
    """
    
    # read the original image.
    img = cv2.imread(original_image_path)
    # translate the image to a conceptual maze.
    maze = convert_img2maze(img)
    # look the start point.
    actual_point = start_point(maze)
    
    # for all the steps we have passed as parameter (except the last, that is the final position) ...
    for step in steps[:-1]:
        # ... change our position adding the value of the conceptual step to the actual position ...
        movement = translate_step(step)
        actual_point[0] = actual_point[0] + movement[0]
        actual_point[1] = actual_point[1] + movement[1]
        
        # ... and we change the color of that position in the image to purple.
        img[actual_point[0]][actual_point[1]][0] = 197
        img[actual_point[0]][actual_point[1]][1] = 75
        img[actual_point[0]][actual_point[1]][2] = 140

    # We draw the new image and we saved it.
    cv2.imwrite(original_image_path.split('.')[0] + '-steps.png', img)
    print("New image " + original_image_path.split('.')[0] + "-steps.png created!")