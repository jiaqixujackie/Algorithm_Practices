
"""
input: 
weight: a list used to store weight of each item
value: a list used to store value of each item
capacity: an integer indicating the maximum weight to put into the bag

output:
for items taken, print item's (weight,value) tuple. also print the total value. 
if two or more combinations got the same max_value, pick the one with the less amount of items.
if 2 sets of items got the same number of items, keep both.
"""


def candidate_set(weight, target):
    """
    weight = [0,1,2,3,4,5] 
    target = 3.5
    return 4  --> because weight[0:4]<=target
    """
    if len(weight) == 0 or weight[0]>target:
        return -1
    i = 0
    while weight[i]<=target:
        i+=1
        if i==len(weight):
            break
    return i


def backtracking (info, memory, wLeft, vTotal, inBag, i):
    """
    info[0],info[1] = list of item's weight, list of item's value
    memory[0], memory[1] = historical max total value, set(s) of items with total value of memory[0]
    wLeft, vTotal = remaining capacity of the bag, total value in the bag
    inBag: inBag[i] is either 0 or 1. 0 if not in the bag, 1 if in the bag
    i: index of item last added into the bag

    step 1: get possible items. then find feasible items (weight < wLeft)
    step 2: add the heaviest feasible item into the bag (update inBag)
    step 3: update wLeft and wTotal accordingly
    step 4: make i to the index of item added in step 2
    step 5: repeat step 1 to 4 until all items' weight > wLeft
    step 6: at step 5, if vTotal < memory[0], backtrack to check another set of items
            if vTotal >= memory[0]: 
            - if greater, replace memory to vTotal and inBag
            - if euqal, choose the combination with smaller amount of items
    """

    w,v = info[0],info[1]
    candidates = w[:i]  # [step 1: possible items]
    index = candidate_set(candidates, wLeft) # [step 1: feasible items]
 

    if index == -1:  # [step 6: >=]
        print ("inBag = {}, total value = {}".format(inBag, vTotal))
        if memory[0] == 0 or vTotal>memory[0] or vTotal==memory[0] and sum(inBag)<sum(memory[1][0]):  
            memory = [vTotal,[inBag]]
            return memory
        elif vTotal==memory[0] and sum(inBag)==sum(memory[1][0]):
            memory[1].append(inBag)
            return memory 


    for x in range(index): # [step 6: backtrack]
        k = index - x - 1
        new_bag = inBag[:k] + [1] + inBag[k+1:] # [step 2]
        memory = backtracking(info, memory, wLeft-w[k], vTotal+v[k],new_bag, k) # [step 3,4,5]
    return memory 



def knapsack(w,v,c):
    n = len(w)

    # [step 1: sort w and v by w]
    for i in range(n-1):
        temp = i
        for j in range(i+1,n):
            if w[j] < w[i]:
                temp = j
        w[temp],w[i] = w[i], w[temp]
        v[temp],v[i] = v[i], v[temp]
    
    # [step 2: implement backtracking]
    value,inBag = backtracking((w,v), [0,[[0]*n]], c, 0, [0]*n, len(w))

    # [step 3: build final result]
    items = []
    for i in range(len(inBag)):
        solution = []
        for j in range(n):
            if inBag[i][j]:
                solution.append((w[j],v[j]))
        items.append(solution) if solution else None
    
    print ()
    n = len(items)
    if n == 0:
        return "maximum capacity (weight) is {}, but item's minimum weight is {}".format(c,w[0])
    else:
        for item in items:
            print (item, value)
        return "the above {} sets of items, each with {} items, have maximim value of {}".format(n,len(items[0]),value)





if __name__=="__main__":
    # w = [0,1,2,3,4,5]
    # t1,t2,t3 = -1, 3.5, 6
    # print(candidate_set(w,t3))

    c = 20

    w0 = [25,30]
    v0 = [25,30]

    w1 = [5,15,20]
    v1 = [500,1500,2000]

    w2 = [5,14,20]
    v2 = [500,1600,2000]

    w3 = [5,15,4,16]
    v3 = [500,1500,400,1600]

    w4 = [4,9,10,20,2,1]
    v4 = [400,1800,3500,4000,1000,200]


    print(knapsack(w0,v0,c))
    print(knapsack(w1,v1,c))
    print(knapsack(w2,v2,c))
    print(knapsack(w3,v3,c))
    print(knapsack(w4,v4,c))

