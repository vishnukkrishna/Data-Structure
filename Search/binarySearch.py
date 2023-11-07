# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


array = [1,2,3,4,5,6,7,8,9,10]
data = 5
result = binary_search(array, data)
print("The elements is in", result, "position")