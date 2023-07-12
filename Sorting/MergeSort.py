# # Merge Sort

# def merge_sort(list1):
#     # Dividing the list
#     if len(list1) > 1:
#         mid = len(list1) // 2 # Middle Value
#         left = list1[:mid]  # from the beginning
#         right = list1[mid:] # from the end
#         # Recursion Method
#         merge_sort(left)
#         print(".......Left........")
#         print(left)
#         merge_sort(right)
#         print(".......Right........")
#         print(right)
#         i = j = k = 0
#         # ................... #
#         # Merging Methods
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 list1[k] = left[i]
#                 i = i+1
#                 # k = k+1
#             else:
#                 list1[k] = right[j]
#                 j = j+1
#                 # k = k+1
#             k = k+1
#         # .................... #
#         # Check any values left or not
#         while i < len(left):
#             list1[k] = left[i]
#             i = i+1
#             k = k+1
#         # Check any values right or not
#         while j < len(right):
#             list1[k] = right[j]
#             j = j+1
#             k = k+1

# list1 = [20, 1, 50, 40, 2]
# merge_sort(list1)
# print("Sorted Array in Ascending Order:",list1)


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result = result + left[i:]
    result = result + right[j:]
    return result


arr = [5, 2, 8, 0, 1, 6]
sortedarr = mergesort(arr)
print(sortedarr)
