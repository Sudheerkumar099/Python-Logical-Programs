lst = [1,2,3,4,5,6,7,8,9,10]

def linear_search(lst):
    n = int(input("Enter the number to search"))
    for i in lst:
        if (n == i):
            print(f"number found at {i}")
            return
    print("Number not Found")

def linear_search2(lst):
    n = int(input("Enter the number to search"))
    if n in lst:
        print("Number found in the list")
        return
    
    print("Number not found")

linear_search(lst)
linear_search2(lst)

