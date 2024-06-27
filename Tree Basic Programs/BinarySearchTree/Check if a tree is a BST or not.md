### Check if a tree is a BST or not 

To determine if a given binary tree is a Binary Search Tree (BST), we need to ensure that for every node in the tree, the left subtree contains only nodes with values less than the node’s value, and the right subtree contains only nodes with values greater than the node’s value.

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(h)\)

Here’s a Python function to check if a binary tree is a BST:

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_bst(node, left=float('-inf'), right=float('inf')):
    """
    Check if the binary tree rooted at `node` is a Binary Search Tree (BST).
    
    A binary tree is a BST if for every node, all values in its left subtree are less than the node's value,
    and all values in its right subtree are greater than the node's value.

    Args:
    - node (TreeNode): The root of the binary tree to check.
    - left (float): The lower bound for node values (default: negative infinity).
    - right (float): The upper bound for node values (default: positive infinity).

    Returns:
    - bool: True if the tree is a BST, False otherwise.
    """
    if node is None:
        return True

    if not (left < node.value < right):
        return False

    return (is_bst(node.left, left, node.value) and 
            is_bst(node.right, node.value, right))
```

### Explanation

1. **TreeNode Class**: This class represents a node in the binary tree. It has a `value` and pointers to its left and right children.
2. **is_bst Function**:
   - **Arguments**:
     - `node`: The current node being checked.
     - `left`: The lower bound for the current node's value.
     - `right`: The upper bound for the current node's value.
   - **Base Case**: If `node` is `None`, it means we've reached a leaf node, so we return `True`.
   - **Current Node Check**: If the current node’s value is not between `left` and `right`, it violates the BST property, so we return `False`.
   - **Recursive Check**: Recursively check the left subtree with updated bounds (`left` to `node.value`) and the right subtree with updated bounds (`node.value` to `right`).

### Time Complexity

- **O(n)**: The function visits each node exactly once, where `n` is the number of nodes in the tree.

### Space Complexity

- **O(h)**: In the worst case, the recursion stack will be equal to the height of the tree (`h`). For a balanced tree, this is O(log n), and for a skewed tree, this is O(n).

This function ensures that every node adheres to the BST properties by leveraging recursion and maintaining valid value ranges for each node in the tree.