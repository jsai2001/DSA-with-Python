### Graph Coloring Problem

#### Problem Statement
The Graph Coloring Problem involves assigning colors to the vertices of a graph such that no two adjacent vertices share the same color. The objective is to use the minimum number of colors.

- **Time Complexity:** `O(m^V)`

- **Space Complexity:** `O(V)`

#### Applications
1. **Scheduling problems**: Assigning time slots to tasks, where some tasks cannot occur simultaneously.
2. **Map coloring**: Coloring a map such that no two adjacent regions have the same color.
3. **Register allocation in compilers**: Assigning a limited number of registers to a large number of variables.

#### Approach
The most common approach to solving the Graph Coloring Problem is through backtracking. There are also heuristic and approximation algorithms for larger graphs where an exact solution is not feasible.

#### Backtracking Algorithm
The backtracking algorithm is a recursive method that tries to assign colors to the vertices one by one. If a vertex cannot be assigned a color without violating the coloring constraints, the algorithm backtracks and tries a different color for the previous vertex.

### Algorithm Implementation

```python
def is_safe(graph, vertex, color, colors):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True

def graph_coloring_util(graph, m, colors, vertex):
    if vertex == len(graph):
        return True

    for color in range(1, m + 1):
        if is_safe(graph, vertex, color, colors):
            colors[vertex] = color
            if graph_coloring_util(graph, m, colors, vertex + 1):
                return True
            colors[vertex] = 0
    return False

def graph_coloring(graph, m):
    colors = [0] * len(graph)
    if not graph_coloring_util(graph, m, colors, 0):
        return False, []
    return True, colors

# Example usage:
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 3  # Number of colors

result, coloring = graph_coloring(graph, m)
if result:
    print("Graph can be colored with the given colors:", coloring)
else:
    print("Graph cannot be colored with the given colors.")
```

### Explanation
1. **is_safe(graph, vertex, color, colors)**: Checks if it's safe to assign the color to the vertex by ensuring no adjacent vertices have the same color.
2. **graph_coloring_util(graph, m, colors, vertex)**: Recursively tries to color each vertex. If it finds a coloring that satisfies all constraints, it returns True.
3. **graph_coloring(graph, m)**: Initializes the colors array and starts the recursive coloring process.

### Time Complexity
The time complexity of the backtracking algorithm for graph coloring is O(m^V), where V is the number of vertices and m is the number of colors. This is because, in the worst case, we try m colors for each of the V vertices.

### Space Complexity
The space complexity is O(V), which is the space required for the `colors` array used to store the color assigned to each vertex. Additionally, the recursion stack may also take up to O(V) space in the worst case.

### Conclusion
The Graph Coloring Problem is NP-complete, meaning that no polynomial-time algorithm is known for solving all instances of the problem. The backtracking approach is practical for small graphs but may become infeasible for large graphs due to its exponential time complexity. For larger graphs, heuristic and approximation algorithms are often used.