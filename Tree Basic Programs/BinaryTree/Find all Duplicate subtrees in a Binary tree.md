### Find all Duplicate subtrees in a Binary tree

To solve the problem of finding all duplicate subtrees in a binary tree, we can use a postorder traversal approach combined with serialization of subtrees. Here is a step-by-step solution:

### Problem Definition

Given a binary tree, we need to find all subtrees that appear more than once. A subtree is defined by a node and all its descendants.

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(n)\)

### Approach

1. **Serialize Subtrees**: Convert each subtree to a string representation. This allows easy comparison of subtrees.
2. **Use a HashMap**: Store each serialized subtree in a hashmap along with its frequency of occurrence.
3. **Postorder Traversal**: Traverse the tree in postorder fashion (left, right, root) to ensure that each subtree is considered in its entirety before the parent node.
4. **Identify Duplicates**: Check the hashmap to identify subtrees that appear more than once.

### Implementation

Here is the detailed implementation in Python:

```python
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findDuplicateSubtrees(root):
    def serialize(node, lookup):
        if not node:
            return '#'
        left_serial = serialize(node.left, lookup)
        right_serial = serialize(node.right, lookup)
        serial = f'{node.val},{left_serial},{right_serial}'
        lookup[serial].append(node)
        return serial

    lookup = defaultdict(list)
    serialize(root, lookup)
    
    # Extract subtrees with more than one occurrence
    duplicates = [nodes[0] for nodes in lookup.values() if len(nodes) > 1]
    
    return duplicates

# Helper function to print the tree (for verification)
def printTree(root):
    if not root:
        return "None"
    return f'{root.val} ({printTree(root.left)}) ({printTree(root.right)})'

# Example usage:
# Constructing a binary tree:
#       1
#      / \
#     2   3
#    /   / \
#   4   2   4
#      /
#     4
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)

# Find duplicates
duplicates = findDuplicateSubtrees(root)
for node in duplicates:
    print(printTree(node))
```

### Explanation

1. **TreeNode Class**: Defines the structure of a tree node.
2. **findDuplicateSubtrees Function**: This is the main function that finds and returns the list of duplicate subtrees.
    - `serialize` Function: Converts a subtree rooted at a given node to a string representation. This function updates a hashmap (`lookup`) where the keys are serialized subtrees and the values are lists of nodes with that subtree.
    - Postorder traversal is used in `serialize` to ensure the complete subtree is processed before the parent node.
3. **printTree Function**: A helper function to print the tree structure for verification purposes.

### Time Complexity

- **Serialization**: Each node is visited once, and the serialization of each node takes constant time, resulting in an O(n) complexity where n is the number of nodes.
- **HashMap Operations**: Insertion and lookup in the hashmap are O(1) on average.
- Therefore, the overall time complexity is **O(n)**.

### Space Complexity

- **HashMap Storage**: In the worst case, we store a string for each node. If all nodes have unique subtrees, we store n strings.
- **Call Stack**: The depth of the recursion is equal to the height of the tree, which is O(h) in the worst case.
- Therefore, the overall space complexity is **O(n)**.