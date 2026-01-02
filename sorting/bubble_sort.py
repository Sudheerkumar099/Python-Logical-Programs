lst=[8,5,3,4,6,7,1,0,2,9]
for i in range(len(lst)+1):
    for j in range(len(lst)-i-1):
        if(lst[j]>lst[j+1]):
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp 
print(lst)