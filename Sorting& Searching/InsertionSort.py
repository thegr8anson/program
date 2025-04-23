def InsertionSort(array, n = None):
    if (n == None):
        n = len(array)
    for i in range(1, n):
        # Store the current element to be inserted
        key = array[i]
        j = i - 1
        # Shift elements of the sorted portion that are greater than key
        while (j >= 0 and array[j] > key):
            array[j+1] = array[j]
            j = j - 1
        # Insert the key at the correct position
        array[j+1] = key
    return array


nums = [999, 666, 557, 87, 99, 2, 1, 0]
print(InsertionSort(nums))

