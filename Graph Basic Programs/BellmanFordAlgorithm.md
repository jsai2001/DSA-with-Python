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