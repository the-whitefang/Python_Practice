'''
Python program to create and print a new_list by following the given rules:
1. create two Lists, list1 and list2 containing integer values
2. check whether the double of each element in list1 is present in list2 or not.
3. if present then add the element of list1 to new_list
'''
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
new_list =[]

for i in list1:
    if i*2 in list2:
        new_list.append(i)

print(new_list)