### Boundary Traversal of a Binary Tree

To solve the problem of finding the boundary traversal of a binary tree, we need to traverse the tree in a specific order:
1. Left boundary (excluding leaf nodes and root).
2. Leaf nodes.
3. Right boundary (excluding leaf nodes and root, in reverse order).

- **Time Complexity:** \(O(N)\)

- **Space Complexity:** \(O(N)\)

Here’s a step-by-step explanation and the implementation in Python:

### Step-by-Step Explanation

1. **Left Boundary**:
   - Traverse from the root to the left-most node, collecting nodes along the way, but excluding leaf nodes and the root.

2. **Leaf Nodes**:
   - Traverse the tree and collect all the leaf nodes.

3. **Right Boundary**:
   - Traverse from the root to the right-most node, collecting nodes along the way, but excluding leaf nodes and the root.
   - The collected nodes are then reversed to ensure the correct order.

### Implementation

```python
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printBoundary(root):
    if not root:
        return

    result = []

    def isLeaf(node):
        return node.left is None and node.right is None

    def addLeftBoundary(node):
        while node:
            if not isLeaf(node):
                result.append(node.data)
            if node.left:
                node = node.left
            else:
                node = node.right

    def addLeaves(node):
        if isLeaf(node):
            result.append(node.data)
        if node.left:
            addLeaves(node.left)
        if node.right:
            addLeaves(node.right)

    def addRightBoundary(node):
        stack = []
        while node:
            if not isLeaf(node):
                stack.append(node.data)
            if node.right:
                node = node.right
            else:
                node = node.left
        while stack:
            result.append(stack.pop())

    if not isLeaf(root):
        result.append(root.data)

    addLeftBoundary(root.left)
    addLeaves(root)
    addRightBoundary(root.right)

    return result

# Example Usage
# Constructing the binary tree:
#          20
#         /  \
#        8   22
#       / \    \
#      4   12   25
#         /  \
#        10  14
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right.right = Node(25)

print(printBoundary(root))  # Output: [20, 8, 4, 10, 14, 25, 22]
```

### Time and Space Complexity

- **Time Complexity**: \(O(N)\)
  - Each node is visited at most three times: once for the left boundary, once for the leaves, and once for the right boundary.
  
- **Space Complexity**: \(O(N)\)
  - The space complexity is primarily due to the storage of nodes in the result list. Additionally, the call stack for the recursive leaf node collection can go up to \(O(N)\) in the worst case (skewed tree).

This implementation ensures a clear traversal following the boundary traversal rules and efficiently collects the boundary nodes.