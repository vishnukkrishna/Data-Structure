# # Traversal
# class Node:
#     def __init__(self, data):
#         self.data = data  # Assign data
#         self.ref = None # Initiliaze reference


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print_List(self):
#         if self.head is None:
#             print("LinkedList is empty")
#         else:
#             n=self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

# LL1 = LinkedList()
# LL1.print_List()


# .................................................. #
# Add / Insertion
# .................................................. #
# At the Beginning
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print_LL(self):
#         if self.head is None:
#             print("Linked List is empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

#     def add_begin(self, data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node


# LL1 = LinkedList()
# LL1.add_begin(10)
# LL1.add_begin(20)
# LL1.add_begin(30)
# LL1.print_LL()


# ..................................................... #
# At the End

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def printLL(self):
#         if self.head is None:
#             print("LinkedList is empty")

#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data, "--->", end="")
#                 n = n.ref

#     # def add_begin(self, data):
#     #     new_node = Node(data)
#     #     new_node.ref = self.head
#     #     self.head = new_node


#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n = n.ref
#             n.ref = new_node


# LL1 = LinkedList()
# # LL1.add_begin(10)
# LL1.add_end(100)
# # LL1.add_begin(20)
# LL1.printLL()


# ............................................. #
# In Between Nodes
# After Nodes
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def printLL(self):
#         if self.head is None:
#             print("LinkedList is empty")

#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data, "--->", end=" ")
#                 n = n.ref

#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n = n.ref
#             n.ref = new_node


#     def add_after(self,data,x):
#         n = self.head
#         while n is not None:
#             if x == n.data:
#                 break
#             n = n.ref
#         if n is None:
#             print("Node is not present in LinkedList")
#         else:
#             new_node = Node(data)
#             new_node.ref = n.ref
#             n.ref = new_node

# LL1 = LinkedList()
# LL1.add_end(20)
# LL1.add_after(40, 20)
# LL1.printLL()


# Before Nodes


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def printLL(self):
#         if self.head is None:
#             print("LinkedList is empty")

#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data, "--->", end=" ")
#                 n = n.ref

#     def add_begin(self, data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node

#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n = n.ref
#             n.ref = new_node

    # def add_before(self, data, x):
    #     if self.head is None:
    #         print("Linked list is empty")
    #         return
    #     if self.head.data == x:
    #         new_node = Node(data)
    #         new_node.ref = self.head
    #         self.head = new_node
    #         return
    #     n = self.head
    #     while n.ref is not None:
    #         if n.ref.data == x:
    #             break
    #         n = n.ref
    #     if n.ref is None:
    #         print("Node is not Found!")
    #     else:
    #         new_node = Node(data)
    #         new_node.ref = n.ref
    #         n.ref = new_node

#     def add_after(self, data, x):
#         n = self.head
#         while n is not None:
#             if x == n.data:
#                 break
#             n = n.ref
#         if n is None:
#             print("Node is not present in LinkedList")
#         else:
#             new_node = Node(data)
#             new_node.ref = n.ref
#             n.ref = new_node


# LL1 = LinkedList()
# LL1.add_begin(10)
# LL1.add_before(20, 10)
# # LL1.add_before(30, 10)
# # LL1.add_after(40, 20)
# LL1.printLL()
# print()
# ..................................................... #


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Print LinkedList
    def printLL(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "---->", end=" ")
                n = n.ref

    # Add node at the begining of the list
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node


    # Add node at the end of the list
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                n = n.ref
            n.ref = new_node

    # Add node before 
    def add_before(self, data, x):
        if self.head is None:
            print("LinkedList is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in LinkedList")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # Delete the node from the beginning
    def deleteBegin(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        self.head = self.head.ref

    # Delete the node from any values 
    def delete_value(self, value):
        if self.head is None:
            print("LinkedList is empty")
            return

        # If the value to be deleted is in the head
        if self.head.data == value:
            self.head = self.head.ref
            return

        n = self.head
        while n.ref is not None:
            if n.ref.data == value:
                break
            n = n.ref

        if n.ref is None:
            print("Node with the given value not found")
        else:
            n.ref = n.ref.ref

    # Delete the node from the before
    def delete_before(self, x):
        if self.head is None or self.head.ref is None:
            print("LinkedList is empty or has only one element")
            return

        if self.head.ref.data == x:
            self.head = self.head.ref
            return

        n = self.head
        while n.ref.ref is not None:
            if n.ref.ref.data == x:
                n.ref = n.ref.ref
                return
            n = n.ref

        print("Node with value", x, "not found")

    # Delete the node from the after
    def delete_after(self, x):
        if self.head is None:
            print("LinkedList is empty")
            return

        n = self.head
        while n is not None:
            if n.data == x and n.ref is not None:
                n.ref = n.ref.ref
                return
            n = n.ref

        print("Node with value", x, "not found or is the last node")

    # LinkedList reverse
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.ref
            current.ref = prev
            prev = current
            current = next_node
        self.head = prev


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(40)
LL1.add_begin(50)
LL1.add_begin(60)
LL1.add_begin(70)
# LL1.add_before(20, 10)
# LL1.add_before(30, 10)
# LL1.add_after(40, 20)
# LL1.deleteBegin()
# LL1.delete_after(40)
# LL1.deleteAnyvalue(20)
# LL1.printLL()
print()
# LL1.delete_value(20)
LL1.reverse()
# LL1.printLL()
print()

# ..................................................................




