
# ---------- Coin Change Problem, bottom up approach ----------


def coins_change_bottomUp(coins:list, n:int):

    mem = [float("inf")]*(n+1)      # step 1: mem list 
    mem[0] = 0                      # step 2: base case

    for i in range(1,n+1):  # solve all cases iteratively from small to 
                            # large until we find the solution for F(n).
        options = [mem[i-k] for k in coins if k <= i]
        mem[i] = min(options) + 1

    return -1 if mem[n]==float("inf") else mem[n]





# ---------- Coin Change Problem, top down approach ----------


def coins_change_topDown(coins:list, n:int):

    mem = [float("inf")]*(n+1)      # step 1: mem list
    mem[0] = 0                      # step 2: base case 

    CC_AUX(coins, n, mem)

    return -1 if mem[n]==float("inf") else mem[n]

def CC_AUX(coins:list, n:int, mem:list):

    # return f(n) if f(n) has an optimal solution
    if   mem[n] != float("inf"):    
        return mem[n]
    
    # otherwise, since n = k + (n-k), so f(n) = f(k) + f(n-k) for valid k. 
    elif mem[n] == float("inf"):    
        for k in coins:
            option = (CC_AUX(coins, k, mem) + \
                      CC_AUX(coins, n-k, mem)) if k <= n else mem[n]
            mem[n] = min(mem[n], option)
        return mem[n]

