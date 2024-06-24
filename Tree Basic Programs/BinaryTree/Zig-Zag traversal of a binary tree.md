### Zig-Zag (or Spiral) traversal of a binary tree

In a Zig-Zag traversal, the nodes are visited in a level order but the direction of traversal alternates between left to right and right to left for each level.

- **Time Complexity:** \(O(N)\)

- **Space Complexity:** \(O(N)\)

## Approach

To achieve a Zig-Zag traversal, we can use a double-ended queue (deque) which allows for efficient insertion and deletion from both ends. We will use a Breadth-First Search (BFS) strategy to traverse the tree level by level. For each level, we will keep track of the direction of traversal and append the nodes to the result accordingly.

### Steps

1. **Initialize**:
    - A deque to keep track of the nodes at the current level.
    - A flag (`left_to_right`) to indicate the direction of traversal. Initially set to `True` (left to right).
    - A list (`result`) to store the final Zig-Zag order.

2. **Traversal**:
    - While the deque is not empty, do the following:
        - Determine the number of nodes at the current level (`level_size`).
        - Create a temporary list (`level_nodes`) to store the nodes of the current level.
        - Iterate over the nodes of the current level:
            - Pop a node from the deque.
            - Depending on the direction, append the node's value to `level_nodes`.
            - Add the node's children to the deque for the next level.
        - After processing all nodes of the current level, append `level_nodes` to `result`.
        - Toggle the direction (`left_to_right`).

3. **Output**:
    - The `result` list will contain the nodes in Zig-Zag order.

### Time Complexity

- Each node is processed exactly once, so the time complexity is \(O(N)\), where \(N\) is the number of nodes in the tree.

### Space Complexity

- The space complexity is \(O(N)\) due to the deque and the result list, which at most will hold all nodes in the tree.

Here's the implementation in Python:

```python
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def zigzag_traversal(root):
    if not root:
        return []
    
    result = []
    current_level = deque([root])
    left_to_right = True
    
    while current_level:
        level_size = len(current_level)
        level_nodes = []
        
        for _ in range(level_size):
            if left_to_right:
                node = current_level.popleft()
                level_nodes.append(node.value)
                if node.left:
                    current_level.append(node.left)
                if node.right:
                    current_level.append(node.right)
            else:
                node = current_level.pop()
                level_nodes.append(node.value)
                if node.right:
                    current_level.appendleft(node.right)
                if node.left:
                    current_level.appendleft(node.left)
        
        result.append(level_nodes)
        left_to_right = not left_to_right
    
    return result

# Example usage
# Constructing a binary tree as an example:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(zigzag_traversal(root))
# Output: [[1], [3, 2], [4, 5, 6, 7]]
```

### Explanation of Example Usage

In the provided binary tree example:
- The first level is traversed left to right: [1]
- The second level is traversed right to left: [3, 2]
- The third level is traversed left to right: [4, 5, 6, 7]

Thus, the final Zig-Zag order is `[[1], [3, 2], [4, 5, 6, 7]]`.