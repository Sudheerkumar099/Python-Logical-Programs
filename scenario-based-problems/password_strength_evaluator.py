password = input("Enter your password: ")

digits = 0
uppercase = 0
for char in password:
    if char>='0' and char<='9':
        digits = digits + 1
    elif char>='A' and char<='Z':
        uppercase = uppercase + 1

if len(password) >= 8 and digits >= 1 and uppercase >= 1:
    print("STRONG")
else:
    print("WEAK")
