# # Queue
# queue = []
# # Adding the element in queue
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)

# # Delete the element
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
# queue.insert(0, 10)
# queue.insert(1, 20)
# queue.insert(2, 30)
# queue.insert(3, 40)
# print(queue)

# print(queue.pop())
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())

# Queue implementation in Python
class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()
print(q.size())

# import collections
# q = collections.deque()
# print(q)

# q.appendleft(10)
# q.appendleft(20)
# q.appendleft(30)
# print(q)

# print(q.pop())


# import queue

# q = queue.Queue()
# q.put(10)
# q.put(20)
# q.put(30)
# print(q)

# print(q.get())
# print(q.get())
# print(q.get())
