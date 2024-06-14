### Floyd-Warshall algorithm

The Floyd-Warshall algorithm is a classic algorithm used to find the shortest paths between all pairs of vertices in a weighted graph. It can handle both positive and negative edge weights but requires that the graph does not contain any negative weight cycles.

- **Time Complexity**: \(O(n^3)\)

- **Space Complexity**: \(O(1)\) 

### Detailed Explanation:

#### Algorithm Steps:

1. **Initialization:**
   - Create a distance matrix `dist` where `dist[i][j]` represents the shortest distance from vertex `i` to vertex `j`.
   - If there is an edge from `i` to `j`, initialize `dist[i][j]` to the weight of that edge.
   - If `i` is equal to `j`, initialize `dist[i][j]` to 0.
   - If there is no edge from `i` to `j`, initialize `dist[i][j]` to infinity.

2. **Updating Distances:**
   - Use three nested loops:
     - The outer loop picks intermediate vertices.
     - The middle and inner loops pick source and destination vertices.
   - For each pair of vertices `(i, j)`, update `dist[i][j]` as follows:
     ```python
     dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
     ```
   - This step checks if a path through vertex `k` is shorter than the direct path from `i` to `j`.

#### Pseudocode:
```python
def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
```

### Time and Space Complexity:

#### Time Complexity:
- The algorithm uses three nested loops, each running `V` times (where `V` is the number of vertices).
- Therefore, the time complexity is \(O(V^3)\).

#### Space Complexity:
- The algorithm uses a distance matrix of size \(V \times V\).
- Therefore, the space complexity is \(O(V^2)\).

### Implementation in Python:

```python
def floyd_warshall(graph):
    """
    Implements the Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices.
    
    Parameters:
    graph (list of list of int): The adjacency matrix representing the graph.
                                  If graph[i][j] is 0, it means there is no edge from vertex i to vertex j.
                                  If graph[i][j] is a positive number, it represents the weight of the edge from vertex i to vertex j.
    
    Returns:
    list of list of int: A matrix representing the shortest paths between all pairs of vertices.
                         dist[i][j] will be the shortest distance from vertex i to vertex j.
    """
    num_vertices = len(graph)
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    
    # Initialize the distance matrix with the given graph
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    # Update the distance matrix with the shortest paths
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

### Example Usage:
```python
graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]

shortest_paths = floyd_warshall(graph)
for row in shortest_paths:
    print(row)
```

In this example, the `graph` is represented as an adjacency matrix where `float('inf')` indicates no direct edge between the vertices. The function `floyd_warshall` computes the shortest paths between all pairs of vertices and returns the result in a distance matrix.

### Space Efficient Method (Using In-Place technique)

The problem you are referring to can be solved using the Floyd-Warshall algorithm. The Floyd-Warshall algorithm is a classic algorithm used to find the shortest paths between all pairs of vertices in a weighted graph with positive or negative edge weights (but without negative cycles). The algorithm works in \(O(n^3)\) time complexity and \(O(1)\) space complexity if we modify the adjacency matrix in place.

### Floyd-Warshall Algorithm Explanation

#### Input:
An \(n \times n\) adjacency matrix, where `matrix[i][j]` denotes the weight of the edge from vertex `i` to vertex `j`. If `matrix[i][j] = -1`, it means there is no edge from `i` to `j`.

#### Output:
An \(n \times n\) matrix where `matrix[i][j]` contains the shortest distance from vertex `i` to vertex `j`.

### Algorithm Steps:

1. **Initialization**: 
   - Convert all `-1` values in the matrix to a large number (representing infinity), except for the diagonal elements where `i == j`, which should be set to 0 (as the shortest path from a vertex to itself is always 0).

2. **Dynamic Programming Update**:
   - For each intermediate vertex `k`, update the distance between every pair of vertices `(i, j)` using the formula:
     \[
     \text{matrix}[i][j] = \min(\text{matrix}[i][j], \text{matrix}[i][k] + \text{matrix}[k][j])
     \]
   - This step considers whether a path through vertex `k` is shorter than the direct path from `i` to `j`.

3. **Post-Processing**:
   - Convert the large number back to `-1` for pairs `(i, j)` where no path exists (if the value is still infinity).

### Time and Space Complexity

- **Time Complexity**: \(O(n^3)\), where \(n\) is the number of vertices. This is because we have three nested loops iterating over all pairs of vertices and an intermediate vertex.
- **Space Complexity**: \(O(1)\), as we are modifying the input matrix in place and using no additional space.

### Implementation

Here's the detailed implementation of the Floyd-Warshall algorithm:

```python
def floyd_warshall(matrix):
    n = len(matrix)
    INF = float('inf')

    # Step 1: Initialize the matrix
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == -1:
                matrix[i][j] = INF
    
    # Step 2: Update the matrix with the shortest path information
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] < INF and matrix[k][j] < INF:
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    
    # Step 3: Post-process the matrix
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == INF:
                matrix[i][j] = -1

    return matrix

# Example usage:
matrix = [
    [0, 3, -1, 7],
    [-1, 0, 2, -1],
    [-1, -1, 0, 1],
    [2, -1, -1, 0]
]

shortest_paths = floyd_warshall(matrix)
for row in shortest_paths:
    print(row)
```

### Explanation of the Code

1. **Initialization**:
   - We convert all `-1` values to `INF` (infinity) except for the diagonal elements which remain `0`.

2. **Dynamic Programming Update**:
   - We iterate over each vertex `k` as an intermediate vertex and update the distance between every pair of vertices `(i, j)`.

3. **Post-Processing**:
   - After processing all vertices, we convert all `INF` values back to `-1` to indicate no path exists between those vertices.

By following this algorithm, you can compute the shortest paths between all pairs of vertices in the given edge-weighted directed graph in place, adhering to the specified time and space complexity constraints.