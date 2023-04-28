'''
Create Array with +ve and -ve numbers, then move all the -ve numbers towards starting of the array
and print the final output
'''

n = int(input())

num = list(map(int,input().strip().split()))[:n]

# Approach 1
print("Approach 1:\n")
i = 0
for j in range(0,n-1):
    if num[j] < 0:
        temp = num[j]
        num[j] = num[i]
        num[i] = temp
        i += 1

print(num)

# Approach 2
print("Approach 2:\n")
num1 =[]
num2 =[]
ctr1 =0
ctr2 =0
for i in range(0,n-1):

    if num[i] < 0:
        num1.append(num[i])
    else:
        num2.append(num[i])

print(num1+num2)