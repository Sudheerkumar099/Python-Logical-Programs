m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
m4 = int(input("Enter marks for subject 4: "))
m5 = int(input("Enter marks for subject 5: "))

while (m1 > 100 or m2 > 100 or m3 > 100 or m4 > 100 or m5 > 100):
    print("Invalid marks entered. Please enter marks between 0 and 100.")
    m1 = int(input("Enter marks for subject 1: "))
    m2 = int(input("Enter marks for subject 2: "))
    m3 = int(input("Enter marks for subject 3: "))
    m4 = int(input("Enter marks for subject 4: "))
    m5 = int(input("Enter marks for subject 5: "))

average = (m1 + m2 + m3 + m4 + m5)/5
if m1 < 35 or m2 < 35 or m3 < 35 or m4 < 35 or m5 < 35:
    print("Fail")
elif (average >= 75):
    print("DISTINCTION")
else:
    print("PASS")
