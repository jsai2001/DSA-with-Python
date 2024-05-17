# Time Complexity: O(|V|+|E|)
# Space Complexity: O(|V|)
"""
**Breadth-First Search (BFS) Traversal for Directed Graphs**

BFS is a graph traversal algorithm that explores all the neighboring nodes of a starting node before moving on to the next level of neighbors. 
This results in a level-by-level exploration of the graph. 
It's particularly useful for finding the shortest paths in unweighted graphs.
"""
from collections import deque

def bfs_traversal(graph, start):
    """
  Performs BFS traversal on a directed graph starting from a given node.

  Args:
      graph: A dictionary representing the graph. Keys are nodes, values are lists of neighboring nodes.
      start: The starting node for the traversal.

  Returns:
      A list containing the nodes visited in BFS order.
  """
    visited = set()  # Track visited nodes to avoid cycles
    queue = deque([start])  # Queue for BFS traversal

    traversal = []
    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            traversal.append(current_node)
            for neighbor in graph[current_node]:
                queue.append(neighbor)

    return traversal

# Example usage
graph = {
  0: [1, 2],
  1: [3, 4],
  2: [5],
  3: [],
  4: [],
  5: [],
}

traversal = bfs_traversal(graph, 0)
print("BFS traversal:", traversal)

"""
**Explanation:**

1. **`bfs_traversal` function:**
   - Takes a graph (dictionary) and a starting node as input.
   - Initializes a `visited` set to keep track of explored nodes and prevent revisiting them in case of cycles in the graph.
   - Creates a `queue` using `deque` from `collections` for efficient BFS (FIFO - First-In-First-Out) behavior. The starting node is added to the queue.
   - Initializes an empty `traversal` list to store the visited nodes in the order they are explored.

2. **BFS Loop:**
   - The loop continues as long as there are nodes in the queue (i.e., unexplored neighbors).
   - **`current_node`:** The node at the front of the queue is dequeued.
   - **Visited Check:** If the `current_node` hasn't been visited before:
     - It's marked as visited in the `visited` set.
     - The node is appended to the `traversal` list, signifying it's been explored.
     - All the neighbors of the `current_node` are retrieved from the graph dictionary and added to the queue for further exploration in the next iteration.

3. **Return:**
   - The function returns the `traversal` list containing the nodes visited in BFS order, ensuring connected nodes (directly or indirectly) from the starting node are included.

**Key Points:**

- BFS uses a queue data structure to process nodes level-by-level.
- The `visited` set is crucial to avoid infinite loops in graphs with cycles.
- This code effectively addresses the prompt's requirements for BFS traversal on directed graphs, considering node connectivity.
"""
"""
**Time Complexity:**

- In the worst case, the BFS algorithm might need to explore all reachable nodes and edges in the graph.
- The queue operation (`enqueue` and `dequeue`) takes constant time (O(1)) on average with most queue implementations like `deque`.
- The total number of queue operations depends on the number of nodes and edges explored. In the worst case, BFS visits every node and its outgoing edges once, resulting in:
   - O(|V|) for visiting all nodes (V being the number of vertices).
   - O(|E|) for processing all edges (E being the number of edges).
- Therefore, the overall time complexity of BFS traversal on a directed graph is:
   - **O(|V| + |E|)**, which is linear in the number of vertices and edges.

**Space Complexity:**

- The BFS algorithm primarily uses the queue to store the nodes waiting for exploration.
- In the worst case, all nodes reachable from the starting node could be in the queue at a single level, especially for dense graphs (many edges).
- This translates to a space complexity of:
   - **O(|V|)**, which is also linear in the number of vertices.

**Summary:**

- BFS traversal has a time complexity of O(|V| + |E|), making it efficient for exploring graphs, especially for finding shortest paths in unweighted graphs.
- The space complexity of BFS is O(|V|), reflecting the memory needed to store the queue of nodes awaiting exploration.
"""
