### Right View of a Binary Tree

To solve the problem of finding the right view of a binary tree, we need to identify the nodes that are visible when the tree is viewed from the right side. This involves traversing the tree level by level and selecting the last node at each level.

- **Time Complexity:** \(O(N)\)

- **Space Complexity:** \(O(N)\)

Here is a detailed solution, including documentation and an analysis of the time and space complexity:

### Solution: Right View of a Binary Tree

#### Approach

We can solve this problem using a breadth-first search (BFS) approach, which will allow us to traverse the tree level by level. We use a queue to facilitate the level order traversal. For each level, we will add the last node to our right view result list.

#### Steps

1. If the tree is empty, return an empty list.
2. Initialize a queue and add the root node to it.
3. While the queue is not empty:
    - Determine the number of nodes at the current level (`level_length`).
    - Traverse all nodes at the current level.
    - Add the value of the last node at the current level to the result list.
    - Add the children of the current node to the queue for the next level traversal.
4. Return the result list containing the right view of the tree.

#### Implementation

Here's the Python implementation:

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_view(root):
    """
    Returns the right view of a binary tree.
    
    Args:
    root (TreeNode): The root of the binary tree.
    
    Returns:
    List[int]: A list of node values representing the right view of the tree.
    """
    if not root:
        return []

    right_view_list = []
    queue = deque([root])

    while queue:
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()

            # If this is the last node in the current level, add it to the right view list
            if i == level_length - 1:
                right_view_list.append(node.val)

            # Add left and right children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return right_view_list
```

#### Example Usage

```python
# Example tree:
#     1
#    / \
#   2   3
#    \   \
#     5   4

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print(right_view(root))  # Output: [1, 3, 4]
```

### Time and Space Complexity

- **Time Complexity**: O(N)
  - We visit each node exactly once. Here, \( N \) is the number of nodes in the binary tree.
  
- **Space Complexity**: O(N)
  - In the worst case, the queue will hold all nodes at the deepest level of the tree. This could be up to \( N \) nodes if the tree is a complete binary tree. Therefore, the space complexity is \( O(N) \). The result list also takes \( O(N) \) space.

This approach ensures that we efficiently and correctly obtain the right view of a binary tree using level order traversal.