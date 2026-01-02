def partition(lst,low ,high):
    p = lst[low]
    i = low + 1
    j = high
    while True:
        while i<=j and lst[i]<=p:
            i = i+1
        while i<=j and lst[j]>=p:
            j = j-1
        if i<=j:
            lst[i],lst[j]=lst[j],lst[i]
        else:
            break
    lst[low],lst[j] = lst[j],lst[low]
    return j 

def quicksort(lst,low,high):
    if low < high:
        pivot = partition(lst,low,high)
        quicksort(lst,low,pivot-1)
        quicksort(lst,pivot+1,high)

lst = [5,8,1,2,6,3,9,4,7]
quicksort(lst,0,len(lst)-1)
print(lst)

    