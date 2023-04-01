'''
*** Quick Sort ***
'''


def Partition(array, low, high):  # Partition function to partition the array elements in such a way that the
    # numbers before the pivot element is less than the pivot element and the ones
    # to its right is greater than the pivot element
    pivot = array[high]  # storing the last element of the array
    i = low - 1
    for j in range(low, high):  # partitioning is done here
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low,
              high):  # Quick sort function is used to sort the elements that are left unsorted after the partition
    if low < high:
        pi = Partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


data = [8, 7, 6, 1, 0, 9, 2]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print("Sorted Array in Ascending order: ")
print(data)
