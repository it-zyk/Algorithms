# Finds the smallest value in an array
def findSmallest(arr):
    # Stores the smallest value
    smallest = arr[0]
    # Stores the index of the smallest value
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index

# Sort array


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
            # Finds the smallest element in the array and adds it to the new array
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))  # 从arr表中异常最小的值 然后循环减少最小的元素排序
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
