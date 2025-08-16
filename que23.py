""""
AP to calculate swap 2 numbers with using of multiplication and division
"""
a = int(input("enter number"))
b = int(input("enter number"))
print(f"before swappign a: {a} and b: {b}")
a = a*b
b = a/b
a = a/b
print(f"After swapping: a = {a},b = {b}")