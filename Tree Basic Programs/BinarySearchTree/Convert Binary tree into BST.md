### Convert Binary tree into BST

Convert a binary tree into a binary search tree (BST) while preserving the original tree's structure, follow these steps:

- **Time Complexity:** \(O(n log n)\)

- **Space Complexity:** \(O(n)\)

1. **Inorder Traversal to Extract Elements**: Perform an inorder traversal of the binary tree to collect its elements. Inorder traversal of a binary tree visits nodes in the order of left child, root, and right child.

2. **Sort the Elements**: Sort the collected elements. This sorted list will represent the inorder traversal of the final BST, as inorder traversal of a BST visits nodes in ascending order.

3. **Reassign Elements to the Tree using Inorder Traversal**: Perform another inorder traversal of the binary tree, but this time reassign the values from the sorted list to the nodes.

### Step-by-Step Solution

#### Step 1: Inorder Traversal to Extract Elements

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(node, elements):
    if node:
        inorder_traversal(node.left, elements)
        elements.append(node.val)
        inorder_traversal(node.right, elements)
```

#### Step 2: Sort the Elements

```python
elements = []
inorder_traversal(root, elements)
elements.sort()
```

#### Step 3: Reassign Elements to the Tree using Inorder Traversal

```python
def inorder_assign(node, elements_iter):
    if node:
        inorder_assign(node.left, elements_iter)
        node.val = next(elements_iter)
        inorder_assign(node.right, elements_iter)

sorted_elements = iter(elements)
inorder_assign(root, sorted_elements)
```

### Full Implementation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(node, elements):
    if node:
        inorder_traversal(node.left, elements)
        elements.append(node.val)
        inorder_traversal(node.right, elements)

def inorder_assign(node, elements_iter):
    if node:
        inorder_assign(node.left, elements_iter)
        node.val = next(elements_iter)
        inorder_assign(node.right, elements_iter)

def binary_tree_to_bst(root):
    elements = []
    inorder_traversal(root, elements)
    elements.sort()
    sorted_elements = iter(elements)
    inorder_assign(root, sorted_elements)

# Example usage:
# Construct the binary tree
#       10
#      /  \
#     2    7
#    / \
#   8   4

root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(8)
root.left.right = TreeNode(4)

binary_tree_to_bst(root)
# The tree is now converted to BST
#       7
#      /  \
#     4    10
#    / \
#   2   8
```

### Time Complexity

1. **Inorder Traversal to Extract Elements**: O(n), where n is the number of nodes in the tree.
2. **Sorting the Elements**: O(n log n).
3. **Inorder Traversal to Reassign Elements**: O(n).

Overall time complexity: O(n log n) due to the sorting step.

### Space Complexity

1. **Space for Inorder Traversal**: O(n) for the elements list.
2. **Space for Recursion Stack**: O(h), where h is the height of the tree. In the worst case, this could be O(n) for a skewed tree, but on average, it is O(log n) for a balanced tree.

Overall space complexity: O(n).