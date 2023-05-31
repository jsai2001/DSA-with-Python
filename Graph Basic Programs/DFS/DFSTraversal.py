# DFS Traversal for the entire graph , 
# even if we have a disconnection
from collections import defaultdict
# This class represents a directed graph ,
# using adjacency list representation
class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
    # Function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    # DFS Utility function , which contains main logic
    def DFSUtil(self,v,visited):
        # Mark current node as visited
        visited.add(v)
        print(v,end=' ')
        # recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)
    def DFS(self):
        # Create a set to store all visited vertices
        visited = set()
        # Calling this recursive helper function , vertices by vertice
        # To iterate the whole tree , by DFS
        # This for loop helps us in dealing with disconnected graphs
        for vertex in self.graph:
            if vertex not in visited:
                self.DFSUtil(vertex,visited)
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# Function call
g.DFS()

# Time complexity: O(V+E)
# Auxilary Space: O(V) , extra visited array of size V is required