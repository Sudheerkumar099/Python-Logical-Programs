binary = input("Enter a binary number: ")

decimal = 0
power = 0

for i in binary[::-1]:
    if i == "1":
     decimal = decimal + (2 ** power)
    power = power +1

print(f"The decimal equivalent of {binary} is : {decimal}")