def SequentialSearch(array, target):
    for i in range(0, len(array)):
        if (array[i] == target):
            return i
    return -1

array = [1, 5, 9, 54, 88, 99, 888]
target = 888
print(SequentialSearch(array, target))