# sentence = input("Enter a sentence: ")
# vowels = "aeiouAEIOU"
# vowel_count = 0
# for char in sentence:
#     if char in vowels:
#         vowel_count = vowel_count+1
# print(vowel_count)

sentence = input("Enter a sentence ")
k = int(input("enter the vowel count"))
a = 0 
e = 0 
i = 0
o = 0 
u = 0
for char in sentence :
    if char == 'a':
        a = a + 1
    elif char == 'e':
        e = e + 1
    elif char == 'i':
        i = i + 1
    elif char == 'o':
        o = o + 1
    elif char == 'u':
        u = u + 1

if a > k:
    print("a",a)
elif e > k :
    print("e",e)
elif i > k :
    print("i" , i)
elif o > k :
    print("o",o)
elif u > k:
    print("u",u)

        