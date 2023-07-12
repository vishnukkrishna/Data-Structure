# DFS (Depth First Search)
class Node:
    def __init__(self) -> None:
        self.graph = {}

    def insert(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, v1, v2):
        if v1 not in self.graph or v2 not in self.graph:  # No is Working
            return None

        self.graph[v1].append(v2)

    def dfs(self, node, visited):
        if node not in self.graph:
            print("Node not present in this graph")
            return
        if node not in visited:
            print(node)
            visited.add(node)
            for i in self.graph[node]:
                self.dfs(i, visited)


obj = Node()
list1 = [89, 90, 70]
for i in list1:
    obj.insert(i)
# obj.insert(89)
# obj.insert(90)
# obj.insert(70)
obj.add_edge(89, 70)
obj.add_edge(70, 89)
obj.add_edge(89, 90)

obj.dfs(89, set())

# using dictionary
# class Graph:
#     def __init__(self, gdict=None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict

#     def addEdge(self, vertex, edge):
#         self.gdict[vertex].append(edge)

#     def bfs(self, vertex):
#         visited = [vertex]
#         queue = [vertex]
#         while queue:
#             deqVertex = queue.pop(0)
#             print(deqVertex)
#             for adjacentVertex in self.gdict[deqVertex]:
#                 if adjacentVertex not in visited:
#                     visited.append(adjacentVertex)
#                     queue.append(adjacentVertex)

#     def dfs(self, vertex):
#         visited = [vertex]
#         stack = [vertex]
#         while stack:
#             popVertex = stack.pop()
#             print(popVertex)
#             for adjacentVertex in self.gdict[popVertex]:
#                 if adjacentVertex not in visited:
#                     visited.append(adjacentVertex)
#                     stack.append(adjacentVertex)


# customDict = {"a": ["b", "c"],
#               "b": ["a", "d", "e"],
#               "c": ["a", "e"],
#               "d": ["b", "e", "f"],
#               "e": ["d", "f"],
#               "f": ["d", "e"]
#               }

# g = Graph(customDict)
# g.dfs("a")
# g.addEdge("e", "c")
# print(g.gdict["e"])
# print(g.gdict)
# g.dfs("a")
