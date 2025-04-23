def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    # Base case
    if n == 1:
        return arr
    # One pass of bubble sort
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    # Recursive call for the rest of the array
    return bubble_sort_recursive(arr, n - 1)

nums = [11111, 999, 666, 77, 88, 66, 55, 3, 1]
print(bubble_sort_recursive(nums))

