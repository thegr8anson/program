def SelectionSort_Recursive(arr, n = 0):
    if (n == len(arr) - 1):
        return arr
    # Assume the min element is arr[n].
    min_index = n 
    # Find the actual min element.
    for i in range(n, len(arr)):
        # If the assumption is correct, the following condition wouldn't meet.
        if (arr[i] < arr[min_index]): 
            min_index = i
    # If the min element is the element we had assumed, then we don't need to swap. 
    if (min_index != n):   
        arr[min_index], arr[n] = arr[n], arr[min_index]
    return SelectionSort_Recursive(arr, n + 1)

nums = [555, 999, 666, 557, 87, 99, 2, 1, 0, 2.5, -2.5]
print(SelectionSort_Recursive(nums))

