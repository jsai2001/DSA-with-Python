### Bottom View of a binary tree

The "Bottom View" of a binary tree is a set of nodes visible when the tree is viewed from the bottom. Let's walk through the process of solving this problem, including the necessary algorithm, implementation, and analysis of time and space complexity.

- **Time Complexity:** \(O(N)\)

- **Space Complexity:** \(O(N)\)

### Problem Explanation

Given a binary tree, you need to return the bottom view of the binary tree. The bottom view includes the last node visible from bottom at each horizontal distance from the root.

### Algorithm

1. **Horizontal Distance (HD):**
   - Assign a horizontal distance to each node. The horizontal distance of the root is 0.
   - For the left child of a node, the horizontal distance is parent’s horizontal distance minus 1.
   - For the right child, it’s parent’s horizontal distance plus 1.

2. **Level Order Traversal:**
   - Perform a level order traversal using a queue, keeping track of nodes along with their horizontal distances.
   - Use a dictionary to keep track of the latest node at each horizontal distance.

### Detailed Steps

1. Create an empty dictionary to store the bottom view. The key will be the horizontal distance, and the value will be the node's value.
2. Use a queue for level order traversal. Each element in the queue will be a tuple containing a node and its horizontal distance.
3. Traverse the tree:
   - For each node, update the dictionary with the node’s value for its horizontal distance.
   - Add the left child to the queue with a horizontal distance decremented by 1.
   - Add the right child to the queue with a horizontal distance incremented by 1.
4. After traversal, extract the values from the dictionary and sort them by horizontal distance to get the bottom view.

### Python Implementation

Here’s a complete implementation in Python:

```python
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def bottom_view(root):
    if not root:
        return []

    # Dictionary to store the bottom view of the binary tree
    bottom_view_map = {}

    # Queue for level order traversal. Stores tuples of (node, horizontal_distance)
    queue = deque([(root, 0)])

    while queue:
        node, hd = queue.popleft()
        
        # Update the dictionary with the node's value at the current horizontal distance
        bottom_view_map[hd] = node.key

        # Add left child to the queue with horizontal distance hd-1
        if node.left:
            queue.append((node.left, hd - 1))

        # Add right child to the queue with horizontal distance hd+1
        if node.right:
            queue.append((node.right, hd + 1))

    # Extracting the bottom view from the dictionary and sorting by horizontal distance
    bottom_view_result = [bottom_view_map[hd] for hd in sorted(bottom_view_map)]

    return bottom_view_result

# Example usage:
# Constructing the following binary tree
#          20
#         /  \
#        8   22
#       / \   \
#      5   3   25
#         / \
#        10  14

root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(25)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)

print(bottom_view(root))  # Output: [5, 10, 3, 14, 25]
```

### Time and Space Complexity

- **Time Complexity:**
  - The algorithm performs a level order traversal which visits each node exactly once, hence the time complexity is \(O(N)\), where \(N\) is the number of nodes in the binary tree.
  
- **Space Complexity:**
  - The space complexity consists of the space for the queue and the dictionary.
  - In the worst case, the queue can hold up to \(O(N)\) nodes, and the dictionary can also store up to \(O(N)\) horizontal distances.
  - Thus, the overall space complexity is \(O(N)\).