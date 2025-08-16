"""
24.Accept 5 employees name and salary and count average and total salar
"""
names = input("Enter 5 employee name").split()
salary = map(int, input("Enter salary").split())
total = sum(salary)
avg = total / 5
print("Total salary:",total)
print("avgerage:",avg)