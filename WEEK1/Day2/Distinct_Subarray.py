'''
program to input any integer number num1 and find its double num2 and check
whether the digits present in num2 are there in num1 and each of the num2's digit's position
is different from that of the positions of digits in num1.
'''
# printing the array elements using list comprehension
num1 = int(input("Enter the Starting number: "))
num2 = int(input("Enter the ending number: "))
array = [ i for i in range(num1,num2+1)]
print(array)

#printing the values using nested loop
result = []
for i in range(len(array)):
    for j in range(i,len(array)):
        result. append(array[i:j+1])
print(result)

#printiing the values using list comprehension method
result = [array[i:j+1] for i in range(len(array))
          for j in range(i,len(array))]
ctr = 0
for i in result:
    if sum(i) % 2 != 0:
        ctr += 1
print(ctr)


