
### https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/?ref=lbp

"""
Use a graph to represent a r rows by c columns maze where graph[i][j]==0 
if it is a dead cell, and graph[i][j]==1 if not. This task starts with a 
rat standing at the top left corner, graph[0][0]. It then aims to find a 
path from graph[0][0] to the right bottom corner (by moving 1 step 
forward or downward each time) to access the food. 

This task finishes by printing out the board with an embeded path in 
it where 0 indicates dead cell, a * on each cells that contribute to 
the path, and leave it as blank for the rest of the cells. 


2 main tasks: 
    - task 1: find a path, this is where we implement backtracking.
    - task 2: print the path on the board (irrelevant to backtracking).

Task 1: 
    1.  [selection function] find fields to the right or below current field.
    2.  [feasible function] from the adjacent fields, find the ones that can 
        be visited.
    3.  [objective function] implement backtracing to build the path (keep 
        calling the feasible function). For each field, assume the selected
        candidate is a good one, add it to the path and move on to the next
        field. Backtrack if we reach a dead corner. keep doing this until 
        we reach the right bottom corner.
    4.  [solution function] this is for us to get the board size, so that we
        can implement backtracking. 

Task 2: Try it yourself, as it is very similar to your sudoku assignment!
"""


###
### Task 1: use backtracking to find a path
###

def try_next(board,i,j): # [selection function]
    """
    for field (i,j), check whether (i+1, j) and/or (i,j+1) 
    is/are on the board. returns them as candidate set.
    """
    candidate_fields = []
    if i < len(board)-1:
        candidate_fields.append((i+1,j))
    if j < len(board[0])-1:
        candidate_fields.append((i,j+1))
    return candidate_fields

def feasible_next (board,i,j): # [feasible function]
    """
    for candidate in the candidate set, check its feasibility. 
    a candidate field (x,y) is feasible if board[x][y] == 1. 

    we do not need to check whether the candidate field has been 
    previously visited because we can't go backward or upward, 
    which indicates that the formation of a cycle is impossible. 
    """
    candidates = try_next(board,i,j)
    return [(x,y) for x,y in candidates if board[x][y]]


from copy import deepcopy

def backtracking(board, i,j, path):
    """
    step 1: find the feasible candidate set for field (i,j)
    step 2: for candidate in the candidate set, add candidate to 
            the path, assume the candidate can lead to the right 
            path, then repeat step 1 and 2 for the chosen candidate.
    step 3: backtrack if the out of feasible candidate, else keep 
            extend the path until we reach the end. 
    """

    r,c = len(board), len(board[0]) # number of rows(r) and columns(c)

    if (i,j) == (r-1,c-1): # [step 3 (reach the end)]
        return path

    solution = None
    candidates = feasible_next(board,i,j)   # [step 1]

    for x,y in candidates:  # [step 2, and step 3 (backtrack)]
        new_path = deepcopy(path)
        new_path.append((x,y)) # step 2
        solution = backtracking(board, x,y, new_path) or solution
        if solution:
            break
    
    return solution 


def MazePath(board):
    solution = backtracking(board,0,0,[(0,0)]) 
    return solution if solution else "Path to the food does not exist"



###
### Task 2: print the path onto the board.
###

def MazeSolver(board):
    """ print the path onto the board.
    step 1: find a path
    step 2: if path is found, change board[i][j] to "*" where (i,j) 
            are index of the path.
    step 3: print a boarderline on top of the board
    step 4: for each row in the board:
            - print board[row] with condition flow on board[row][col]
            - print a boarderline 

    """

    path = MazePath(board)  # [step 1]
    if type(path) == list:  # [step 2]
        for i,j in path:
            board[i][j] = "*"
    
    # store boarderline for step 3 and 4
    line = "|"+"-"*(len(board[0])*2-1) +"|" 

    print(line) #[step 3]

    # [step 4]
    for item in board: 
        print("|",end="")
        for j in item:
            print(j,end="|") if j is "*" or j is 0 else print(" ", end="|")
        print("\n"+line)
    
    # retuns the path or the error message
    return path 



###
### testing 
###

if __name__ == "__main__":

    small1 = [[1,1],
              [1,1]]
    small2 = [[1,1],
              [0,1]]
    small3 = [[1,0],
              [0,1]]

    big1 =  [[1,0,1,1],
             [1,1,0,1],
             [1,1,1,0],
             [0,1,1,1]]
    big2 =  [[1,0,1,1],
             [1,1,0,1],
             [1,1,1,0],
             [0,1,1,0]]

    rectangle =[[1,0,1,1],
                [1,1,0,1],
                [1,1,1,1]]
    
    # print(MazeSolver(small1))      
    # print(MazeSolver(big2))
    # print(MazeSolver(rectangle))
