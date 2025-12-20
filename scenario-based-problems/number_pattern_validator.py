number = input("Enter a number: ")

for i in range (len(number)-1):
    if int(number[i])  > int(number[i+1]): 
        print("NO")
        break
else:
    print("YES")