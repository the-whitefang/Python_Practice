'''list-->Ordered--default index
can store elements of different data types
'''
list1 = []
print(list1,type(list1))
list2 = [20,30,40,]
print(list2,type(list2))
list4 = list([100,200,300,400])
print(type(list4))
list5 = [101,393,29,883]
list5.append(344)
print(list5)
list5.extend([929,873,838])
print(list5)
list5.insert(0,43)#index, value
print(list5)
list5.insert(4,50)#index, value
print(list5)
list5.remove(929)
print(list5)
list5.pop()
print(list5)
list5.pop(5)
print(list5)
del list5[2]
print(list5)