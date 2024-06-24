### Check if 2 trees are mirror or not

To determine if two binary trees are mirrors of each other, we need to verify that:

1. The root values of both trees are the same.
2. The left subtree of the first tree is a mirror of the right subtree of the second tree.
3. The right subtree of the first tree is a mirror of the left subtree of the second tree.

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(n)\)

Here is a step-by-step solution in Python with clear documentation:

### Definition of the Tree Node

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

### Function to Check if Two Trees are Mirrors

```python
def are_mirrors(tree1, tree2):
    """
    Check if two binary trees are mirrors of each other.

    :param tree1: TreeNode - the root of the first tree
    :param tree2: TreeNode - the root of the second tree
    :return: bool - True if the trees are mirrors, False otherwise
    """
    # If both trees are empty, they are mirrors
    if tree1 is None and tree2 is None:
        return True
    
    # If only one of the trees is empty, they are not mirrors
    if tree1 is None or tree2 is None:
        return False
    
    # Both trees are non-empty, check the value of the roots and recursively check subtrees
    return (tree1.value == tree2.value and
            are_mirrors(tree1.left, tree2.right) and
            are_mirrors(tree1.right, tree2.left))
```

### Example Usage

```python
# Example trees
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(3), TreeNode(2))

print(are_mirrors(tree1, tree2))  # Output: True
```

### Time and Space Complexity Analysis

**Time Complexity:**
The function `are_mirrors` visits each node of both trees exactly once, so the time complexity is O(n), where n is the number of nodes in the trees. This is because for each node, it performs a constant amount of work (comparison and two recursive calls).

**Space Complexity:**
The space complexity is determined by the recursion stack. In the worst case, the depth of the recursion stack is equal to the height of the trees. For a balanced tree, this would be O(log n), and for an unbalanced tree, this could be O(n). Thus, the worst-case space complexity is O(n).

This solution effectively checks whether two binary trees are mirrors by comparing nodes recursively and ensures that the subtrees follow the mirror condition.