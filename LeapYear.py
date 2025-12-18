year = int(input("Enter a year: "))
while len(str(year)) !=4:
    print("Enter a valid Year")
    year = int(input("Enter a year again: "))
    
if(year %4==0 and year %100 !=0 or year%400==0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

