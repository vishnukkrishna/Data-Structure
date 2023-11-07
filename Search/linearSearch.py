# Linear Search
def linearSearch(data, list):
    size = len(list)
    if data in list:
        index = [c+1 for c in range(size) if data == list[c]]
        return index
    else:
        return -1
    

list1 = [2,1,3,5,4,6,8,7,9,10]
data = 4
result = linearSearch(data, list1)
if result == -1:
    print("Invalid linear search")
else:
    print("The value is Here:",result)