'''
program to print the square of the odd numbres and cube of the even numbers
present in the matrix.
'''

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

#List Comprehension version of printing Square of the Odd numbers and Cube of the Even numbers
print(
    [
        j**2 if j % 2 != 0 else j**3
        for i in mat
        for j in i
     ]
      )

#Regular for loop method of printing Square of the Odd numbers and Cube of the Even numbers
result = []
for row in mat:
    row_data =[]
    for column in row:
        if column % 2 != 0:
            row_data.append(column**2)
        else:
            row_data.append(column**3)
    result.append(row_data)
print(result)