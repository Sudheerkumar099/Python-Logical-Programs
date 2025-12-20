sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in sentence:
    if char in vowels:
        vowel_count = vowel_count+1
print(vowel_count)
