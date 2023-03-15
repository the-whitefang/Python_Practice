'''
List Comprehension
'''
#for loop version of printing a List
result = []
for i in range(11):
    result.append(i)
print(result)

#List Comprehension version of printing a List
print([i for i in range(11)])

#for loop version --> odd elements
l1 = []
for i in range(11):
    if i % 2 != 0:
        l1.append(i)
print(l1)

#odd elements --> List Comprehension method
print([i for i in range(11) if i %2 != 0 ])

#for loop version of printing if the numbers of the list is odd else if even print its square
l1 = []
for i in range(11):
    if i % 2 != 0:
        l1.append(i)
    else:
        l1.append(i**2)
print(l1)

#List Comprehenson version of printing if the numbers of the list is odd else if even print its square
print([i if i % 2 != 0 else i**2 for i in range(11)])

