### Bipartite Graph

Solve the problem of determining whether a given graph is bipartite using an adjacency list representation. Here's a step-by-step explanation along with the code and analysis of time and space complexity.

- **Time Complexity:** \(O(V + E)\)

- **Space Complexity:** \(O(V)\)

### Understanding the Problem

A graph is bipartite if we can split its set of vertices into two disjoint sets \( U \) and \( V \) such that every edge \( (u, v) \) either connects a vertex in \( U \) to a vertex in \( V \) or vice versa. In other words, there should be no edges connecting vertices within the same set.

### Approach to Solution

We can use BFS (Breadth-First Search) or DFS (Depth-First Search) to determine if the graph is bipartite. Here's the detailed approach using BFS:

1. **Initialization**: Use a color array to store the color of each vertex. Initialize all vertices with -1, indicating they are uncolored.
2. **BFS Traversal**: For each unvisited vertex, start a BFS traversal:
   - Color the starting vertex with color 0.
   - For each adjacent vertex, assign the opposite color.
   - If an adjacent vertex already has the same color as the current vertex, the graph is not bipartite.
3. **Repeat**: Perform the above steps for all components of the graph.

### Implementation

Here is the Python implementation:

```python
from collections import deque

def isBipartite(V, adj):
    # Initialize color array with -1
    color = [-1] * V
    
    # Function to perform BFS
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        
        while queue:
            u = queue.popleft()
            
            for v in adj[u]:
                if color[v] == -1:  # If the vertex is uncolored
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:  # If the vertex has the same color as its neighbor
                    return False
        return True
    
    # Check all vertices (handle disconnected graph)
    for i in range(V):
        if color[i] == -1:  # If the vertex is uncolored
            if not bfs(i):
                return False
    
    return True

# Example usage
V = 4
adj = [
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2]
]

print(isBipartite(V, adj))  # Output: True
```

### Explanation

1. **Initialization**: The `color` array is initialized with -1 for all vertices.
2. **BFS Traversal**: The `bfs` function performs BFS starting from an uncolored vertex:
   - The starting vertex is colored with 0.
   - For each adjacent vertex, if it is uncolored, it is colored with the opposite color. If it is already colored and has the same color as the current vertex, the graph is not bipartite.
3. **Handle Disconnected Graph**: The outer loop ensures that we check all components of the graph.

### Time Complexity

The time complexity of this algorithm is \( O(V + E) \), where:
- \( V \) is the number of vertices.
- \( E \) is the number of edges.

This is because each vertex and each edge are processed once during the BFS traversal.

### Space Complexity

The space complexity is \( O(V) \) due to the following:
- The `color` array which stores the color of each vertex.
- The queue used for BFS, which in the worst case, can store all vertices.

This provides an efficient way to determine if a given graph is bipartite using its adjacency list representation.