"""
9. Write a program in C to find the maximum number of characters in a string
"""
str = input("Enter a string")
max_char = ''
max_count = 0
for ch in str:
    count =str.count(ch)
    if count > max_count:
        max_count = count
        max_char = ch
print(f"character :{max_char} and appearing:{max_count}")
