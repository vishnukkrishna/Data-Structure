# Bubble sort in Python


def BubbleSort(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


data = [4, 1, 3, 6, 5, 2, 8, 7]
print("UnSorted Array:", data)
BubbleSort(data)
print("Sorted Array in Ascending Order:", data)
# data = []
# limit = int(input("Enter the  limit:"))
# print("Enter the numbers:")
# for k in range(limit):
#     data.append(int(input()))

# BubbleSort(data)
# print("Sorted Array in Ascending Order:",data)
