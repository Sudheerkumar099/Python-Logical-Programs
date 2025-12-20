number = int(input("Enter a number: "))
temp = number
sum = 0
while number > 0:
    digit = number % 10
    sum = sum + (digit ** 3)
    number = number // 10

if sum == temp:
    print("YES")
else:
    print("NO")