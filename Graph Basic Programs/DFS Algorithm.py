# Time Complexity: O(|V| + |E|)
# Space Complexity: O(|V|)
"""
**Depth-First Search (DFS) Traversal**
DFS is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It visits a node, then explores all its unvisited neighbors recursively, resulting in a depth-wise exploration of the graph. This strategy comes in handy for various applications, including finding connected components, detecting cycles, and topological sorting (for directed acyclic graphs).

**Python Implementation:**
"""

def dfs_traversal(graph, start, order="preorder"):
  """
  Performs DFS traversal on a directed graph starting from a given node with a specified traversal order.

  Args:
      graph: A dictionary representing the graph. Keys are nodes, values are lists of neighboring nodes.
      start: The starting node for the traversal.
      order (str, optional): The desired DFS traversal order. Defaults to "preorder" (visit node before neighbors).
          Other options include "inorder" and "postorder".

  Returns:
      A list containing the nodes visited in DFS order based on the specified order.
  """
  visited = set()  # Track visited nodes to avoid cycles
  traversal = []

  def dfs_helper(node):
    """
    Recursive helper function for DFS traversal.

    Args:
        node: The current node being explored.
    """
    if node not in visited:
      if order == "preorder":
        traversal.append(node)  # Preorder: visit node before neighbors
      visited.add(node)
      for neighbor in graph[node]:
        dfs_helper(neighbor)
      if order == "postorder":
        traversal.append(node)  # Postorder: visit node after neighbors

  dfs_helper(start)
  return traversal

# Example usage with different traversal orders
graph = {
  0: [1, 2],
  1: [3, 4],
  2: [5],
  3: [],
  4: [],
  5: [],
}

preorder_traversal = dfs_traversal(graph.copy(), 0, order="preorder")
print("DFS traversal (preorder):", preorder_traversal)

inorder_traversal = dfs_traversal(graph.copy(), 0, order="inorder")  # Not applicable for directed graphs
print("DFS traversal (inorder):", inorder_traversal)  # Might print an incomplete traversal

postorder_traversal = dfs_traversal(graph.copy(), 0, order="postorder")
print("DFS traversal (postorder):", postorder_traversal)

"""
**Explanation:**

- The code defines a `dfs_traversal` function that takes a graph, starting node, and an optional `order` parameter (defaulting to "preorder").
- The `dfs_helper` function recursively explores the graph, marking visited nodes and appending them to the `traversal` list based on the specified order:
   - **Preorder:** The node is visited before exploring its neighbors (default).
   - **Inorder:** Not applicable for directed acyclic graphs (DAGs) as the order between nodes at different levels isn't well-defined. The provided code might print an incomplete traversal.
   - **Postorder:** The node is visited after exploring all its neighbors.

**Time and Space Complexity:**
- DFS, similar to BFS, has a time complexity of O(|V| + |E|) in the worst case, where V is the number of vertices and E is the number of edges. This is because DFS might need to visit all nodes and their edges once.
- The space complexity of DFS is also O(|V|) due to the recursive call stack, which can grow as deep as the number of vertices in the path being explored.

**In Summary:**
DFS provides a powerful tool for graph exploration, offering different traversal orders for specific use cases. This implementation allows you to choose the desired order and effectively navigate directed graphs.
"""

"""
In this directed graph:

Starting at node 0, DFS can explore either node 1 or 2 first. There's no inherent "left" or "right" child.
Depending on the exploration path, the traversal might visit nodes in an order that doesn't align with inorder's left-root-right structure.
Therefore, in directed graphs, inorder traversal might not produce a meaningful or complete result. 
It could be empty if the exploration doesn't encounter nodes in a specific left-to-right order or might only include a partial traversal if it gets stuck on a specific path.

Key Points:

Inorder traversal is well-suited for BSTs, where it provides a sorted output.
Directed graphs lack the inherent left-right structure required for meaningful inorder traversal.
DFS on directed graphs is more flexible, allowing for exploration in preorder (visit node before neighbors) or postorder (visit node after neighbors) based on the chosen traversal order.
"""
"""
Time Complexity:

In the worst case, DFS might need to explore all reachable nodes and edges in the graph.
The DFS algorithm visits a node, then explores all its unvisited neighbors recursively.
Assuming constant time (O(1)) for visiting a node and adding/removing from the recursive call stack, the total time complexity depends on the number of nodes and edges explored.
In the worst case, DFS visits every node and its outgoing edges once, resulting in:
O(|V|) for visiting all nodes (V being the number of vertices).
O(|E|) for processing all edges (E being the number of edges).
Therefore, the overall time complexity of DFS traversal on a directed graph is:
O(|V| + |E|), which is linear in the number of vertices and edges.

Space Complexity:

DFS primarily uses the recursive call stack to keep track of the exploration path.
In the worst case, all nodes reachable from the starting node could be on the call stack at a time, especially for dense graphs (many edges).
This translates to a space complexity of:
O(|V|), which is also linear in the number of vertices.
"""