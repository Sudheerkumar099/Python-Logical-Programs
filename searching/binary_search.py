
lst = [1,2,5,6,7,8,9,10]
def binary_search(lst):
    n = int(input("Enter the Number to search:\n"))
    left = 0
    right = len(lst)-1
   
    while (left<=right):
        mid = int((left+right)/2)
        if(n==lst[mid]):
            print(f"Number found at index {mid}")
            return
        elif (n>lst[mid]):
            left += 1
        else:
            right -=1
print("Number not found in the list")
binary_search(lst)