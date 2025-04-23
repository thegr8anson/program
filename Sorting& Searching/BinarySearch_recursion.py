def BinarySearch_recursion(nums, target, left = None, right = None):
    if (left == None and right == None):
        left = 0
        right = len(nums) - 1
    mid = (left + right) // 2
    if (left > right):
        return -1
    elif (nums[mid] == target):
        return mid
    elif (nums[mid] > target):
        # right = mid - 1
        return BinarySearch_recursion(nums, target, left, mid - 1)
    elif (nums[mid] < target):
        # left = mid + 1
        return BinarySearch_recursion(nums, target, mid + 1, right)

nums = [1, 5, 9, 54, 88, 99, 888]
target = 888
print(BinarySearch_recursion(nums, target))