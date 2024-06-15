Detecting a negative cycle in a graph is a common problem in graph theory, and it can be solved using various algorithms. One of the most well-known algorithms for this purpose is the Bellman-Ford algorithm. Here, I will explain the Bellman-Ford algorithm and how it can be used to detect negative cycles, along with its time and space complexity.

- **Time Complexity:** \(O(V x E)\)

- **Space Complexity:** \(O(V)\)

### Bellman-Ford Algorithm

The Bellman-Ford algorithm computes shortest paths from a single source vertex to all other vertices in a weighted graph. It is particularly useful for graphs with negative weight edges, where Dijkstra's algorithm would fail.

#### Steps to Detect a Negative Cycle

1. **Initialize Distances:**
   - Create a distance array `dist[]` of size `V` (number of vertices) and initialize all distances to infinity (`INF`), except for the source vertex which is set to 0.
   
2. **Relax Edges Repeatedly:**
   - For each vertex, apply the relaxation process for all edges `V-1` times, where `V` is the number of vertices. Relaxation means updating the distance to the neighboring vertex if a shorter path is found.

3. **Check for Negative Weight Cycles:**
   - Perform one more iteration over all edges. If you can further relax any edge, then a negative weight cycle exists in the graph.

#### Detailed Steps and Code Implementation

```python
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def detect_negative_cycle(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 1: Relax all edges |V| - 1 times.
        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 2: Check for negative-weight cycles.
        for u, v, w in self.edges:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                return True  # Negative cycle detected

        return False  # No negative cycle

# Example usage:
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

if g.detect_negative_cycle(0):
    print("Graph contains negative weight cycle")
else:
    print("Graph does not contain negative weight cycle")
```

### Explanation

1. **Graph Initialization:**
   - The `Graph` class is initialized with the number of vertices `V`.
   - The `add_edge` method is used to add edges to the graph with given vertices `u` and `v` and weight `weight`.

2. **Negative Cycle Detection:**
   - The `detect_negative_cycle` method initializes distances and performs edge relaxation `V-1` times.
   - If after `V-1` relaxations, any distance can still be updated, a negative cycle is detected, and the function returns `True`.
   - If no further relaxation is possible, the function returns `False`, indicating no negative cycle exists.

### Time and Space Complexity

- **Time Complexity:** \(O(V x E)\)
  - The algorithm performs \(V-1\) iterations of relaxation over all edges, which takes \(O(E)\) time per iteration, resulting in a total time complexity of \(O(V x E)\).
- **Space Complexity:** \(O(V)\)
  - The space complexity is dominated by the distance array `dist[]`, which stores the shortest distances to each vertex, resulting in \(O(V)\) space.

### Conclusion

The Bellman-Ford algorithm efficiently detects negative cycles in a graph with a time complexity of \(O(V x E)\) and a space complexity of \(O(V)\). It is particularly useful for graphs with negative edge weights, providing a robust solution for detecting negative cycles.