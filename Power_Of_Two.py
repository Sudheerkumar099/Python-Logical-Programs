n= int(input("Enter a number: "))
if(n<=0 or n<31):
    for i in range(0,31,1):
        power=2**i
        if(power<=2**n):
         print(f"2  power {i} = {power}")
         
