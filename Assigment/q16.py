l1 = [1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2]
freq = {}
for num in l1:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for k in freq:
    print(k,":",freq[k],end = " ,")