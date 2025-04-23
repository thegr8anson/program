def insertion_sort_recursive(arr, n = None):
    if (n is None):
        n = len(arr)
    # Base case
    if (n <= 1):
        return arr
    # Sort the first n-1 elements
    insertion_sort_recursive(arr, n - 1)
    # Insert the last element into the sorted array
    last = arr[n - 1]
    j = n - 2
    while (j >= 0 and arr[j] > last):
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last
    return arr

nums = [999, 666, 557, 66, 87, 99, 2, 1, 0]
print(insertion_sort_recursive(nums))