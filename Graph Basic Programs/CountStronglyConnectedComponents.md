### Kosaraju Algorithm

To find the number of strongly connected components (SCCs) in a directed graph, we can use Kosaraju's algorithm. This algorithm operates in two main phases and efficiently finds all SCCs in O(V + E) time complexity, where V is the number of vertices and E is the number of edges. Below, I will provide a detailed explanation, step-by-step process, and code implementation in Python.

- **Time Complexity:** \(O(V + E)\)

- **Space Complexity:** \(O(V + E)\)

### Detailed Explanation

#### Definitions:
1. **Directed Graph**: A graph where edges have directions.
2. **Strongly Connected Component (SCC)**: A subgraph where every vertex is reachable from every other vertex in that subgraph.

#### Steps to find SCCs using Kosaraju's Algorithm:
1. **First Pass (Order Vertices by Finish Time)**:
    - Perform a Depth-First Search (DFS) on the original graph to compute the finishing times of vertices. This means we need to keep track of the order in which vertices finish processing.

2. **Transpose the Graph**:
    - Reverse the direction of all edges in the graph to get the transpose of the graph.

3. **Second Pass (Find SCCs)**:
    - Perform a DFS on the transposed graph, but in the order of decreasing finish times obtained from the first pass.
    - Each DFS tree in this pass represents a strongly connected component.

### Kosaraju's Algorithm

Here is a step-by-step Python implementation:

```python
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def _dfs(self, v, visited, stack=None):
        visited[v] = True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                self._dfs(neighbour, visited, stack)
        if stack is not None:
            stack.append(v)
    
    def _transpose(self):
        transposed_graph = Graph(self.V)
        for v in self.graph:
            for neighbour in self.graph[v]:
                transposed_graph.add_edge(neighbour, v)
        return transposed_graph
    
    def find_sccs(self):
        stack = []
        visited = [False] * self.V
        
        # First pass to order vertices by finish time
        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, stack)
        
        # Get the transposed graph
        transposed_graph = self._transpose()
        
        # Second pass to find SCCs
        visited = [False] * self.V
        scc_count = 0
        
        while stack:
            v = stack.pop()
            if not visited[v]:
                transposed_graph._dfs(v, visited)
                scc_count += 1
        
        return scc_count

# Example usage:
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    
    print("Number of strongly connected components:", g.find_sccs())
```

### Explanation of Code:
1. **Graph Class**: Represents a directed graph using an adjacency list.
2. **add_edge(u, v)**: Adds a directed edge from vertex u to vertex v.
3. **_dfs(v, visited, stack)**: A utility method to perform DFS and optionally fill the stack with vertices based on their finishing times.
4. **_transpose()**: Generates the transpose of the graph.
5. **find_sccs()**: Uses Kosaraju's algorithm to find and return the number of SCCs.

### Time Complexity:
- The algorithm performs two DFS traversals, each taking O(V + E) time.
- Transposing the graph also takes O(V + E) time.
- Thus, the overall time complexity is O(V + E).

### Space Complexity:
- The space complexity is O(V + E) due to the adjacency list representation of the graph and the storage of the visited list and stack.
- Additional space for the transposed graph is also O(V + E).

In summary, Kosaraju's algorithm efficiently finds the number of strongly connected components in a directed graph with a time complexity of O(V + E) and space complexity of O(V + E).