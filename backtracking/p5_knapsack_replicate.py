


def backtracking (info, memory, wLeft, vTotal, inBag):

    w,v,n = info[0],info[1], len(inBag)

    add_item = False
    for i in range(n-1,-1,-1):
        if w[i] <= wLeft and inBag[i]==0:
            if sum(inBag) == 0: # if no item in the bag yet
                print ()        # print a line break 
            newBag = inBag[:i] + [1] + inBag[i+1:]
            add_item = True
            memory = backtracking(info, memory, wLeft-w[i], vTotal+v[i], newBag)

    if add_item == False:    
        print ("inBag = {}, total value = {}".format(inBag, vTotal))
        if memory[0] == 0 or vTotal>memory[0] or vTotal==memory[0] and sum(inBag)<sum(memory[1][0]):  
            memory = [vTotal,[inBag]]
        elif vTotal==memory[0] and sum(inBag)==sum(memory[1][0]):
            memory[1].append(inBag)

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
    value,inBag = backtracking((w,v), [0,[[0]*n]], c, 0, [0]*n)

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



        # if sum(inBag) == 0:
        #     print ()

if __name__=="__main__":
    # w = [0,1,2,3,4,5]
    # t1,t2,t3 = -1, 3.5, 6
    # print(candidate_set(w,t3))

    w4 = [4,9,10,20,2,1]
    v4 = [400,1800,3500,4000,1000,200]
    c  = 20

    print(knapsack(w4,v4,c))

