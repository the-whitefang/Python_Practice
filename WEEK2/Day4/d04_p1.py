'''
Linear Search in python
'''


def Linear_Search(array, n, x):
    ''' searching for the element in the array sequentially'''
    for i in range(0, n):
        if array[i] == x:
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 4
n = len(array)
result = Linear_Search(array, n, x)
if result == -1:
    print("Element not found.")
else:
    print("Element found at index: ",result)