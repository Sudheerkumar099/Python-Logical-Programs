lst = [4,3,2,5,1,6,7,8,9,10]
for i in range(1,len(lst)):
    insert_index = i
    current_value = lst.pop(i)
    for j in range(i-1,-1,-1):
        if lst[j]>current_value:
            insert_index = j
    lst.insert(insert_index,current_value)


def insertion_sort(lst):
    for i in range(1,len(lst)):
        insert_index = i
        current_value = lst.pop(i)
        for j in range(i-1,-1,-1):
            if lst[j]>current_value:
                insert_index = j
        lst.insert(insert_index,current_value)
    print(lst)

insertion_sort(lst)


