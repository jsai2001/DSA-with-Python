# DFS traversal for CONNECTED GRAPH
# For disconnected graphs , we need to start DFS traversal from a vertex
# And later on , we need to loop through visited array , and perform DFS
# On unvisited nodes , Code will be typically same as below

# Python program to print DFS Traversal
from collections import defaultdict
# Represents a directed graph using adjacency list
class Graph:
    # Constructor
    def __init__(self):
        # Default dictionary to store the graph
        self.graph = defaultdict(list)
    # Function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    # A function used by DFS
    def DFSUtil(self,v,visited):
        # Mark the current node as visited and print it
        visited.add(v)
        print(v,end=' ')
        # Recur for all vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)
    # Function to do DFS traversal
    # DFSUtil is the utility function for DFS
    def DFS(self,v):
        # create a set to store the visited vertices
        visited = set()
        # Call Recursive helper function for DFS traversal
        self.DFSUtil(v,visited)

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print("DFS traversal from vertex 2")
g.DFS(2)

# Time complexity : O(V+E)
# Space Complexity: O(V+E) , as we need an extra visited array of size V , 
# And stack size for iterative call to DFS function
