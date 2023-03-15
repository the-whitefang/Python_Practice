'''

'''

#example 1,2,3,4,5,6,7,3,8,2
#num1 = 1+2+3+4+2 = 11
#num2 = 56738 + 11 56749



#using for loop
# num1=[]
# num2 = 0
# num3 =0
# for i in str.split(','):
#     num1.append(int(i))
# a = num1.index(5)
# b = num1.index(8)
# for i in num1:
#     if i< a or i>b:
#         num2 += i
#
# for i in num1:
#     if i>a and i<b:
#         num3 = (num3*10)+i
# print(num3)
# # print(num3+num2)

#using list comprehension
array = list(map(int,input().split(",")))
number1 = sum(array[:array.index(5)]) + sum(array[array.index(8)+1:])
l = array[array.index(5):array.index(8)+1]
number2 =""
for i in l:
    number2 += str(i)
print(int(number2)+number1)