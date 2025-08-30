"""
8. Write a program in C to count the total number of vowels or consonants in a
string
"""
str = input("Enter a string")
vowel = "aeiouAEIOU"
v = 0
c = 0
for ch in str:
    if ch in vowel:
        v += 1
    else:
        c += 1
print("Vowels:",v)
print("Consonants:",c)