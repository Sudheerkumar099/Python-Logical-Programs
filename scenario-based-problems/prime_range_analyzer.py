start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    else:
        return True
count = 0
for num in range(start, end+1):
    if is_prime(num):
       count = count+1

print(count)       

    