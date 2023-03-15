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


