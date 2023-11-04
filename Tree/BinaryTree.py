# Binary Search Tree
class BST:
    def __init__(self, key):
        # Create a node
        self.key = key
        self.lchild = None
        self.rchild = None

    # Insertion
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        # Check the duplicate value
        if self.key == data:
            return
        if self.key > data:
            # Left child part
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)  # Create a new node means creating an object
        else:
            # Right side part
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)  # Create a new node means creating an object

    # Searching
    def search(self, data):
        if self.key == data:
            print("Node is found!")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in the Tree!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in the Tree!")

    # Traversal Methods
    # pre-order
    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    # in-order
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()

    # post-order
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")

    # Deletion
    def delete(self, data):
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given node is not present in the Tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given node is not present in the Tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self
    # Minimum node
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("Node with smallest key is: ", current.key)
    
    # Maximum node
    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("Node with largest key is: ", current.key)
    
    # BST validation
    def BST_Validation(self):
        if self.key is None:
            return True
        if self.lchild and self.lchild.key > self.key:
            return False
        if self.rchild and self.rchild.key < self.key:
            return False
        if self.lchild is not None and not self.lchild.BST_Validation():
            return False
        if self.rchild is not None and not self.rchild.BST_Validation():
            return False
        return True


root = BST(None)
list1 = [1, 4, 2, 9, 7]
for i in list1:
    root.insert(i)

print("--BST Validate or Not--")
print(root.BST_Validation())
print("----Search----")
root.search(55)

print("----Pre-Order----")
root.preorder()
print()
print("----In-Order----")
root.inorder()
print()
print("----Post-Order----")
root.postorder()
print()

root.delete(11)
print("----Pre-Order----")
root.preorder()
print()

root.min_node()
root.max_node()
