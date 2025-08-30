"""
emove characters from a string except alphabets
"""
strr = input("Enter a string")
alpha = ""
for ch in strr:
    if ch.isalpha():
        alpha += ch
print("Only alphabets:",alpha)