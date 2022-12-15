


# ------------------- 1. Location Optimisation -------------------------



def ideal_place(relevant:list) -> list[int]:

    n = len(relevant)

    # base cases
    if n == 0:          # choose any point if no point to be considered
        return [0,0]
    elif n <= 2:            # if less than two points, any point within the  
        return relevant[0]  # rectangle of the two points can be the median.
    
    x = [relevant[i][0] for i in range(len(relevant))]
    y = [relevant[i][1] for i in range(len(relevant))]

    # find index of the median
    k1, k2 = n//2, n//2
    if n%2 == 0:    # 2 medians if got even number of elements
        k1 -= 1

    # find the x and y median 
    xmedian = find_median(x, k1, k2)
    ymedian = find_median(y, k1, k2)

    return [xmedian,ymedian]



def find_median(lst:list, k1:int, k2:int) -> int:

    # set the left and right boundary for finding the median
    L,R = 0, len(lst)

    while True:
        
        pivot = median_of_medians(lst,L,R)
        i,j = partitioning(lst,L,R,pivot) 
            # lst[0:i] < pivot  where i >= 0
            # lst[i:j] = pivot, where j > i
            # lst[j: ] > pivot, where j <= len(lst)
        print(lst, i,j ,pivot)

        if i<=k1<j or i<=k2<j:
            return lst[i]
        if j <= k1:  
            L = j
        elif i >= k2:
            R = i



def median_of_medians(lst:list, L:int, R:int) -> int:

    while R-L > 1: 

        p = L
        for i in range(L,R,5):
            upper_bound = min(i+5, R)
            small_median_index = insertion_sort(lst,i, upper_bound)
            lst[p], lst[small_median_index] = lst[small_median_index], lst[p]
            p += 1
        R = p
    
    return lst[L]



def insertion_sort(lst:list, L:int, R:int) -> None:

    for i in range(L+1,R):
        target = lst[i]
        j = i-1
        while j>=L and lst[j]>target:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = target
    return (L+R)//2



def partitioning(lst:list, L:int, R:int, pivot:int) -> tuple[int,int]:

    i,j= L, R       # i-L will be the number of element(s) in lst[L:R] < pivot
                    # R-j will be the number of element(s) in lst[L:R] > pivot
                    # j-i will be the number of element(s) in lst[i:j] == pivot


    for k in range(L,R):

        if lst[k] < pivot:
            lst[i],lst[k] = lst[k], lst[i]
            i += 1

        elif lst[k] > pivot:
            while j-1>L and lst[j-1]>pivot:
                if j-1 == k:
                    return (i,j-1)
                j-=1
            lst[j-1], lst[k] = lst[k], lst[j-1]
            if lst[k] < pivot:
                lst[k],lst[i] = lst[i], lst[k]
                i+= 1

    return (i,j)





if __name__ == "__main__":


    rel = [ [1,1],[1,1],[10,10],[30,30],[30,30],
            [1,1],[1,1],[10,10],[30,30],[30,30],
            [1,1],[1,1],[10,10],[30,30],[30,30],
            [1,1],[1,1],[10,10],[30,30],[30,30],
            [1,1],[1,1],[10,10],[30,30],[30,30],
            
            [1,1],[1,1],[10,10],[30,30],[30,30],
            [1,1],[1,1],[10,10],[30,30],[30,30],
            [1,1],[1,1],[10,10],[30,30],[30,30],
            [1,1],[1,1],[10,10],[30,30],[30,30],
            [1,1],[1,1],[10,10],[30,30],[30,30],
            
            [1,1],[1,1],[10,10],[30,30],[30,30],
            [1,1],[1,1],[10,10],[30,30],[30,30],

            [1,1],[1,1],[10,10],[50,50],[50,50],
            
            [50,50],[50,50],[100,100],[101,101],[101,101],
            [50,50],[50,50],[100,100],[101,101],[101,101],
            
            [50,50],[50,50],[100,100],[101,101],[101,101],
            [50,50],[50,50],[100,100],[101,101],[101,101],
            [50,50],[50,50],[100,100],[101,101],[101,101],
            [50,50],[50,50],[100,100],[101,101],[101,101],
            [50,50],[50,50],[100,100],[101,101],[101,101],
            
            [50,50],[50,50],[100,100],[101,101],[101,101],
            [50,50],[50,50],[100,100],[101,101],[101,101],
            [50,50],[50,50],[100,100],[101,101],[101,101],
            [50,50],[50,50],[100,100],[101,101],[101,101],
            [50,50],[50,50],[100,100],[101,101],[101,101],]


    print(ideal_place(rel))



