def SequentialSearch_recursion(arr, target, n = 0):
    if (n == len(arr)):
        return -1
    elif (arr[n] == target):
        return n
    return SequentialSearch_recursion(arr, target, n + 1)

nums = [1, 5, 9, 54, 27, 50, 88, 66, 99, 888, 555]
target = 0
print(SequentialSearch_recursion(nums, target))   