# Heap MinHeap
class MinHeap:
    def __init__(self):
        self.heap=[]

    def parent(self,index):
        return (index-1)//2
    
    def left(self,index):
        return (2*index)+1
    
    def right(self,index):
        return (2*index)+2
        
    def insert(self,val):
        self.heap.append(val)
        curr = len(self.heap)-1
        while curr !=0 and self.heap[self.parent(curr)] > self.heap[curr]:
            self.heap[self.parent(curr)] , self.heap[curr] =  self.heap[curr] , self.heap[self.parent(curr)]
            curr = self.parent(curr)

    def heapify(self,index):
        r = self.right(index)
        l = self.left(index)
        small = index
        
        if l < len(self.heap) and self.heap[l] < self.heap[small]:
            small = l
        
        if r < len(self.heap) and self.heap[r] < self.heap[small]:
            small = r
        
        if small != index:
            self.heap[small] , self.heap[index] =  self.heap[index] , self.heap[small]
            self.heapify(small)

    def extract_min(self):
        if self.heap is None:
            return None
        # One value 
        elif len(self.heap)==1:
            return self.heap.pop()
        
        else:
            val = self.heap[0]
            self.heap[0]=self.heap.pop()
            self.heapify(0)
            return val
        
    # Heap sort 
    def heap_sort(self):
        sorted_array = []
        while self.heap:
            sorted_array.append(self.extract_min())
        return sorted_array
        
h1 = MinHeap()
list1 = [10,20,30,40,50,3,2,1,4]
for i in list1:
    h1.insert(i)
# h1.insert(10)
# h1.insert(20)
print("Min Heap")
print(h1.heap)
# print(h1.extract_min())

sorted_array = h1.heap_sort()
print("Sorted array (Heap Sort):")
print(sorted_array)


# import heapq

# heap = []
# heapq.heappush(heap,10)
# heapq.heappush(heap,1)
# heapq.heappush(heap,5)
# heapq.heappush(heap,6)
# heapq.heappush(heap,20)
# print(heap)

# heapq.heappop(heap)
# heapq.heappop(heap)
# print(heap)

# list1 = [3, 2, 1, 4, 7, 5]
# heap = [3, 2, 1, 4, 7, 5]
# heapq.heapify(list1)
# heapq.heappushpop(list1,22)
# heapq.heapreplace(list1,100)
# print(list1)
# heapq.nsmallest(2, heap)
# print(heap)
# heapq.nlargest(3, heap)
# print(heap)