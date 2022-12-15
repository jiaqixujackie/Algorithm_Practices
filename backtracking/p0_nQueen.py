

def nQueen(n):
    return nQueen_aux(n, [])


def nQueen_aux(n, partial):

    if len(partial) == n:           # [base case, complete solution]
        return [partial]

    # [selection function]
    possible_i = [i for i in range(n)]

    # [feasible function]
    col = len(partial)

    for j in range(len(partial)):   # on the j-th col
        i = partial[j]              # we have a queen on the i-th row
        
        possible_i[i] = -1          # same row, so cannot 
        
        distance = col - j            
        if 0 <= i+distance < n:        # topLeft to bottomRight diagonal, so cannot
            possible_i[i+distance] = -1
        if 0 <= i-distance < n:        # topRight to bottomLeft diagonal, so cannot
            possible_i[i-distance] = -1

    feasible_i = [i for i in possible_i if i!=-1]
    if len(feasible_i) == 0:        # [base case, wrong solution]
        return []
    
    # [objective function]
    solution = []

    for i in feasible_i:
        new_partial = partial[:] + [i]
        solution += nQueen_aux(n,new_partial)

    return solution 



if __name__ == "__main__":
    print(nQueen(4))
