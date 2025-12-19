T = int(input("Enter the seconds: "))

cycle = T % 90
if cycle == 0:
    cycle = 90

if 1 <= cycle <= 30:
    print("RED")
elif 31 <= cycle <= 45:
    print("YELLOW")
else:
    print("GREEN")
