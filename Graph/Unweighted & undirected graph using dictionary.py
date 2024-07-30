# Dictionary Implementation of undirected unweighted graph
"""
We can self.gdict[vertexuse a dictionary where there are all vertices as keys and the value of each vertex is a list containing all
                             the other vertices, the key vertex is connected to.
"""
class Graph:
    def __init__(self):
        self.gdict = {}

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() or vertex2 in self.gdict.keys():
            # Undirected graph therefore both vertices will occur in each other lists
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
        else:
            print("One or both of the vertices not present in the graph.")

    def addVertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
        else:
            print("Vertex already present in the dictionary.")
            return

    def print_graph(self):
        if not self.gdict:
            print("Graph doesn't exist.")
            return
        for i in self.gdict:
            print(i,":",self.gdict[i])

    def remove_edge(self, vertex1, vertex2):
        if not self.gdict:
            print("Graph doesn't exist.")
        elif vertex1 not in self.gdict.keys() or vertex2 not in self.gdict.keys():
            print("One or both of the provided vertices not present in the graph.")
        elif vertex1 not in self.gdict[vertex2] or vertex2 not in self.gdict[vertex1]:
            print(f"No edge present between {vertex1} and {vertex2}")
        else:
            self.gdict[vertex1].remove(vertex2)
            self.gdict[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if not self.gdict:
            print("Graph doesn't exist.")
        elif vertex not in self.gdict.keys():
            print(f"Provided vertex {vertex} not in the graph.")
        else:
            # First using a for loop remove the vertex from all the lists of connection
            for i in self.gdict[vertex]:
                self.gdict[i].remove(vertex)
            del self.gdict[vertex]

    def bfs_traversal(self, vertex):
        # In BFS, we visit a node then it's all neighbours first. Then move on to explore the surrounding of neighbours
        # Time Complexity - O(V+E) || Space Complexity - O(V)
        if not self.gdict:
            print("Graph doesn't exist.")
            return
        if vertex not in self.gdict.keys():
            print("Vertex not present in graph.")
            return
        visited = set()
        visited.add(vertex)
        q = [vertex]
        while q:
            n = q.pop(0)
            print(n, end=" ")
            for i in self.gdict[n]:
                if i not in visited:
                    visited.add(i)
                    q.append(i)

    def dfs_traversal(self, vertex):
        # In DFS, we go as deep as possible by connecting the immediate node first instead of neighbours.
        # Time Complexity - O(V+E) || Space Complexity - O(V)
        if not self.gdict:
            print("Graph doesn't exist.")
            return
        if vertex not in self.gdict.keys():
            print("Vertex not present in graph.")
            return
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

g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "D")
g.addEdge("A", "D")
g.print_graph()
g.bfs_traversal("A")

