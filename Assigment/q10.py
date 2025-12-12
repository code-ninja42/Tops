#10.Write a Python program to get unique values from a list
l1=[1,1,2,2,3,3]

unique_l1=[]
[unique_l1.append(i) for i in l1 if i not in unique_l1]
print(unique_l1)