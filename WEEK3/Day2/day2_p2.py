"""
Job Scheduling Algorithm Implementation
"""

lst = [190, 90, 80, 60, 50, 40, 30, 20, 20, 10]
dd = [2, 7, 3, 4, 2, 7, 3, 5, 1, 1]
final = []
profit = []

for i in range(max(dd), 0, -1):  # i slots
    for j in range(len(dd)):  # customers
        if i == dd[j]:
            final.append(lst[j])  # profit
    print(final)
    profit.append(max(final))

    final.remove(max(final))
    print(profit)

print("total :", profit[::-1])
print("total :", sum(profit))


'''profit list   lst = [190,90,80,60,50,40,30,20,20,10]

slot list dd =  [2  ,7 , 3, 4, 2, 7, 3, 5, 1, 1]

to support list 

final = []
profit = []

loop from  i = max slot max(dd) to 1
	loop j = 0 to slot list (dd) length - 1
		when we find the slot value
			we append the corresponding value to final list
		now we append the maximum value of final to profit list and remove maximum value fro the final list

finally,
print profit list in reverse order
print the sum of the profit list'''