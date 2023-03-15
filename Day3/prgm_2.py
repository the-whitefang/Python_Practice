'''
Paired outputs
For each element in
'''

mylist = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]

#using list and tuple
result = []
for i in list_b:
    result.append((i,mylist.index(i)))
print(result)

#using Dictionary Comprehension
print({i:mylist.index(i)
      for i in list_b})

#using Dictionary with regular For Loop
result1 ={}
for i in list_b:
    result1[i] = mylist.index(i)
print(result1)