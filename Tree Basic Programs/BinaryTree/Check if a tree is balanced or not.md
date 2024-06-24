### Check if a tree is balanced or not

To determine if a binary tree is balanced, we need to verify that the tree satisfies the balanced binary tree property. A binary tree is balanced if, for every node in the tree, the height difference between its left and right subtrees is at most 1. Here's a step-by-step explanation and implementation of an algorithm to check if a binary tree is balanced, along with its time and space complexity analysis.

- **Time Complexity:** \(O(N)\)

- **Space Complexity:** \(O(log N)\)

### Approach

1. **Recursive Depth-First Search (DFS):** We can use a recursive approach to traverse the tree and check the balance condition at each node.
2. **Height Calculation:** For each node, calculate the heights of the left and right subtrees.
3. **Balance Check:** Ensure the height difference between the left and right subtrees is no more than 1.
4. **Propagate Balance Status:** If any subtree is unbalanced, propagate this information up the tree.

### Algorithm

To implement this, we define a helper function that computes both the height of a subtree and whether the subtree is balanced. This function will:
- Return `(-1, False)` if the subtree is unbalanced.
- Return `(height, True)` if the subtree is balanced.

Here's the Python code implementing this algorithm:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: TreeNode) -> bool:
    def check_balance(node: TreeNode) -> (int, bool):
        # An empty subtree is balanced and its height is -1
        if not node:
            return -1, True

        # Check left subtree
        left_height, left_balanced = check_balance(node.left)
        if not left_balanced:
            return -1, False

        # Check right subtree
        right_height, right_balanced = check_balance(node.right)
        if not right_balanced:
            return -1, False

        # Current node is balanced if the height difference is no more than 1
        if abs(left_height - right_height) > 1:
            return -1, False

        # Height of the current node
        current_height = max(left_height, right_height) + 1
        return current_height, True

    # Start the balance check from the root
    _, is_bal = check_balance(root)
    return is_bal
```

### Explanation

1. **TreeNode Class:** This class defines the structure of each node in the binary tree.
2. **is_balanced Function:** This is the main function that checks if the tree is balanced.
3. **check_balance Helper Function:** This recursive function performs the following tasks:
   - Returns `(-1, True)` for an empty subtree.
   - Recursively calculates the height and balance status of the left and right subtrees.
   - Checks the balance condition for the current node.
   - Returns the height and balance status for the current node.

### Time Complexity

The time complexity of this algorithm is \(O(N)\), where \(N\) is the number of nodes in the binary tree. This is because each node is visited once, and the height of its subtrees is calculated in constant time.

### Space Complexity

The space complexity is \(O(H)\), where \(H\) is the height of the tree. This is due to the recursive call stack, which can be as deep as the height of the tree. In the worst case (an unbalanced tree), this can be \(O(N)\), but in the best case of a balanced tree, it is \(O(log N)\).

This algorithm efficiently checks if a binary tree is balanced using a recursive approach, ensuring that each node is processed only once.