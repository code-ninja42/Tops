#7. Program to find Greatest Common Divisor of two numbers. For example, theGCD of 20 and 28 is 4 and the GCD of 98 and 56 is 14.
num1 = 20
num2 = 24
gcd = 1
for i in range(1,min(num1,num2)+1):
    if num1%i == 0 and num2%i==0:
        gcd = i
print(gcd)