
"""
sum up to target value using smallest amount of coins 

[selection function] all the coins (sorted, from big to small)
[feasible function] index of first coins with value <= target
[objective function] keep adding coins with max_feasible value until == target
[solution function] get input (coins, target) from user, implement backtracking.
"""


def feasible_coins (target, coins):
    for i in range(len(coins)):
        if coins[i] <= target:
            return i
    return -1 # no coin <= target


def backtracking(target, coins, mem):

    x = feasible_coins(target, coins)
    if x == -1 and target != 0:
        return []
    elif x==-1 and target == 0:
        return mem
    
    solution = []
    n = len(coins)
    for i in range(x,n):
        new_mem = mem[:]
        new_mem.append(coins[i])
        solution = backtracking(target-coins[i], coins, new_mem) or solution
        if solution:
            break
    
    return solution


def exchange(target,coins):
    coins.sort()
    coins.reverse() 
    return backtracking(target, coins, [])



if __name__ == "__main__":

    x1,t1 = [3,7], 8
    x2,t2 = [1,3,5,7], 18
    print(exchange(t1,x1))
    print(exchange(t2,x2))

    
