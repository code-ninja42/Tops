"""
1. Write a program in C to find the length of a string without using library
functions.
"""
name = input("enter string")
print(name)
c = 0
for i in name:
    c += 1
print("Lenth of string",c)