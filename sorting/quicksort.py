lst = [7,4,7,100,9,9,5,4,8,4,45,68]

def quick_sort(lst):
    n=len(lst)
    if n<=1:
        return lst
    else:
        pivot = lst.pop()
        
    higher = []
    lower = []
    for i in lst :
        if i<pivot:
            lower.append(i)
        else :
            higher.append(i)
    lst = quick_sort(lower)+[pivot]+quick_sort(higher)
    return lst

lst= quick_sort(lst)
print(lst)


