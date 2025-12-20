number = int(input("Enter a number: "))
temp = number
sum = 0

while number > 0:
    digit = number % 10
    sum = (sum *10) + digit
    number = number // 10

if sum == temp:
    print("PALINDROME")
else:
    print("NOT PALINDROME")