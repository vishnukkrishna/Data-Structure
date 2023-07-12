# Selection Sort in Python


# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         if min_index != i:
#             arr[i], arr[min_index] = arr[min_index], arr[i]
#             print(data)
#     return arr
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


data = [22, 11, 55, 44, 66, 33]
selection_sort(data)
print("Sorted Array in Ascending Order:", data)
