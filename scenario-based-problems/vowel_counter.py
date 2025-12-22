sentence = input("Enter a sentence \n")
k = int(input("enter the vowel count \n"))
a = 0 
e = 0 
i = 0
o = 0 
u = 0
for char in sentence :
    if char == 'a' or char == 'A':
        a = a + 1
    elif char == 'e' or char == 'E':
        e = e + 1
    elif char == 'i' or char == 'I':
        i = i + 1
    elif char == 'o' or char == 'O':
        o = o + 1
    elif char == 'u' or char == 'U':
        u = u + 1
        
if a > k:
    print("A",a)
if e > k :
    print("E",e)
if i > k :
    print("I" , i)
if o > k :
    print("O",o)
if u > k:
    print("U",u)

        