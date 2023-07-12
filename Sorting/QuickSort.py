# Quick Sort


def pivot_place(list1, first, last):
    pivot = list1[first]
    left = first + 1
    right = last
    while left <= right and list1[left] <= pivot:
        left = left + 1
    while left <= right and list1[right] >= pivot:
        right = right - 1
    if right < left:
        pass
        # break
    else:
        list1[left], list1[right] = list1[right], list1[left]
    list1[first], list1[right] = list1[right], list1[first]
    return right


def quick_sort(list1, first, last):
    if first < last:
        p = pivot_place(list1, first, last)
        quick_sort(list1, first, p - 1)
        quick_sort(list1, p + 1, last)


data = [2, 1, 3, 5, 4, 6, 7]
n = len(data)
quick_sort(data, 0, n - 1)
print("Sorted Array in Ascending Order:", data)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


data = [2, 1, 3, 5, 4, 6]
result = quick_sort(data)
print("Sorted Array in Ascending Order:", result)
