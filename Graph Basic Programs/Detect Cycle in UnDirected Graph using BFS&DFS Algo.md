## Detect Cycle in UnDirected Graph using BFS/DFS Algo

- **Time Complexity:** \(O(V + E)\)

- **Space Complexity:** \(O(V)\)

Detecting a cycle in an undirected graph can be achieved using both Breadth-First Search (BFS) and Depth-First Search (DFS). Below, I'll provide detailed explanations for both methods, including the algorithm steps, Python implementations, and their time and space complexities.

## Cycle Detection in Undirected Graph using BFS

### Algorithm (BFS)
1. Initialize a queue to hold pairs of `(node, parent)`.
2. Maintain a visited array to keep track of visited nodes.
3. For each unvisited node in the graph, perform the following steps:
   1. Mark the node as visited and push `(node, -1)` into the queue (since the starting node has no parent).
   2. While the queue is not empty:
      1. Dequeue a pair `(current_node, parent_node)`.
      2. For each adjacent node of `current_node`:
         1. If the adjacent node is not visited, mark it as visited and push `(adjacent_node, current_node)` into the queue.
         2. If the adjacent node is visited and is not the parent of `current_node`, a cycle is detected.
4. If no cycle is detected after checking all nodes, return `False`.

### Python Implementation (BFS)
```python
from collections import deque

def detect_cycle_bfs(graph, num_nodes):
    visited = [False] * num_nodes

    def bfs(start):
        queue = deque([(start, -1)])  # (node, parent)
        visited[start] = True

        while queue:
            node, parent = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True
        return False

    for node in range(num_nodes):
        if not visited[node]:
            if bfs(node):
                return True
    return False

# Example usage:
graph = [
    [1, 2],
    [0, 2],
    [0, 1, 3],
    [2]
]
num_nodes = len(graph)
print(detect_cycle_bfs(graph, num_nodes))  # Output: True
```

### Time and Space Complexity (BFS)
- **Time Complexity:** \(O(V + E)\), where \(V\) is the number of vertices and \(E\) is the number of edges. This is because each vertex and edge is processed once.
- **Space Complexity:** \(O(V)\) for the visited array and the queue, which can grow to the size of all nodes in the worst case.

## Cycle Detection in Undirected Graph using DFS

### Algorithm (DFS)
1. Maintain a visited array to keep track of visited nodes.
2. For each unvisited node in the graph, perform the following steps:
   1. Call a recursive DFS function with the current node and its parent.
   2. In the DFS function:
      1. Mark the current node as visited.
      2. For each adjacent node:
         1. If the adjacent node is not visited, recursively call the DFS function with the adjacent node and the current node as its parent.
         2. If the adjacent node is visited and is not the parent of the current node, a cycle is detected.
3. If no cycle is detected after checking all nodes, return `False`.

### Python Implementation (DFS)
```python
def detect_cycle_dfs(graph, num_nodes):
    visited = [False] * num_nodes

    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in range(num_nodes):
        if not visited[node]:
            if dfs(node, -1):
                return True
    return False

# Example usage:
graph = [
    [1, 2],
    [0, 2],
    [0, 1, 3],
    [2]
]
num_nodes = len(graph)
print(detect_cycle_dfs(graph, num_nodes))  # Output: True
```

### Time and Space Complexity (DFS)
- **Time Complexity:** \(O(V + E)\), where \(V\) is the number of vertices and \(E\) is the number of edges. This is because each vertex and edge is processed once.
- **Space Complexity:** \(O(V)\) for the visited array and the call stack in the worst case of recursion depth, which can be equal to the number of nodes.

Both BFS and DFS are effective for detecting cycles in an undirected graph. The choice between BFS and DFS may depend on specific use cases or personal preference, as both have similar time and space complexities.