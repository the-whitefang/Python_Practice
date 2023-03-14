#program to count the number of pairs which is equivalent to the given check value
a = [1,2,7,4,5,6,0,3]
check = 6
Count = 0
pair = []
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]+a[j] == check:
            Count += 1
            pair.append(j)
        else:
            continue

print(Count)