### Check if given graph is tree or not

To determine whether a given graph is a tree, we need to check two main properties:

1. **The graph is connected**: There is a path between any two vertices in the graph.
2. **The graph has no cycles**: The graph must not contain any cycles.

Additionally, for a graph with \(V\) vertices and \(E\) edges:
- It must have \(E = V - 1\) edges. This is a necessary condition for a connected acyclic graph (tree).

- **Time Complexity:** \(O(V + E)\) ~ \(O(V)\)

- **Space Complexity:** \(O(V + E)\) ~ \(O(V)\)

Let's break down the steps to check if the graph is a tree:

### Steps:

1. **Verify the edge count**: Ensure that the number of edges \(E\) is exactly \(V - 1\). If not, it cannot be a tree.
2. **Check for cycles and connectivity**:
   - Use Depth First Search (DFS) or Breadth First Search (BFS) to ensure there are no cycles.
   - Also ensure that all vertices are reachable from the starting vertex (i.e., the graph is connected).

### Algorithm:
We will use a DFS approach to check for cycles and connectivity.

### Pseudocode:
```python
def is_tree(graph):
    V = len(graph)
    
    # Step 1: Check if the number of edges is V-1
    edge_count = sum(len(neighbors) for neighbors in graph.values()) // 2
    if edge_count != V - 1:
        return False
    
    # Step 2: Check for cycles and connectivity using DFS
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if not dfs(neighbor, node):
                    return False
            elif neighbor != parent:
                return False
        return True
    
    # Start DFS from the first node (assuming nodes are labeled from 0 to V-1)
    start_node = list(graph.keys())[0]
    if not dfs(start_node, -1):
        return False
    
    # Check if all vertices are visited (graph is connected)
    return len(visited) == V
```

### Complexity Analysis:
- **Time Complexity**:
  - Checking the number of edges: \(O(V)\)
  - DFS traversal: \(O(V + E)\)
  - Since \(E = V - 1\) in a tree, the time complexity is \(O(V + (V - 1)) = O(V)\).

- **Space Complexity**:
  - Space required to store the graph: \(O(V + E)\)
  - Space required for the DFS recursion stack: \(O(V)\) in the worst case.

### Example Usage:
```python
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

print(is_tree(graph))  # Output: True, since this graph is a tree
```

### Explanation:
- We first check the number of edges.
- We then use DFS to detect any cycles and ensure all nodes are connected.
- If both checks pass, the graph is a tree.

### Edge Cases:
- An empty graph (no vertices) or a single vertex graph is trivially a tree.
- Disconnected graphs or graphs with cycles will fail the checks and return `False`.

This approach ensures that we accurately determine if a given graph is a tree with clear checks and efficient complexity.