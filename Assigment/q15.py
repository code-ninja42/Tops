n = int(input("Enter number"))
l1 = []
a,b = 0,1
for i in range(n):
    l1.append(a)
    a,b = b,a+b
print(l1)