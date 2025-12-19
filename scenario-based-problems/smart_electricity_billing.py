units = int(input("Enter the number of electricity units consumed: "))
bill = 0
if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = (100 * 3) + ((units - 100) * 5)
else:
    bill = (100 * 3) + (100 * 5) + ((units - 200) * 8)

if (bill > 300):
    bill = bill + (bill * 0.10)

print(f"Total electricity bill: {bill:.2f}")
