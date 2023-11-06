def linearSearch(data, list):
    size = len(list)
    if data in list:
        index = [c+1 for c in range(size) if data == list[c]]
        return index
    else:
        return -1
    

list1 = [1,2,3,4,5,6,7,8,9,10]
data = 4
result = linearSearch(data, list1)
if result == -1:
    print("Invalid linear search")
else:
    print("The value is Here:",result)