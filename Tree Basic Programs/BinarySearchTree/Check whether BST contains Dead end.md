## Checking Whether a BST Contains a Dead End

A Binary Search Tree (BST) contains a "dead end" if there exists a leaf node such that no further nodes can be inserted into the BST. This happens when a leaf node `x` has no potential child nodes that satisfy the BST properties, meaning both `x-1` and `x+1` are already present in the BST.

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(n)\)

### Problem Explanation

In a BST:
- The left subtree of a node contains only nodes with keys less than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.

A dead end occurs if:
1. There exists a node `x` such that both `x-1` and `x+1` are also in the BST.
2. For the node with value 1, the dead end condition will be if `x+1` is present in the BST because 0 is not allowed in the BST (assuming all keys are positive).

### Solution Approach

To solve this problem, we need to check each node to determine if both its immediate neighboring values (`x-1` and `x+1`) are present in the BST. We'll use an in-order traversal to check each node while keeping track of the node values using a set for efficient lookup.

### Algorithm

1. **In-order Traversal:** Traverse the BST in-order to visit nodes in increasing order.
2. **Set to Track Values:** Use a set to keep track of the nodes that we have encountered.
3. **Dead End Check:** For each node, check if both `x-1` and `x+1` are present in the set. If found, a dead end exists.
4. **Base Case Handling:** Specifically handle the edge case for the node with value 1.

### Detailed Solution

Here's the implementation in Python:

```python
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def contains_dead_end(root):
    if root is None:
        return False

    # Set to store all nodes and leaf nodes
    all_nodes = set()
    leaf_nodes = set()

    def store_nodes_and_leafs(node):
        if node is None:
            return
        all_nodes.add(node.data)
        if node.left is None and node.right is None:
            leaf_nodes.add(node.data)
        store_nodes_and_leafs(node.left)
        store_nodes_and_leafs(node.right)

    store_nodes_and_leafs(root)

    # Checking for dead end
    for leaf in leaf_nodes:
        if (leaf - 1 in all_nodes and leaf + 1 in all_nodes) or leaf == 1:
            return True

    return False

# Helper function to create a BST
def create_bst(values):
    root = None
    for value in values:
        root = insert(root, value)
    return root

# Example usage:
# Creating a BST
bst_values = [8, 5, 3, 2, 7, 10, 9]
root = create_bst(bst_values)

# Checking for dead end
print(contains_dead_end(root))  # Output: True
```

### Explanation of Code

1. **Node Class:** Represents a node in the BST.
2. **insert Function:** Inserts a new key into the BST.
3. **contains_dead_end Function:** Checks if the BST contains a dead end.
    - **store_nodes_and_leafs Function:** Traverses the BST to store all node values and leaf node values in sets.
    - **Dead End Check:** Iterates over leaf nodes to check if both `leaf-1` and `leaf+1` are present in the set of all nodes.
4. **create_bst Function:** Helper function to create a BST from a list of values.

### Time and Space Complexity

- **Time Complexity:** O(n)
  - In-order traversal of the BST to collect nodes and leaf nodes takes O(n).
  - Checking for dead ends takes O(n) in the worst case.
- **Space Complexity:** O(n)
  - Additional space is used to store all node values and leaf node values in sets.

In summary, the solution effectively checks for dead ends in a BST using an in-order traversal and set operations, ensuring optimal time and space complexity.