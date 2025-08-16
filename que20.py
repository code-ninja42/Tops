""""
Accept monthly salary from the user and deduct 10% insurance premium,
10% loan installment find out of remaining salary
"""
salary = int(input("Enter your s"))
premium = salary - (salary * 0.10)
loan = premium - (premium * 0.10)
print(f"Remaining Salary:{loan}")