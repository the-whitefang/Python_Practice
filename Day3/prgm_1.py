mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

#
print([j**2 if j % 2 != 0 else j**3 for i in mat for j in i ])

#
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

#
print( [ele**2 if ele%2!=0 else ele**3
        for row in mat
        for ele in row]
       )

#
print( [[ele**2 if ele%2!=0 else ele**3
        for ele in row]
        for row in mat]
       )