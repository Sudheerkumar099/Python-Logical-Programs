lst = [1,5,7,2,6,8,3,4,9,10]
for i in range(len(lst)-1):
    min_index = i
    for j in range(i+1,len(lst)):
        if(lst[j]<lst[min_index]):
            min_index = j
    min_value = lst.pop(min_index)
    lst.insert(i,min_value)



def selection_sort(lst):
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1,len(lst)):
            if (lst[j]<lst[min_index]):
                min_index = j
        min_value = lst.pop(min_index)
        lst.insert(i,min_value)
    print(lst)
    
selection_sort(lst)