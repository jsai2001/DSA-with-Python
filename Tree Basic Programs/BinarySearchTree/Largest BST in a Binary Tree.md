### Largest BST in a Binary Tree

To find the largest Binary Search Tree (BST) in a given Binary Tree, we need to identify the largest subtree that adheres to the BST properties within the given tree. 

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(h)\)

Here's a step-by-step explanation, along with the implementation and complexity analysis.

### Explanation

To solve this problem, we need to traverse the binary tree and for each node, determine whether the subtree rooted at that node is a BST. While doing this, we need to track the size of the largest BST found.

#### Steps:

1. **Define a Helper Function**:
   - This function will be used to determine if a subtree rooted at a given node is a BST.
   - It will return a tuple containing:
     - Whether the subtree is a BST.
     - The size of the largest BST in the subtree.
     - The minimum value in the subtree.
     - The maximum value in the subtree.
   
2. **Recursive Traversal**:
   - Traverse the tree in a post-order manner (left, right, root).
   - For each node, use the helper function to get information about the left and right subtrees.
   - Use the information from the left and right subtrees to determine if the current subtree is a BST.
   - Update the size of the largest BST if the current subtree is a BST and its size is larger than the previously found largest BST.

#### Pseudocode

1. Define the helper function `largestBSTSubtreeHelper(node)`:
    - Base case: If the node is `null`, return a tuple indicating an empty BST.
    - Recursively call the helper function on the left and right children.
    - Check if the current subtree rooted at `node` is a BST using the results from the left and right children.
    - If it is a BST, update the size and return the appropriate values.
    - If it is not a BST, return the size of the largest BST found so far.

2. Call the helper function on the root of the tree and extract the size of the largest BST.

### Code

Here is the Python implementation of the above logic:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestBSTSubtree(root):
    def largestBSTSubtreeHelper(node):
        # Base case: An empty tree is a BST of size 0.
        if not node:
            return (True, 0, float('inf'), float('-inf'))

        # Recursively get info from left and right subtrees.
        left_is_bst, left_size, left_min, left_max = largestBSTSubtreeHelper(node.left)
        right_is_bst, right_size, right_min, right_max = largestBSTSubtreeHelper(node.right)

        # Check if the current node is a BST.
        if left_is_bst and right_is_bst and left_max < node.val < right_min:
            current_size = left_size + right_size + 1
            return (True, current_size, min(left_min, node.val), max(right_max, node.val))
        else:
            # Return false with the size of the largest BST found so far.
            return (False, max(left_size, right_size), 0, 0)

    # The second element of the tuple is the size of the largest BST.
    return largestBSTSubtreeHelper(root)[1]

# Example usage:
# Constructing a binary tree
#        10
#       /  \
#      5   15
#     / \    \
#    1   8   17

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(17)

print(largestBSTSubtree(root))  # Output should be 3 (the subtree rooted at node 5)
```

### Time and Space Complexity

- **Time Complexity**: \(O(n)\)
  - We traverse each node once, performing constant-time operations at each node.
  
- **Space Complexity**: \(O(h)\)
  - The space complexity is determined by the height of the tree due to the recursion stack. In the worst case (for an unbalanced tree), this can be \(O(n)\), but for a balanced tree, it is \(O(\log n)\).

This solution ensures we efficiently find the largest BST in a given binary tree using a recursive post-order traversal approach.