#4. Write a Python program to get a single string from two given strings, separatedbya space and swap the first one characters of each string

s1 = "Hello"
s2 = "World"
new = s2[0] + s1[1:]
new1 = s1[0]+s2[1:] 
result = new + " " +new1
print(result)


 
