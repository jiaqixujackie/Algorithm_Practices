

def ideal_place(relevant:list) -> list[int]:
    """
    find a point on a grid such that sum of the Manhattan 
    distance from the selected point to all other relevant 
    points is minimized. The median of median and quick 
    select algorithm were used. 

    :param relevant: a list of [x,y] coordinates
    :return: a list of two integer [i,j] such that sum of 
             the Manhattan distance from [i,j] to all the
             [x,y] coorindates is minimized. 

    Time Complexity: O(N)
        O(N+N) creating the x and y list.
        O(N) for finding each of the find_median() function
    Space Complexity: O(N)
        O(N) for input parameter
        O(N+N) for x and y lists
        O(N) for median of medians 
    """

    n = len(relevant)

    if n == 1:
        return [0,0]
    elif n <= 2:
        return relevant[0]
    
    k = n//2

    x = [relevant[i][0] for i in range(n)]
    y = [relevant[i][1] for i in range(n)]

    xmedian = find_median(x,k)
    ymedian = find_median(y,k)

    return [xmedian,ymedian]



def build_sublists(lst:list) -> list[list]:
    """
    This function split a long list of N integers into sublists 
    of size 5 based on index.

    :param lst: a list of integers
    :return: a list of sublist of size 5

    Time Complexity: O(N)
    Space Complexity: O(N)
        O(N) for both input parameter and local variable sublists
        O(1) for local variable n and i
    """
    n = len(lst)
    sublists = [lst[i:i+5] for i in range(0,n,5)]
    return sublists


def sort_sublists(lst:list[list]) -> None:
    """
    given a list of sublists of length 5, use insertion sort 
    to sort every sublist.

    :param lst: a list of N/5 sublists of size 5 or less
    
    Time Complexity: O((1+2+3+4) * (N/5)) ≈ O(N)
    Space Complexity: O(N) for input list, in-place auxiliary
    """
    n = len(lst)
    for sublist in lst:
        insertion_sort(sublist)


def insertion_sort(lst:list) -> None:
    """
    this function sorts a list of integer on the original list.

    :param lst: a list of 5 or less integers. 

    Time Complexity: O(1+2+3+4) ≈ O(1)
    Space Complexity: O(5)≈O(1) for input lst, in-place auxiliary.
    """
    n = len(lst)
    for i in range(1,n):
        target = lst[i]
        j = i-1
        while j>=0 and lst[j]>target:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = target


def get_medians(lst:list[list]) -> list:
    """
    given a list of sorted sublist (mostly length of 5), this 
    function replace every sublist with the median of that sublist.

    :param lst: a list of sublist of 5 integers or less.

    Time Complexity: O(N/5) ≈ O(N)
    Space Complexity: O(N) for input lst, in-place auxiliary. 
    """
    n = len(lst)

    for i in range(n-1):
        lst[i] = lst[i][2]
    n = len(lst[-1])
    lst[-1] = lst[-1][n//2]


def get_pivot(lst:list) -> int:
    """
    Implement the median of medians algorithm to find a good pivot 
    in lst for partitioning. (Inspired by FIT2004 studio 4 problem 4).

    :param lst: a list of integers
    :return: the pivot selected to represent the median of medians,this 
             pivot is not neccessary the median of the entire list, but 
             it reduces the size of the input lst by at least 30%.

    Time Complexity: O(N)
        O(N/5**0 + N/5/5**1 + N/5**2 + ... ) = O(5N/4) ≈ O(N) 
    Space Complexity: O(N)
        O(N) for input lst
        O(N) for build_sublist()
        O(1) for sort_sublists() and get_medians() because changes were
        made directly on the input list rather than creating a new list.
    """
    medians = lst
    while len(medians)>1:
        medians = build_sublists(medians)
        sort_sublists(medians)
        get_medians(medians)
    return medians[0]


def partitioning(lst:list,pivot:int) -> tuple[int,int,list]:
    """
    rearrange the input list (lst) such that the lst[0:i]<pivot,
    lst[i:j]==pivot, and lst[j:]>pivot.

    :param lst: a list of integers 
    :param pivot: an integer in the list that can reduce the the
                  size of the input list by at least 30%. 
    :result: (i,j,lst). integers in the input lst have been
             rearranged such that lst[:i]<pivot, lst[i:j]==pivot 
             and lst[j:]>pivot.
    
    Time Complexity: O(2N)
        O(1) for checking each element in the lst
        O(1) for comparing every element in the lst against the pivot
        We have N element in the lst, so the overall time complexity 
        is N * (O(1) + O(1)) = O(2N) ≈ O(N)
    Space Complexity: O(N) for input lst, O(1) in-place auxiliary.
    """
    i,j= 0, len(lst)-1
    for k in range(len(lst)):
        if lst[k] < pivot:
            lst[i],lst[k] = lst[k], lst[i]
            i += 1
        elif lst[k] > pivot:
            while j>0 and lst[j]>pivot:
                if j == k:
                    return i,j,lst
                j-=1
            lst[j], lst[k] = lst[k], lst[j]
            if lst[k] < pivot:
                lst[k],lst[i] = lst[i], lst[k]
                i+= 1


def find_median(lst:list,index:int) -> int:
    """
    use the median of medians and the quick select algorithm 
    to find the median of a given list of integers.

    :param lst: a list of integers 
    :param index: an integer representing the index of an 
                  element in a sorted list.
    :return: the median of the entire list. 

    Time Complexity: O(N)
        In each iteration we need O(5N/4) for finding a good 
        pivot and O(N) for partitioning, which is O(9N/4). 
        Since each iteration reduce the size of the input lst 
        by at least 30%, The complexity at worst case is:
        O(9N/4) + O(9N/4 * 0.7) + O(9N/4 * 0.7**2) + ...
        = O(9N/4 * (1 + 0.7 + 0.7**2 + 0.7**3 + ...) )
        = O(9N/4 * 10/3) = O(90N/12) ≈ O(7N) ≈ O(N)
    Space Complexity: O(N)
        O(N) for input lst
        O(N) for get_pivot()
        O(1) for partitioning(), because changes were made directly
             on the input list, rather than creating a new list.
    """
    while True:
        pivot = get_pivot(lst)
        i,j,lst = partitioning(lst, pivot)
        if j < index:
            index -= j
            lst = lst[j:]
        elif i > index:
            lst = lst[:i]
        else:
            return lst[i]



if __name__ == "__main__":
    # x = [93,66,14,90,68,89,66,17,22,2,20,96,90,49,17,16,90,1,88,4,42,90,72,43,35,60,91,90,44,71,63,72,71]
    # print(find_median(x, len(x)//2+1))
    
    relevant1 = [[5,8], [7,5], [9, 1], [0,7], [1,9], [2,1]]
    relevant2 =[[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]]
    relevant3 = [[0,0], [2,1],[1,2]]
    print(ideal_place(relevant3))

