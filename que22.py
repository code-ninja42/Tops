"""
2.Calculate compound interest (Compound Interest formula:
a. Formula to calculate compound interest annually is given by:
Amount= P(1 + R/100)t
b. Compound Interest = Amount – P
"""
principal = int(input("Enter principal"))
rate = int(input("Enter R"))
time = int(input("Enter "))
A = principal * (1 +rate / 100)** time
ci = A -principal
print("Compound Interest:",ci)