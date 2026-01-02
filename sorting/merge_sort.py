def merge_sort(lst):
    if len(lst)<=1:
        return lst
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left,sorted_right)

def merge(left,right):
    result = []
    i = 0
    j = 0
    while i<len(left) and j <(len(right)):
        if left[i]<right[j]:
            result.append(left[i])
            i= i+1
        else:
            result.append(right[j])
            j = j+1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

lst = [12,3,45,6,7,8,6,5,4,3,2,123,4,5,6,7,8,9,7,6,543]
print(merge_sort(lst))
