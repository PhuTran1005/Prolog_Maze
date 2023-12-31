## Term Project for Computational Linguistic
## Prolog-Mazes

## The Prolog Maze Solver Project
The Jupyter Notebook "Mazes Manipulation Script" (and also the python script with the same name) 
allows us to convert images of labyrinths into rules or facts
or draw the path that would be followed to solve the labyrinth.

The prolog file "MazeSolver.pl" is the skeleton on which we have worked to solve mazes. 
With this file you can select the .pl file you want to read with the facts that represent 
the laberint (generated by the python script) and solve it!

If you don't want to select the file you can embed the rules or facts as you can see in the 
examples on the folder "embedded facts or rules examples" 
like "MazeSolver_Maze0_with_rules.pl" or others.

In the folder of "mazes" there are several .png images of labyrinths that, through the Jupyter Notebook 
we have translated to facts. Next to every image there are the text file with the facts 
(entry point to the labyrinth, exit and the existing walls) that prolog can understand. 
The prolog file that we have programmed can read files so we just 
have to indicate the path of the file we want to solve. Next to the files you can see the maze 
solution with the path drawed writen in a .png image generated by our python script.

Thanks for read me! (^.^)