"""
11.Write a program in C to read a sentence and replace lowercase characters with
uppercase and vice versa.
"""
s1 = input("Enter string")
print(s1)
s2 = ""
for c in s1:
    if c.isupper():
        s2 += "".join(c.lower())
    else:
        s2 += "".join(c.upper())
print(s2)