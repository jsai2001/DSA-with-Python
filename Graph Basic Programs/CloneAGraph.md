## Clone a Graph

Cloning a graph involves creating a deep copy of the graph such that the new graph is an exact replica of the original graph, with new nodes and edges but maintaining the same structure.

-  **Time Complexity:** \(O(V + E)\)

- **Space Complexity:** \(O(V + E)\)

### Problem Statement

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

### Approach

We can solve this problem using Depth-First Search (DFS) or Breadth-First Search (BFS). Here, we will use BFS for the solution.

### Detailed Steps

1. **Create a dictionary to store the cloned nodes**. This helps in keeping track of the nodes that have been copied.
2. **Use a queue to perform BFS**. This ensures all nodes are visited level-by-level.
3. **For each node, clone it and its neighbors**.

### Python Implementation

```python
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return node
    
    # A dictionary to save the cloned nodes
    cloned_nodes = {}
    
    # Create the queue for BFS
    queue = deque([node])
    
    # Clone the root node
    cloned_nodes[node] = Node(node.val)
    
    # Start BFS traversal
    while queue:
        current = queue.popleft()
        
        # Iterate through the neighbors of the node
        for neighbor in current.neighbors:
            if neighbor not in cloned_nodes:
                # Clone the neighbor and put it in the dictionary
                cloned_nodes[neighbor] = Node(neighbor.val)
                # Add the original neighbor to the queue for further exploration
                queue.append(neighbor)
            
            # Add the cloned neighbor to the current cloned node's neighbors list
            cloned_nodes[current].neighbors.append(cloned_nodes[neighbor])
    
    # Return the cloned node corresponding to the input node
    return cloned_nodes[node]
```

### Time Complexity Analysis

The time complexity is \(O(V + E)\), where \(V\) is the number of vertices (nodes) and \(E\) is the number of edges in the graph. This is because:
- Each node is processed exactly once.
- Each edge is processed exactly once when it is first encountered in the BFS.

### Space Complexity Analysis

The space complexity is also \(O(V + E)\) because:
- The `cloned_nodes` dictionary stores each of the \(V\) nodes.
- The BFS queue can store up to \(V\) nodes in the worst case.
- Each node's neighbors list will cumulatively store \(E\) references to nodes.

### Detailed Documentation

```python
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        """
        Initialize a node in the graph.
        :param val: The integer value of the node.
        :param neighbors: A list of neighboring nodes.
        """
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    """
    Clone an undirected graph given a reference node.
    :param node: The reference node of the graph to be cloned.
    :return: The cloned graph's reference node.
    """
    if not node:
        return node

    # Dictionary to keep track of cloned nodes
    cloned_nodes = {}

    # Queue for BFS traversal
    queue = deque([node])

    # Clone the root node and put it in the dictionary
    cloned_nodes[node] = Node(node.val)

    # BFS traversal to clone all nodes and their neighbors
    while queue:
        current = queue.popleft()

        # Iterate through each neighbor of the current node
        for neighbor in current.neighbors:
            if neighbor not in cloned_nodes:
                # If the neighbor hasn't been cloned yet, clone it and add to the dictionary
                cloned_nodes[neighbor] = Node(neighbor.val)
                # Add the original neighbor to the queue for further exploration
                queue.append(neighbor)
            
            # Append the cloned neighbor to the current cloned node's neighbors list
            cloned_nodes[current].neighbors.append(cloned_nodes[neighbor])

    # Return the cloned graph starting from the clone of the original input node
    return cloned_nodes[node]
```

This code provides a clear and efficient way to clone a graph using BFS, with comprehensive time and space complexity analysis and documentation.