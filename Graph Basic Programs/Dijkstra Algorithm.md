### Dijkstra's Algorithm for Finding Shortest Paths from a Source to All Vertices

Dijkstra's algorithm is a well-known method for finding the shortest paths from a single source vertex to all other vertices in a weighted graph with non-negative edge weights. This algorithm is widely used in network routing protocols and geographic mapping applications.

- **Time Complexity:** \( O(V \log V) \)
- **Space Complexity:** \( O(V + E) \)

### Algorithm Explanation

#### Steps of the Algorithm

1. **Initialization**:
   - Create a set of all vertices in the graph (`Q`).
   - Initialize the distance to the source vertex (`dist[source]`) to `0` and to all other vertices (`dist[v]`) to infinity (`∞`).
   - Optionally, maintain a priority queue to select the vertex with the smallest distance efficiently.

2. **Main Loop**:
   - While the set `Q` is not empty:
     - Select the vertex `u` in `Q` with the smallest distance (`dist[u]`).
     - Remove `u` from `Q`.
     - For each neighbor `v` of `u` still in `Q`:
       - Calculate the tentative distance through `u` (`alt = dist[u] + weight(u, v)`).
       - If `alt` is less than `dist[v]`:
         - Update `dist[v]` to `alt`.
         - Optionally, update the priority queue to reflect the new distance.

3. **Termination**:
   - When `Q` is empty, the algorithm terminates, and `dist` contains the shortest distances from the source to all vertices.

#### Pseudocode

```python
function Dijkstra(Graph, source):
    dist[source] ← 0                      # Initial distance to source is 0
    for each vertex v in Graph:
        if v ≠ source:
            dist[v] ← ∞                  # Initial distances to all other vertices
        add v to Q                        # All nodes initially in Q

    while Q is not empty:
        u ← vertex in Q with min dist[u]  # Node with the smallest distance
        remove u from Q

        for each neighbor v of u:
            alt ← dist[u] + length(u, v)
            if alt < dist[v]:             # Relax (u, v)
                dist[v] ← alt

    return dist
```

### Time Complexity

- **Using a simple array or list**:
  - Extracting the minimum distance vertex: \( O(V) \)
  - Total time for all vertices: \( O(V^2) \)
  - Updating distances: \( O(E) \)
  - Overall time complexity: \( O(V^2 + E) \)
  - For dense graphs, where \( E \approx V^2 \), the complexity is \( O(V^2) \).

- **Using a binary heap (priority queue)**:
  - Extracting the minimum distance vertex: \( O(\log V) \)
  - Total time for all vertices: \( O(V \log V) \)
  - Updating distances: \( O(E \log V) \)
  - Overall time complexity: \( O((V + E) \log V) \)
  - For sparse graphs, where \( E \approx V \), the complexity is \( O(V \log V) \).

### Space Complexity

- The space complexity is \( O(V + E) \), as we need to store the graph's adjacency list and the distance table.

### Example Implementation in Python

Here’s a Python implementation using a priority queue (min-heap):

```python
import heapq

def dijkstra(graph, source):
    # Initialize distances and priority queue
    dist = {v: float('inf') for v in graph}
    dist[source] = 0
    pq = [(0, source)]  # Priority queue of (distance, vertex)
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # If the popped vertex has a greater distance than the recorded one, skip it
        if current_dist > dist[u]:
            continue
        
        # Iterate through the neighbors of u
        for neighbor, weight in graph[u].items():
            distance = current_dist + weight
            
            # Only consider this new path if it's better
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dist

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

source = 'A'
distances = dijkstra(graph, source)
print(distances)
```

### Explanation

1. **Graph Representation**: The graph is represented as an adjacency list using a dictionary of dictionaries.
2. **Priority Queue**: A min-heap (priority queue) is used to efficiently get the vertex with the smallest distance.
3. **Distance Updates**: The algorithm updates distances and ensures that the priority queue is updated accordingly.

By following this approach, you can efficiently find the shortest paths from a source vertex to all other vertices in a graph using Dijkstra's algorithm.