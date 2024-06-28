### Find Kth smallest element in a BST

To find the Kth smallest element in a Binary Search Tree (BST), we can use an inorder traversal. Inorder traversal of a BST gives nodes in ascending order. By counting the nodes visited during this traversal, we can identify the Kth smallest element.

- **Time Complexity:** \(O(N)\)

- **Space Complexity:** \(O(H)\)

### Steps to Find the Kth Smallest Element in a BST

1. **Perform Inorder Traversal**:
   - Traverse the left subtree.
   - Visit the root node.
   - Traverse the right subtree.

2. **Keep Count of Nodes Visited**:
   - Use a counter to keep track of the number of nodes visited.
   - When the counter reaches K, we have found the Kth smallest element.

### Implementation

Here is a Python implementation of this approach:

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def kth_smallest(root, K):
    def inorder(node):
        nonlocal count, result
        if not node or count >= K:
            return
        inorder(node.left)
        count += 1
        if count == K:
            result = node.value
            return
        inorder(node.right)
    
    count = 0
    result = None
    inorder(root)
    return result
```

### Example Usage

```python
# Create the BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

# Find the 3rd smallest element
print(kth_smallest(root, 3))  # Output: 4
```

### Time Complexity

The time complexity of this algorithm is \(O(N)\) in the worst case, where \(N\) is the number of nodes in the BST. This is because we might need to visit all the nodes in the tree in the worst-case scenario.

### Space Complexity

The space complexity is \(O(H)\), where \(H\) is the height of the tree. This space is used by the recursive call stack. In the best case, for a balanced tree, the height \(H\) is \(\log N\). In the worst case, for a completely unbalanced tree (e.g., a linked list), the height \(H\) is \(N\).