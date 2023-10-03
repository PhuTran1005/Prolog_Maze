import cv2

from convert_image2maze import convert_img2maze
from states import init_state, end_state


# constants definition
END = 3
START = 2
WALL = 0
EMPTY = 1


def write_rules(img_path, rules=False):
    """Image to rule translator

    This function takes an image path and generate a cv2 image. After that we create
    a conceptual maze and with that maze we generate the rules or facts written in prolog.
    This function write a .pl file with all the facts or rules for the prolog program.

    Args:
        img_path (str): The str path where the maze image is. This image must have one (or more)
        red pixel (start), black pixels (walls), white pixels (empty spaces) and one (or more) 
        green pixel (end).
    """
    print("Writing new rules for maze for image at: " + img_path)
    # read image
    img = cv2.imread(img_path)
    # convert the image to a conceptual maze
    maze = convert_img2maze(img)

    # create the .pl file where the rules or facts will be written
    file = open(img_path.split('.')[0] + ".pl","w")

    # write the initial state rule (start)
    line = init_state(maze)
    file.write(line)
    file.write("\n")

    # write the end state rule (end)
    line = end_state(maze)
    file.write(line)
    file.write("\n")

    if rules:
        line = ("c(X, Y, wall) :- \n")
        file.write(line)

    # iterate in every matrix[i][j] (the maze) value and if it's a wall we write a fact or rule with the wall position.
    for idx_row, row in enumerate(maze):
        for idx_col, col in enumerate(row):
            if(col == WALL):
                if rules:
                    line = (f"\tX = {idx_row}, Y = {idx_col}\n\t;\n" )
                    file.write(line)
                else:
                    line = (f"c({idx_row},{idx_col},wall).\n" )
                    file.write(line)

    if rules:
        width, height = img.shape[:2]
        line = (f"\tX > {width}; Y > {height}." )
        file.write(line)
    
    file.close()

    print("New rules for maze in file " + img_path.split('.')[0] + ".pl")
    print("Done!")