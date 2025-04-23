def InsertionSort_recursion(arr, n = 1):
    # Stop condition (If n equals the number of element, it means we've finished sorting.)
    if (n == len(arr)):
        return arr
    # Store the current element to be inserted
    key = arr[n] # Set key as the element now we want to insert
    j = n - 1 # Set j as the index of the element that is right before n
    # Shift elements of the sorted portion that are greater than key
    # The following loop will perform until either j < 0 or key is greater than or equal to arr[j] 
    while (j >= 0 and arr[j] > key):
        arr[j + 1] = arr[j]
        j = j - 1
    # Insert the key at the correct position
    arr[j + 1] = key
    return InsertionSort_recursion(arr, n + 1)

nums = [999, 666, 557, 66, 87, 99, 2, 1, 0]
print(InsertionSort_recursion(nums))
