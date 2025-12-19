n = int(input("Enter a positive integer: "))
while(n<0):
    n = int(input("Please enter a positive integer: "))
hn=0
for i in range(1,n+1):
    hn=hn+1/i     
print("Harmonic Number is:",hn)