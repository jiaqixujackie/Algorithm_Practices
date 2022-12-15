

# ------------ find geometric median using radix sort. time 
#              complexity is O(MN) rather than O(N) where M
#              is number of digits of the largest number  ----------


def ideal_place(relevant):
    return geometric_median(relevant)


def geometric_median(relevant):

    if len(relevant) <= 2:
        return relevant[0]
    
    else:
        x = [relevant[i][0] for i in range(len(relevant))]
        y = [relevant[i][1] for i in range(len(relevant))]
        xmedian = find_median(x)
        ymedian = find_median(y)
        return [xmedian, ymedian]


def find_median(lst):

    maximum = find_max(lst)
    n = length_of_max(maximum)
    
    new_lst = lst 
    for p in range(n):
        counting = count_table(new_lst,p)
        accFreq = accumulation(counting)
        new_lst = rearrange(new_lst, accFreq, p)

    n = len(new_lst)
    if n%2 == 1:
        median = new_lst[n//2]
    elif n%2 == 0:
        left, right = new_lst[n//2-1], new_lst[n//2]
        median = (left+right)//2
    return median


def find_max(lst):
    maximum = 0
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum


def length_of_max(num):
    n = 0
    while num > 0:
        n += 1
        num = num//10
    return n


def count_table(lst, p):
    table = [0]*10

    for num in lst:
        digit = get_digit(num, p)
        table[digit] += 1
    return table


def get_digit(num,p):
    for i in range(p):
        num = num//10
    return num%10


def accumulation(count):
    table = [0]*10
    for i in range(1,10):
        table[i] = table[i-1] + count[i-1]
    return table 


def rearrange(lst, accFreq, p):
    table = [None] * len(lst)
    for i in range(len(lst)):
        digit = get_digit(lst[i], p)
        position = accFreq[digit]
        table[position] = lst[i]
        accFreq[digit] += 1
    return table



if __name__ == "__main__":
    relevant = [[5,8], [7,5], [9, 1], [0,7], [1,9], [2,1]]
    print(ideal_place(relevant))
