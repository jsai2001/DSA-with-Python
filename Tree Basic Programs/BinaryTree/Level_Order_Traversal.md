### Level Order Traversal Of Binary Tree

To solve the problem of finding the level order traversal of a binary tree, we can use the Breadth-First Search (BFS) algorithm. BFS is ideal for this task because it explores nodes level by level.

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(n)\)

Here's a detailed explanation, along with the implementation and analysis of time and space complexity.

### Detailed Explanation

#### Level Order Traversal (Breadth-First Search)
1. **Definition**: Level order traversal of a tree visits nodes level by level from top to bottom and left to right.
2. **Approach**:
   - Use a queue to keep track of nodes at the current level.
   - Start by adding the root node to the queue.
   - Process nodes in the queue iteratively:
     - Remove a node from the front of the queue.
     - Add its value to the result list.
     - Add its left and right children (if any) to the queue.
3. **Termination**: The process continues until the queue is empty, indicating that all nodes have been visited.

#### Steps
1. Initialize an empty queue.
2. Enqueue the root node (if it exists).
3. While the queue is not empty:
   - Dequeue the front node.
   - Record its value.
   - Enqueue its left child (if it exists).
   - Enqueue its right child (if it exists).
4. Return the list of recorded values.

### Implementation in Python

```python
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_traversal(root):
    """
    Perform level order traversal of a binary tree.
    
    Parameters:
    root (TreeNode): The root node of the binary tree.
    
    Returns:
    List[int]: The values of the nodes in level order.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Example Usage:
# Constructing a binary tree
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
#
# Expected Level Order Traversal: [1, 2, 3, 4, 5, 6]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(level_order_traversal(root))  # Output: [1, 2, 3, 4, 5, 6]
```

### Time and Space Complexity

#### Time Complexity
- Each node is enqueued and dequeued exactly once.
- Therefore, the time complexity is \(O(n)\), where \(n\) is the number of nodes in the tree.

#### Space Complexity
- The space complexity is determined by the size of the queue.
- In the worst case, the queue contains the maximum number of nodes at any level of the tree.
- For a complete binary tree, the maximum number of nodes at the lowest level is \( \lceil n/2 \rceil \).
- Thus, the space complexity is \(O(n)\) in the worst case.

### Summary
The BFS approach using a queue is efficient for performing level order traversal of a binary tree, with both time and space complexity being linear relative to the number of nodes in the tree. This makes it suitable for large trees as well.