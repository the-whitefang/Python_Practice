'''

'''

list1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2 = ['y', 'tor', 'e', 'eps', 'ay', "None", 'le', 'n']
s=""
list2.reverse()
for i in range(0,len(list1)):
    s += list1[i]+list2[i]+" "
s.replace("None","")
print(s)
