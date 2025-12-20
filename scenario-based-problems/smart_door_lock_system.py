set_pin = input("Set your 4-digit PIN: ")

while len(set_pin) != 4:
    set_pin = input("Invalid PIN length.\nPlease enter only  4-digit PIN: ")
attempt = 2
for i in range(3):
    pin = input("Enter your PIN to unlock the door: ")
    if (pin == set_pin):
        print("ACCESS GRANTED")
        break
    else:
        print("wrong Pin")
        if attempt > 0:
            print(f"only {attempt} attempts left")
    attempt -= 1
else:
    print("LOCKED")
