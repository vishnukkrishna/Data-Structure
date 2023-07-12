# Hash Table
class Hash_Table:
    def __init__(self, size):
        self.size = size
        self.arr = [[] for x in range(size)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size

    def add(self, key, value):
        h = self.get_hash(key)
        found = False

        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break

        if not found:
            self.arr[h].append((key, value))

    def get_item(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def delete(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


obj = Hash_Table(10)
obj.add("name", "vishnu")
obj.add("place", "palakkad")
print(obj.get_item("place"))
print(obj.delete("place"))
print(obj.arr)


class Hashtable:
    def __init__(self):
        self.limit = 10
        self.arr = [[] for i in range(self.limit)]

    def sethash(self, key, value):
        h = self.gethash(key)
        # print(h)
        self.arr[h] = value
        # print(self.arr[h])

    def gethash(self, key):
        h = 0
        for i in key:
            h += ord(i)
            return h % self.limit

    def search(self, key):
        h = self.gethash(key)
        return self.arr[h]

    def delitem(self, key):
        h = self.gethash(key)
        del self.arr[h]


obj = Hashtable()
# obj.sethash('name','12345678)
# obj.sethash('place','malappuram')
obj.sethash("age", 23)
# print(obj.getitem('age'))
# print(obj.delitem('name'))
print(obj.delitem("age"))
print(obj.search("age"))
print(obj.arr)
