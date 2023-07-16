def insertionSort(array):
    for i in range(1, len(array)):
        min = array[i]
        j = i - 1
        while j >= 0 and min < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = min
data = [9, 5, 1, 4, 3]
print(data)
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)