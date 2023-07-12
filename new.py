# class BST:
#     def __init__(self,key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None

#     def insert(self, data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key == data:
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = BST(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = BST(data)

#     def inorder(self):
#         if self.lchild:
#             self.lchild.inorder()
#         print(self.key, end=" ")
#         if self.rchild:
#             self.rchild.inorder()


# root = BST(None)

# list1 = [2,3,1,4,5,7]
# for i in list1:
#     root.insert(i)

# root.inorder()
# print()


# class MinHeap:
#     def __init__(self):
#         self.heap=[]

#     def parent(self,index):
#         return (index-1)//2

#     def left(self,index):
#         return (2*index)+1

#     def right(self,index):
#         return (2*index)+2

#     def insert(self,val):
#         self.heap.append(val)
#         curr = len(self.heap)-1
#         while curr !=0 and self.heap[self.parent(curr)] > self.heap[curr]:
#             self.heap[self.parent(curr)] , self.heap[curr] =  self.heap[curr] , self.heap[self.parent(curr)]
#             curr = self.parent(curr)

#     def heapify(self,index):
#         r = self.right(index)
#         l = self.left(index)
#         small = index

#         if l < len(self.heap) and self.heap[l] < self.heap[small]:
#             small = l

#         if r < len(self.heap) and self.heap[r] < self.heap[small]:
#             small = r

#         if small != index:
#             self.heap[small] , self.heap[index] =  self.heap[index] , self.heap[small]
#             self.heapify(small)

#     def extract_min(self):
#         if self.heap is None:
#             return None
#         # One value
#         elif len(self.heap)==1:
#             return self.heap.pop()

#         else:
#             val = self.heap[0]
#             self.heap[0]=self.heap.pop()
#             self.heapify(0)
#             return val

#     def heap_sort(self):
#         sorted_array = []
#         while self.heap:
#             sorted_array.append(self.extract_min())
#         return sorted_array

# h1 = MinHeap()
# h1.insert(10)
# h1.insert(20)
# h1.insert(30)
# h1.insert(40)
# h1.insert(50)
# h1.insert(3)
# h1.insert(4)
# h1.insert(6)
# print("Min Heap")
# print(h1.heap)
# # print(h1.extract_min())

# sorted_array = h1.heap_sort()
# print("Sorted array (Heap Sort):")
# print(sorted_array)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_count = 0
# even_sum = 0
# for num in numbers:
#     if num % 2 == 0:
#         even_sum += num
#     else:
#         odd_count += 1

# print("Count of odd numbers:", odd_count)
# print("Sum of even numbers:", even_sum)


# num = int(input("Enter the number: "))
# for i in range(2, num):
#     if num%i==0:
#         print("Not a prime number")
#         break
# else:
#     print("Prime number")


# def decortor(func):
#     def sample():
#         func()
#         print("HI")
#     return sample

# @decortor
# def new():
#     print("I")

# new()

# def generator(start,end):
#     curr = start
#     while curr<=end:
#         yield curr
#         curr +=1

# for num in generator(1, 5):
#     print(num)
