# Traversal in Doubly linked lists
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.nref = None
#         self.pref = None


# class DoublyLL:
#     def __init__(self):
#         self.head = None

#     def print_LL(self):
#         if self.head is None:
#             print("Linked List is Empty")

#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data,"-->" ,end=" ")
#                 n = n.nref


#     def print_LL_reverse(self):
#         if self.head is None:
#             print("Linked List is Empty")

#         else:
#             n = self.head
#             while n.nref is not None:
#                 n = n.nref
#             while n is not None:
#                 print(n.data,"-->", end=" ")
#                 n = n.pref


# dl1 = DoublyLL()
# dl1.print_LL()
# dl1.print_LL_reverse()

# ............................................................... #

#  Add/Insertion Operations


# At the beginning and Add End
class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is Empty")

        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nref

    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("Linked List is Empty")

        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.pref

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is Not Empty!")

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self, data, x):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in Doubly Linked List")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is Empty")
            return
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in Doubly Linked List")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node


dl1 = DoublyLL()
# dl1.insert_empty(10)
dl1.add_begin(10)
# dl1.add_end(30)
# dl1.add_after(20,10)
# dl1.add_after(30,20)
dl1.add_before(20, 10)

dl1.print_LL()
dl1.print_LL_reverse()
