# Topological Sort

"""
PseudoCode - We use stack in this sort

if a vertex depends on currentVertex:
    Go to vertex and come back to currentVertex
else:
    Push currentVertex into the stack

"""


class Graph:
    def __init__(self):
        self.gdict = {}

    def addVertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
        else:
            print("Vertex already present in the graph.")
            return

    def addEdge(self, vertex1, vertex2):
        if vertex1 not in self.gdict.keys() or vertex2 not in self.gdict.keys():
            print("Either one or both of the vertices not in the graph.")
            return
        elif vertex1 in self.gdict[vertex2]:
            print("Edge already present b/w the vertices")
            return
        else:
            self.gdict[vertex2].append(vertex1)
            self.gdict[vertex1].append(vertex2)

    def print_graph(self):
        if not self.gdict:
            print("No graph found.")
            return
        for i in self.gdict.keys():
            print(i, ":", self.gdict[i])

    def bfs(self, vertex):
        q = [vertex]
        visited = set()
        visited.add(vertex)
        while q:
            n = q.pop(0)
            print(n, end=" ")
            for i in self.gdict[n]:
                if i not in visited:
                    visited.add(i)
                    q.append(i)

    def dfs(self, vertex):
        q = [vertex]
        visited = set()
        while q:
            n = q.pop(0)
            if n not in visited:
                print(n, end=" ")
                visited.add(n)
            for i in self.gdict[n]:
                if i not in visited:
                    q.append(i)

    def topologicalHelp(self, vertex, visited, stack):
        visited.append(vertex)

        for i in self.gdict[vertex]:
            if i not in visited:
                self.topologicalHelp(i, visited, stack)

        stack.insert(0, vertex)

    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.gdict):
            if k not in visited:
                self.topologicalHelp(k, visited, stack)

        print(stack)


g = Graph()
g.addVertex("a")
g.addVertex("b")
g.addVertex("c")
g.addVertex("d")
g.addVertex("e")
g.addEdge("a", "b")
g.addEdge("a", "c")
g.addEdge("b", "d")
g.addEdge("d", "e")
g.addEdge("c", "e")
g.print_graph()
g.topologicalSort()
