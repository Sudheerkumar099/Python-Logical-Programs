def partition(lst,low,high):
    pivot = lst[low]
    i = low + 1
    j = high
    while True:
        while i<=j and lst[i]<=pivot:
            i = i+1
        while i<=j and lst[j]>=pivot:
            j = j-1
        if i<=j:
            lst[i],lst[j]=lst[j],lst[i]
        else:
            break
    lst[low],lst[j] = lst[j],lst[low]
    return j

def quick_sort(lst,low,high):
    if low < high:
        pivot = partition(lst,low,high)
        quick_sort(lst,low,pivot -1 )
        quick_sort(lst,pivot+1,high)

lst = [8,6,5,3,4,2,4,786,57,9239,934,98,2,8]
quick_sort(lst,0,len(lst)-1)
print(lst)