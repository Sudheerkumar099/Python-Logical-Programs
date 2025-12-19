n = int(input("Enter a Number: "))
i=2
while(i**2<=n):
    while(n%i==0):
        print(i)
        n=n//i
    i=i+1
if(n>1):
    print(n)

