balance = int(input("Enter the balance : "))
n = input("Enter the number of transactions: ")
lst = []
for i in range(int(n)):
    amount = int(input("Enter the amount : "))
    if amount <= balance and amount % 100 == 0:
        balance = balance - amount
        lst.append("SUCCESS")
    else:
        lst.append("FAILED")
for status in lst:
    print(status)
print(f"Remaining balance: {balance}")
print ("Thank You")
