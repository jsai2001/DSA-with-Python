### Height of a tree

To solve the problem of finding the height of a tree, we need to understand what the height of a tree is and how we can compute it. Here, I'll describe the problem, present a solution in Python, and discuss the time and space complexity.

- **Time Complexity:** \(O(N)\)

- **Space Complexity:** \(O(\log N)\)

### Definition
The **height** of a tree is the length of the longest path from the root node to a leaf node. The height of a tree with a single node (the root) is 0.

### Approach
We'll use a recursive approach to compute the height of a tree. The idea is to find the height of the left and right subtrees recursively and then use these values to determine the height of the tree.

### Steps:
1. If the tree is empty (i.e., the root is `None`), the height is -1.
2. If the tree has only one node, the height is 0.
3. Recursively find the height of the left and right subtrees.
4. The height of the tree is the maximum of the heights of the left and right subtrees, plus one.

### Example Tree
Let's consider the following binary tree:
```
       1
      / \
     2   3
    / \
   4   5
```
The height of this tree is 2.

### Implementation
Here is the Python implementation of the above approach:

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def height_of_tree(root):
    """
    Calculate the height of a binary tree.

    :param root: Root node of the binary tree
    :return: Height of the tree
    """
    if root is None:
        return -1  # Return -1 for an empty tree

    # Recursively compute the height of left and right subtrees
    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)

    # The height of the tree is the maximum of the heights of its subtrees, plus one
    return max(left_height, right_height) + 1

# Example usage:
# Constructing the tree:
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

print("Height of the tree:", height_of_tree(root))  # Output should be 2
```

### Time Complexity
The time complexity of this algorithm is \(O(N)\), where \(N\) is the number of nodes in the tree. This is because we visit each node exactly once to compute its height.

### Space Complexity
The space complexity of this algorithm is \(O(H)\), where \(H\) is the height of the tree. This is because of the recursive call stack, which in the worst case (for a skewed tree) will have a depth equal to the height of the tree. In the best case (for a balanced tree), the height is \(\log N\), resulting in space complexity \(O(\log N)\).

### Conclusion
We have defined and solved the problem of finding the height of a tree using a recursive approach, and we have analyzed the time and space complexity of the solution. The implementation is straightforward and efficient for this problem.