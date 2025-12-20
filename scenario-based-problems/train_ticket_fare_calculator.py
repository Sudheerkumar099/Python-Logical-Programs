distance = int(input("Enter the number of kilometers: "))
fare = distance * 2
age = int(input("Enter your age: "))

if age < 12:
    discount = fare * 0.50
    fare -= discount
elif age >= 65:
    discount = fare * 0.30
    fare -= discount

print(fare)
