### Top View of a Binary Tree

Solve the "Top View of a Binary Tree" problem with clear documentation, including details of the time and space complexity.

- **Time Complexity:** \(O(N \log N)\)

- **Space Complexity:** \(O(N)\)

### Problem Statement
Given a binary tree, you need to print the nodes that are visible when the tree is viewed from the top. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top. 

### Approach
We can solve this problem using a level order traversal (BFS) combined with a horizontal distance concept. The idea is to keep track of the horizontal distance of each node from the root node, which is considered to have a horizontal distance of 0. Nodes to the left have a horizontal distance of -1, -2, etc., and nodes to the right have a horizontal distance of 1, 2, etc.

Here's the step-by-step approach:

1. Use a queue to perform a level order traversal (BFS).
2. Use a dictionary to keep track of the first node at each horizontal distance.
3. For each node, if its horizontal distance is not in the dictionary, add it.
4. Print the values from the dictionary sorted by horizontal distance.

### Algorithm

1. **Initialization**: Create a queue to hold pairs of tree nodes and their horizontal distance. Also, create a dictionary to hold the top view nodes.
2. **BFS Traversal**: While the queue is not empty, dequeue the front node and its horizontal distance.
   - If the horizontal distance is not already in the dictionary, add the node value to the dictionary.
   - Enqueue the left child with a horizontal distance decreased by 1.
   - Enqueue the right child with a horizontal distance increased by 1.
3. **Result**: Extract the values from the dictionary sorted by the horizontal distance and print them.

### Implementation

Here's a Python implementation of the above approach:

```python
class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

from collections import deque

def top_view(root):
    if not root:
        return []
    
    # Dictionary to store the first node at each horizontal distance
    top_view_map = {}
    
    # Queue for BFS traversal
    queue = deque([(root, 0)])  # (node, horizontal_distance)
    
    while queue:
        node, hd = queue.popleft()
        
        # If horizontal distance is seeing for the first time
        if hd not in top_view_map:
            top_view_map[hd] = node.data
        
        # Enqueue left and right children with updated horizontal distances
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    
    # Extracting the top view nodes sorted by horizontal distance
    top_view_nodes = [top_view_map[hd] for hd in sorted(top_view_map.keys())]
    
    return top_view_nodes

# Example usage:
# Creating a binary tree
#       1
#      / \
#     2   3
#      \   
#       4  
#        \
#         5
#          \
#           6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)
root.left.right.right.right = TreeNode(6)

print(top_view(root))  # Output: [2, 1, 3, 6]
```

### Complexity Analysis

- **Time Complexity**: \(O(n \log n)\)
  - The BFS traversal itself takes \(O(n)\), where \(n\) is the number of nodes in the tree.
  - Sorting the keys of the dictionary takes \(O(\log n)\) in the worst case if all nodes have different horizontal distances.
- **Space Complexity**: \(O(n)\)
  - The dictionary `top_view_map` can have at most \(n\) entries.
  - The queue can have at most \(n\) nodes in the worst case, leading to an overall space complexity of \(O(n)\).

This approach ensures we efficiently capture and print the top view of the binary tree.