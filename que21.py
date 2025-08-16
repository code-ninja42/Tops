"""
1.Accept 2 numbers from user and swap 2 numbers with using 3rd variable
and without using 3rd variable
"""
a = int(input("enter number a"))
b = int(input("enter number b"))
temp = 0
temp = a
a = b
b = temp
print("After swapping a",a)
print("After swapping b", b)

#without using 3rd variable 
a,b = b,a
print("after swapping a:", a)
print("after swapping b", b)