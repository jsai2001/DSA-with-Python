class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.adj = [[] for _ in range(self.V)]  # Adjacency List representation

    def addEdge(self, u, v):
        self.adj[u].append(v)  # Add w to v's list

    def printGraph(self):
        for i in range(self.V):
            print("Adjacency list of vertex", i)
            print("head ", i, end=" ")
            for neighbor in self.adj[i]:
                print("->", neighbor, end=" ")
            print("\n")

# Example usage
graph = Graph(4)
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 3)

graph.printGraph()
"""
This code defines a Graph class that uses an adjacency list to represent the graph.

The __init__ method initializes the number of vertices (V) and creates an adjacency list (adj) using a list comprehension. 
The adjacency list is a list of lists, where each inner list stores the vertices connected to a specific vertex.

The addEdge method adds an edge between two vertices (u and v) by appending v to the adjacency list of u.

The printGraph method iterates through the adjacency list and prints the connected vertices for each vertex.

The example creates a graph with four vertices and adds edges between them. 
Finally, it calls the printGraph method to display the adjacency list representation of the graph.
"""
