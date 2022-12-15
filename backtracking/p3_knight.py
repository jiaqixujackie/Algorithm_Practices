
### https://www.geeksforgeeks.org/warnsdorffs-algorithm-knights-tour-problem/ 

"""
in a board of size r by c, starting from filed (0,0), use knight's move 
to visit each of the field exactly once.

    1.  [selection function] find all field that are 2 by 1 step away 
        from the current field.
    2.  [feasible function] from the fields that are 2 by 1 steps away,
        find those that can be visited. 
    3.  [objective function] implement backtracing to build the 
        knight path. We need to use the feasible function to extend 
        the knight path.
    4.  [solution function] this is for the user. the user need to enter
        the board size, so that we can attempt to find the knight path.

"""



def next_move(board_size, field): # [selection function]
    """
    input: 2 tuple, one as the board size (r,c), another as the field (i,j)
    output: find all fields that are 2 by 1 steps away from the (i,j)
    """
    row, col, i,j = board_size[0], board_size[1], field[0],field[1]

    # element in the following two list must be paired by index to generate 
    # all of the possible combinations of 2 by 1.
    move_x = [2,2, -2,-2, 1,1, -1,-1]
    move_y = [1,-1, 1,-1, 2,-2, 2,-2]

    candidates = []
    for k in range(8):
        x = i + move_x[k]
        y = j + move_y[k]
        if 0<=x<row and 0<=y<col: # make sure (x,y) is a field on the board
            candidates.append((x,y))
    return candidates


def safe_moves(board, i,j): # [feasible function]
    """
    input: a board and a field (i,j)
    output: find all fields that are 2 by 1 steps away from the (i,j) which can be visited.
    """
    candidates = next_move((len(board), len(board[0])), (i,j))
    valid_candidates = [field for field in candidates if board[field[0]][field[1]] == -1 ]
    return valid_candidates


from copy import deepcopy

def backtracking(board,i,j,moves): # [objective function]
    """
    a board to be modified: put numbers into the board to form the knight's path
    a field (i,j): used to find the next knight jump (2 by 1)
    moves is used to count how many we jumps we have had so far
    
    step 1: find all feasible jumps from field (i,j)
    step 2: from all the feasible jumps, choose one to jump. then repeat step 1 
            and 2 for the chosen field. backtrack if no feasible jump.
    step 3: once we jump through all the fields, break through all the loops and
            return is as solution
    """
    row, col = len(board), len(board[0])

    # step 3: returns the solution 
    if moves == row*col:
        return [board]

    solution = []

    # step 1
    next_move = safe_moves(board,i,j) 

    # step 2
    for field in next_move:         # from all feasible jumps
        new_board = deepcopy(board)
        x,y = field[0],field[1]     # choose one
        new_board[x][y]= moves      # to jump 
        s = backtracking(new_board, x,y, moves+1) # repeat step 1 and 2 for (x,y)
        solution = s or solution
        if solution:    # step 3: once found, break through the loop 
            break

    # for field in next_move:
    #     x,y = field[0], field[1]
    #     board[x][y] = moves
    #     s = backtracking(board, x,y, moves+1)
    #     solution = s or solution
    #     if solution:
    #         break
    #     else:  
    #         board[x][y] = -1

    return solution


def knight_tour(row, col): # [solution function]
    x,y = 0,0
    board = [[-1 for j in range(col)] for i in range(row)]
    board[x][y] = 0
    solution = backtracking(board, x,y, 1)
    return solution[0] if solution else "No Solution"


if __name__ == "__main__":
    print (knight_tour(2,100))
    print (knight_tour(4,4))
    print (knight_tour(3,8))

