# #1. Write a python program to sum of the first n positive integers
num = int(input("Enter number"))
sum_of = 0
for i in range(1,num+1):
    sum_of += i
print(sum_of)