"""1. Display This Information using printf
a. Your Name
b. Your Birth date
c. Your Age
d. Your Address"""
Name = input("Enter your name")
Birth_Year = int(input("Enter your birth year"))
Age = int(input("Enter your age"))
Address = input("Enter your address")

print(f"my name is{Name}", end=" ")
print(f"i was born in {Birth_Year}")
print(f"i am {Age} year old")
print(f"i live in {Address}")