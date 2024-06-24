### Check if all leaf nodes are at same level or not

To solve the problem of checking if all leaf nodes in a binary tree are at the same level, we can perform a breadth-first search (BFS) or a depth-first search (DFS) with an additional check for the level of each leaf node. Here, I'll provide a solution using DFS for clarity, although a BFS approach is also valid and quite similar in terms of complexity.

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(h)\)

### Solution Explanation

1. **Depth-First Search (DFS) Approach**:
   - Use a helper function that traverses the tree.
   - Keep track of the level of each node during traversal.
   - Store the level of the first encountered leaf node.
   - For each subsequent leaf node, check if it is at the same level as the first leaf node.
   - If any leaf node is found at a different level, return false.
   - If traversal completes without finding such a discrepancy, return true.

### Implementation

Here’s a Python implementation using DFS:

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def check_leaves_level(root):
    if not root:
        return True

    def dfs(node, level, leaf_levels):
        if not node:
            return True
        if not node.left and not node.right:  # It's a leaf node
            if leaf_levels[0] == -1:
                leaf_levels[0] = level  # Set the level of the first leaf node
            elif leaf_levels[0] != level:
                return False  # Leaf at different level
            return True
        
        # Recur for left and right subtree
        return dfs(node.left, level + 1, leaf_levels) and dfs(node.right, level + 1, leaf_levels)

    # We use a list to store the leaf level, so it can be modified inside the dfs
    leaf_levels = [-1]
    return dfs(root, 0, leaf_levels)

# Example Usage:
# Constructing a simple tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(check_leaves_level(root))  # Output should be True
```

### Complexity Analysis

- **Time Complexity**: \(O(n)\)
  - Each node is visited once, so the time complexity is linear relative to the number of nodes in the tree.
- **Space Complexity**: \(O(h)\)
  - The space complexity is determined by the depth of the recursion stack, which is proportional to the height \(h\) of the tree. In the worst case, for a skewed tree, the height could be \(n\), leading to \(O(n)\) space complexity. For a balanced tree, the height would be \(O(\log n)\).

This solution efficiently checks if all leaf nodes are at the same level using a depth-first traversal approach with a clear and concise method to track the level of leaf nodes.