### Detect Cycle in Directed Graph using BFS/DFS algorithm

Detecting a cycle in a directed graph can be efficiently performed using either Depth-First Search (DFS) or Breadth-First Search (BFS). Here, we will provide solutions using both methods, with detailed explanations, code, and analysis of time and space complexity.

* Time Complexity - O(V+E)

* Space Complexity - O(V)

### DFS Approach

**Explanation:**

In the DFS approach, we keep track of the nodes currently in the recursion stack (or call stack). If we encounter a node that is already in the recursion stack, we have detected a cycle.

**Steps:**

1. Use a boolean array `visited` to keep track of visited nodes.
2. Use another boolean array `recStack` to keep track of nodes in the current recursion stack.
3. For each node, if it hasn't been visited, start a DFS from that node.
4. During the DFS, if we reach a node that is already in the recursion stack, a cycle is detected.
5. If the DFS completes without finding a cycle, continue to the next node.

**Code:**

```python
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def isCyclicUtil(self, v, visited, recStack):
        # Mark the current node as visited and add to recursion stack
        visited[v] = True
        recStack[v] = True
        
        # Recur for all neighbours
        # If any neighbour is visited and in recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour]:
                return True
        
        # Remove the vertex from recursion stack
        recStack[v] = False
        return False
    
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        
        # Call the recursive helper function to detect cycle in different DFS trees
        for node in range(self.V):
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True
        return False

# Example usage
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Graph has a cycle" if g.isCyclic() else "Graph has no cycle")
```

**Time Complexity:** \(O(V + E)\), where \(V\) is the number of vertices and \(E\) is the number of edges. Each node and edge is visited once.

**Space Complexity:** \(O(V)\), due to the `visited` and `recStack` arrays.

### BFS (Kahn's Algorithm for Topological Sorting)

**Explanation:**

In the BFS approach using Kahn's Algorithm, we count the in-degrees of all nodes and use a queue to process nodes with zero in-degrees. If we can process all nodes, there's no cycle. If there are nodes left unprocessed, a cycle exists.

**Steps:**

1. Calculate the in-degrees of all nodes.
2. Add all nodes with zero in-degrees to a queue.
3. Process nodes from the queue, reducing the in-degree of their neighbors.
4. If a neighbor's in-degree becomes zero, add it to the queue.
5. If the number of processed nodes is less than the total number of nodes, a cycle exists.

**Code:**

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def isCyclic(self):
        in_degree = [0] * self.V
        
        # Calculate in-degrees of all nodes
        for i in range(self.V):
            for j in self.graph[i]:
                in_degree[j] += 1
        
        # Initialize queue and add all nodes with zero in-degree
        queue = deque()
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            
            # Decrease the in-degree of all neighbors
            for neighbour in self.graph[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        
        # If count of visited nodes is not equal to the number of nodes, there's a cycle
        return count != self.V

# Example usage
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Graph has a cycle" if g.isCyclic() else "Graph has no cycle")
```

**Time Complexity:** \(O(V + E)\), as we process each edge and vertex once.

**Space Complexity:** \(O(V)\), for storing in-degrees and the queue.

Both approaches efficiently detect cycles in a directed graph, with comparable time and space complexities. The choice between DFS and BFS may depend on specific use cases and preferences for recursion (DFS) versus iterative approaches (BFS).

### Example and Explanation

Let's consider the following graph with a cycle:
```
0 → 1 → 2 → 3
↑         ↓
└----4 ←--┘
```

**Step-by-Step Execution for the Corrected Graph:**

1. **Calculate in-degrees**:
   - Vertex 0: in-degree = 1 (edge from 4)
   - Vertex 1: in-degree = 1 (edge from 0)
   - Vertex 2: in-degree = 1 (edge from 1)
   - Vertex 3: in-degree = 1 (edge from 2)
   - Vertex 4: in-degree = 1 (edge from 3)

2. **Initialize queue**:
   - Queue = [] (No vertex has in-degree 0)

3. **Process nodes**:
   - The queue is empty at the start, so no nodes are processed.

4. **Check for cycles**:
   - Number of processed nodes = 0 (no nodes processed)
   - Total number of nodes = 5
   - Since no nodes were processed, a cycle exists.

### Conclusion
In this corrected example, no nodes have an in-degree of 0. Therefore, the queue remains empty, and no nodes are processed, directly indicating the presence of a cycle. This reinforces the idea that if the number of processed nodes is less than the total number of nodes, a cycle must exist.