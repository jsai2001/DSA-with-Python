### Bellman-Ford Algorithm

The Bellman-Ford algorithm is used to find the shortest paths from a single source vertex to all other vertices in a weighted graph. It can handle graphs with negative weight edges, unlike Dijkstra's algorithm.

- **Time Complexity:** \(O(V x E)\)

- **Space Complexity:** \(O(V + E)\)

Here's the Python implementation of the Bellman-Ford algorithm:

```python
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices in the graph
        self.edges = []    # List to store all the edges in the graph

    def add_edge(self, u, v, weight):
        self.edges.append([u, v, weight])

    def bellman_ford(self, src):
        # Initialize the distance to all vertices as infinity and distance to the source as 0
        dist = [float('inf')] * self.V
        dist[src] = 0

        # Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        # Check for negative-weight cycles by checking one more time
        for u, v, weight in self.edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                print("Graph contains negative weight cycle")
                return None

        # Return the computed shortest distances
        return dist

# Example usage:
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    distances = g.bellman_ford(0)

    if distances:
        print("Vertex Distance from Source")
        for i in range(len(distances)):
            print(f"{i}\t\t{distances[i]}")
```

### Detailed Documentation

#### Class: `Graph`

- **Attributes:**
  - `V`: The number of vertices in the graph.
  - `edges`: A list to store all edges in the form `[u, v, weight]`.

- **Methods:**
  - `__init__(self, vertices)`: Initializes the graph with a given number of vertices and an empty edge list.
  - `add_edge(self, u, v, weight)`: Adds an edge from vertex `u` to vertex `v` with the given `weight`.
  - `bellman_ford(self, src)`: Implements the Bellman-Ford algorithm to find the shortest path from the source vertex `src` to all other vertices.

#### Method: `bellman_ford(self, src)`

- **Parameters:**
  - `src`: The source vertex from which to calculate the shortest paths.

- **Process:**
  1. **Initialization**: Set the initial distance to all vertices as infinity (`float('inf')`), except for the source vertex which is set to 0.
  2. **Edge Relaxation**: Relax all edges `V - 1` times. For each edge `(u, v, weight)`, update the distance to vertex `v` if the distance to vertex `u` plus the weight of the edge is less than the current distance to `v`.
  3. **Negative-Weight Cycle Check**: Check all edges one more time to detect negative-weight cycles. If a shorter path is found, it indicates a negative-weight cycle.

- **Return Value:**
  - Returns a list of shortest distances from the source vertex to each vertex.
  - If a negative-weight cycle is detected, returns `None`.

### Time Complexity

The time complexity of the Bellman-Ford algorithm is \(O(V x E)\), where \(V\) is the number of vertices and \(E\) is the number of edges. This is because:
- Initializing the distance array takes \(O(V)\).
- Relaxing all edges \(V - 1\) times takes \(O(V x E)\).
- The final check for negative-weight cycles takes \(O(E)\).

Overall, this sums up to \(O(V x E)\).

### Space Complexity

The space complexity of the Bellman-Ford algorithm is \(O(V + E)\). This is because:
- The distance array requires \(O(V)\) space.
- The edge list requires \(O(E)\) space.

Thus, the total space complexity is \(O(V + E)\).

A **negative weight cycle** in a weighted directed graph is a cycle (a path that starts and ends at the same vertex) where the sum of the weights of the edges in the cycle is negative. This implies that you can repeatedly traverse this cycle and continuously decrease the total path cost, which makes finding shortest paths problematic because the cost can be made arbitrarily small (i.e., infinitely negative).

### Example of a Negative Weight Cycle

Consider the following directed graph with 4 nodes and the given edges:

```
nodes = 4
edges = [
    (0, 1, 1),
    (1, 2, 1),
    (2, 3, 1),
    (3, 1, -4)
]
```

Graphically, the graph looks like this:

```
    1       1       1
0 ----> 1 ----> 2 ----> 3
        ^               |
        |_______________|
               -4
```

In this graph, the cycle 1 -> 2 -> 3 -> 1 has weights 1 + 1 + (-4) = -2. Since the total weight of the cycle is negative, this graph contains a negative weight cycle.

### Why Negative Weight Cycles are Problematic

Negative weight cycles are problematic in the context of shortest path algorithms because they make it impossible to define a finite shortest path. Here’s why:

- In a graph with a negative weight cycle, you can keep traversing the cycle to reduce the path cost indefinitely.
- For instance, consider a path from a source node to some node `u` where a negative weight cycle exists. If we find a path from the source to `u` with cost `C`, by traversing the negative weight cycle once, the cost can be reduced further to `C - k` (where `k` is the absolute value of the sum of weights in the cycle).
- Thus, the concept of the shortest path becomes meaningless because the path cost can be reduced infinitely.

### Detecting Negative Weight Cycles

To detect a negative weight cycle, we use the Bellman-Ford algorithm, which works as follows:

1. **Initialization**:
   - Initialize the distance to the source node to 0 and all other distances to infinity.

2. **Relaxation**:
   - Relax all edges repeatedly (specifically `n-1` times, where `n` is the number of nodes).

3. **Check for Cycles**:
   - After `n-1` relaxations, perform one more relaxation. If any edge can still be relaxed, it means a negative weight cycle exists in the graph.

### Conclusion

A negative weight cycle is a loop in a graph where the sum of the edge weights is negative. Detecting such cycles is crucial for shortest path algorithms to function correctly, and the Bellman-Ford algorithm is an efficient way to do this. If a negative weight cycle exists, shortest path calculations become invalid as the cost can be infinitely reduced by repeatedly traversing the cycle.

### Time Efficient Approch

```python
class Solution:
    def isNegativeWeightCycle(self, n, edges):
        inf = 1000000000000000000 # initializing the value of infinity
        d = [0 for i in range(n)] # creating an array to store the minimum distances
        p = [-1 for i in range(n)] # creating an array to store the parent nodes
        for i in range(n): # iterating over all the nodes
            x = -1 # initializing x to -1
            for e in edges: # iterating over all the edges
                if(d[e[0]] + e[2] < d[e[1]]): # if the distance to the destination node is less than the current minimum distance
                    d[e[1]] = d[e[0]] + e[2] # update the minimum distance
                    p[e[1]] = e[0] # update the parent node
                    x = e[1] # update x to the destination node
        if(x == -1): # if x is still -1, there is no negative weight cycle
            return 0
        return 1 # else, there is a negative weight cycle
```

### Complexity

**Time Complexity:** O(n * m), where n is the number of nodes, and m is the number of edges. This is because the algorithm performs n-1 iterations over all edges.

**Space Complexity:** O(n) due to the arrays used to store distances and parent nodes.

