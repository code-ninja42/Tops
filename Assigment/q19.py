def unique_element(l1):
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2
l1 = [1,2,3,1,2,4,5]

print(unique_element(l1))

#2nd Way
def unique_element(l1):
    return list(set(l1))
l1 = [1,2,3,1,2,4,5]
print(unique_element(l1))