# 12. Write a Python program to convert a list of tuples into a dictionary
n = int(input("Enter number of tuples:"))
tuple_list = []
for i in range(n):
    k = input("Enter key:")
    v = input("Enter value:")
    tuple_list.append((k,v))
d = dict(tuple_list)
print(d)