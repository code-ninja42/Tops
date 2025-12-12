#8. Write a Python program to check whether a list contains a sublist.
l1 = [1,2,3,4,5]
l2 = [1,2]
for i in l2:
    if i in l1:
        print("yes")
    else:
        print("no")
