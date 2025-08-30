"""
6. Write a program in C to count the total number of alphabets, digits and special
characters in a string.
"""
str = input("Enter a string")
alpha = 0
dig = 0
special = 0
for ch in str:
    if ch.isalpha():
        alpha += 1
    elif ch.isdigit():
        dig += 1
    else:
        special += 1
print("Alphabets:",alpha)
print("Digits:",dig)
print("Special char",special)