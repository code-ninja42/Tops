#5. Write a Python program to add 'ing' at the end of a given string (length shouldbeat least 3). If the given string already ends with 'ing' then add 'ly' instead If thestring length of the given string is less than 3, leave it unchanged
s1 = input("Enter string")
print(s1)
if len(s1) == 5:
    if s1.endswith("ing"):
        new1 = s1[:2] + "ly"
        print(new1)
    else:
        new = s1[0:] + "ing"
        print(new)

    
else:
    print(s1)
    