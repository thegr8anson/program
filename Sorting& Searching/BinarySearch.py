def BinarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    while (left <= right):
        if (nums[mid] == target):
            return mid
        elif (nums[mid] > target):
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    return -1

nums = [1, 5, 9, 54, 88, 99, 888]
target = 0
print(BinarySearch(nums, target))
