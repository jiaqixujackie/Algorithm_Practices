
# Number of possible paths from top left to bottom right



# bottom up approach


def paths_bottomUp(m,n):                # m rows and n columns

    mem = [[0]*n for i in range(m)]		# step 1: memory graph

    for i in range(m):					# step 2: base case 1: 1st column
        mem[i][0] = 1
    for j in range(n):					# step 2: base case 2: 1st fow
        mem[0][j] = 1
    
    for i in range(1,m):				# step 3: iterations
        for j in range(1,n):
            mem[i][j] = mem[i-1][j] + mem[i][j-1]
    
    return mem[m-1][n-1]



# top down approach


def paths_topDown(m,n):

    mem = [[0]*n for i in range(m)]         # step 1: memory list 

    for i in range(m):                      # step 2: base cases 
        mem[i][0] = 1
    for j in range(n):
        mem[0][j] = 1

    paths_bottomUp_aux(mem, m-1, n-1)       # step 3: general cases 

    return mem[m-1][n-1]


def paths_bottomUp_aux(mem,m,n):

    if mem[m][n] != 0:                      # if number of paths is known, 
        return mem[m][n]                    # then simply return it as solution 
    
    elif mem[m][n] == 0:                    # otherwise, use, break it down to subproblems
        upper = paths_bottomUp_aux(mem, m-1, n)
        left = paths_bottomUp_aux(mem, m, n-1)
        mem[m][n] = upper + left
        return mem[m][n]

