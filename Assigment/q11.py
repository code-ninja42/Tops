# 11.Write a Python program to unzip a list of tuples into individual lists.
list_of_tuple = [(1,'a'),(2,'b'),(3,'c')]
l1,l2 = zip(*list_of_tuple)
l1 = list(l1)
l2 = list(l2)
print(l1)
print(l2)