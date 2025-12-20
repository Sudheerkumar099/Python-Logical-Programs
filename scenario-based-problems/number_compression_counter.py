number = int(input("Enter a number: "))
count = 0
while number % 2 == 0:
    number /= 2
    count += 1
print(count)