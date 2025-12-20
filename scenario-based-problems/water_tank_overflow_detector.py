capacity = 1000
n = int(input("Enter the number of  inflows : "))
lst = []
count = 1
for i in range(n):
    inflow = int(input(f"Enter the inflow{count} amount: "))
    lst.append(inflow)
    if capacity >0  :
        capacity -= inflow
        count += 1

print(count-1)
        
