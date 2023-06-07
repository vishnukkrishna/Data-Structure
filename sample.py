# Binary Search Tree
# class BST:
#     def __init__(self,key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None

#     def insertion(self,data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key == data:
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.insertion(data)
#             else:
#                 self.lchild = BST(data)
#         else:
#             if self.rchild:
#                 self.rchild.insertion(data)
#             else:
#                 self.rchild = BST(data)
    
#     def search(self,data):
#         if self.key == data:
#             print("Data is Found")
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("Data is not present in the Tree")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("Data is not present in the Tree")

#     def preorder(self):
#         print(self.key, end=" ")
#         if self.lchild:
#             self.lchild.preorder()
#         if self.rchild:
#             self.rchild.preorder()

#     def inorder(self):
#         if self.lchild:
#             self.lchild.inorder()
#         print(self.key, end=" ")
#         if self.rchild:
#             self.rchild.inorder()
    
#     def postorder(self):
#         if self.lchild:
#             self.lchild.postorder()
#         if self.rchild:
#             self.rchild.postorder()
#         print(self.key, end=" ")

#     def delete(self,data):
#         if self.key is None:
#             print("Tree is empty")
#             return
#         if data < self.key:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(data)
#             else:
#                 print("Given node is not present in the Tree")
#         elif data > self.key:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(data)
#             else:
#                 print("Given node is not present in the Tree")
#         else:
#             if self.lchild is None:
#                 temp = self.rchild
#                 self = None
#                 return temp
#             if self.rchild is None:
#                 temp = self.lchild
#                 self = None
#                 return temp
#             node = self.rchild
#             while node.lchild:
#                 node = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(node.key)
#         return self
        
#     def min_node(self):
#         current = self
#         while current.lchild:
#             current = current.lchild
#         print("Node with smallest key is: ", current.key)

#     def max_node(self):
#         current = self
#         while current.rchild:
#             current = current.rchild
#         print("Node with largest key is: ", current.key)

    # def validation(self):
    #     if self.key is None:
    #         return True
    #     if self.lchild and self.lchild.key > self.key:
    #         return False
    #     if self.rchild and self.rchild.key < self.key:
    #         return False
    #     if self.lchild is not None and not self.lchild.validation():
    #         return False
    #     if self.rchild is not None and not self.rchild.validation():
    #         return False
    #     return True
    

# root = BST(None)
# list1 = [1,4,2,9,7]
# for i in list1:
#     root.insertion(i)

# print(root.validation())
# root.search(4)
# root.delete(7)
# root.preorder()
# print()
# root.inorder()
# print()
# root.postorder()
# print()
# root.min_node()
# root.max_node()

# ----------------------------------------------- #

# Heap DSA
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
#         while curr != 0 and self.heap[self.parent(curr)] > self.heap[curr]:
#             self.heap[self.parent(curr)], self.heap[curr] = self.heap[curr], self.heap[self.parent(curr)]
#             curr = self.parent(curr)

#     def heapify(self,index):
#         l = self.left(index)
#         r = self.right(index)
#         small = index

#         if l < len(self.heap) and self.heap[l] < self.heap[small]:
#             small = l
#         if r < len(self.heap) and self.heap[r] < self.heap[small]:
#             small = r
#         if small != index:
#             self.heap[small], self.heap[index] = self.heap[index], self.heap[small]
#             self.heapify(small)

#     def extract_min(self):
#         if self.heap is None:
#             return None
#         elif len(self.heap)==1:
#             return self.heap.pop()
#         else:
#             val = self.heap[0]
#             self.heap[0]=self.heap.pop()
#             self.heapify(0)
#             return val
        
#     def heap_sort(self):
#         sort_array = []
#         while self.heap:
#             sort_array.append(self.extract_min())
#         return sort_array
    
# h1 = MinHeap()
# h1.insert(70)
# h1.insert(20)
# h1.insert(30)
# h1.insert(40)
# h1.insert(50)
# h1.insert(4)
# h1.insert(5)
# h1.insert(2)
# print("Min Heap")
# print(h1.heap)
# print(h1.extract_min())

# sorted_array = h1.heap_sort()
# print("Sorted array (Heap Sort):")
# print(sorted_array)


# ----------------------------------------------------- #

# Prifix Trie
# class TrieNode:
#     def __init__(self):
#         self.child = {}
#         self.end = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self,word):
#         node = self.root
#         for char in word:
#             if char not in node.child:
#                 node.child[char] = TrieNode()
#             node = node.child[char]
#         node.end = True

#     def search(self,word):
#         node = self.root
#         for char in word:
#             if char not in node.child:
#                 return False
#             node = node.child[char]
#         return node.end
    
# tr = Trie()
# tr.insert("vishnu")
# tr.insert("her")
# print(tr.search("vishnu"))

# --------------------------------------------------------- #

# DFS
# class Node:
#     def __init__(self):
#         self.graph = {}
#     def insert(self,vertex):
#         self.graph[vertex] = []

#     def add_edge(self,v1,v2):
#         if v1 not in self.graph or v2 not in self.graph:
#             return None
#         self.graph[v1].append(v2)

#     def dfs(self,node,visited):
#         if node not in self.graph:
#             print("Node not present in this graph")
#             return
#         if node not in visited:
#             print(node)
#             visited.add(node)
#             for i in self.graph[node]:
#                 self.dfs(i,visited)


# obj = Node()
# obj.insert(89)
# obj.insert(90)
# obj.insert(70)

# obj.add_edge(89,70)
# obj.add_edge(70,89)
# obj.add_edge(89,90)

# obj.dfs(89,set())

# ------------------------------------------------- #

def rob(nums):
    prev1 = 0
    prev2 = 0

    for num in nums:
    #   print(prev1,"prev1")
    #   print(prev2,"prev2")
      maxi = max(prev1, prev2 + num)
      print(maxi,"maxi")
      prev2 = prev1
      prev1 = maxi

    return prev1

nums = [1,2,10,11,7,3]
print(rob(nums))