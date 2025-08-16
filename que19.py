"""
19.Calculate compound interest
"""
principal = int(input("Enter principal"))
rate = int(input("Enter R"))
time = int(input("Enter "))
A = principal * (1 +rate / 100)** time
ci = A -principal
print("Compound Interest:",ci)