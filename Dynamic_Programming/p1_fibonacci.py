 

# Fibonacci Sequence: Bottom-Up Approach: 
# for loop, solve all cases from small to large  


def fib_seq_bottomup(n:int):
    
    mem = [None]*(n+1)          # create a memory list
    mem[0], mem[1] = 0,1        # complete all base cases

    # find optimal solution for fibonacci[i] for i in [1,n]

    for i in range(2,n+1):              # iteratively
        mem[i] = mem[i-1] + mem[n-2]    # store it into mem list

    return  mem[n]





# FIbonacci Sequence: Top-Down Approach: 
# recursion (backtracking), focus on large case, look into smaller cases only when large case got no solution


def fib_seq_topdown(n):

    mem = [None]*(n+1)          # create a memory list
    mem[0], mem[1] = 0, 1       # complete base cases

    return fib_seq_aux(n, mem)  # find fibonacci[n] recursively


def fib_seq_aux(n, mem):

    # if we have the anwer, then simply return it
    if mem[n] != None:      
        return mem[n]       
    
    # no solution for mem[n] yet, so look at the subproblem.
    else:        
        mem[n] = fib_seq_aux(n-1, mem) + fib_seq_aux(n-2, mem)
        return mem[n]
