### Find min and max value in a BST

Find the minimum and maximum values in a Binary Search Tree (BST) step by step, along with their time and space complexities.

- **Time Complexity:** \(O(h)\)

- **Space Complexity:** \(O(1)\)

### Binary Search Tree (BST) Properties
1. **Left Subtree**: All nodes in the left subtree have values less than the root.
2. **Right Subtree**: All nodes in the right subtree have values greater than the root.
3. **No Duplicates**: There are no duplicate nodes.

### Finding the Minimum Value in a BST

To find the minimum value in a BST, we keep moving to the left child of the node until we reach the leftmost node, which will have the smallest value.

#### Algorithm
1. Start at the root node.
2. While the current node has a left child, move to the left child.
3. When there is no left child, the current node is the leftmost node and hence contains the minimum value.

#### Pseudocode
```python
def find_minimum(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.value
```

### Finding the Maximum Value in a BST

To find the maximum value in a BST, we keep moving to the right child of the node until we reach the rightmost node, which will have the largest value.

#### Algorithm
1. Start at the root node.
2. While the current node has a right child, move to the right child.
3. When there is no right child, the current node is the rightmost node and hence contains the maximum value.

#### Pseudocode
```python
def find_maximum(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.value
```

### Example

Consider the following BST:

```
       10
      /  \
     5    20
    / \   / \
   3   7 15 25
```

- The minimum value is found by following the left children: 10 -> 5 -> 3. So, the minimum value is 3.
- The maximum value is found by following the right children: 10 -> 20 -> 25. So, the maximum value is 25.

### Time Complexity

- **Finding Minimum**: O(h), where h is the height of the tree.
- **Finding Maximum**: O(h), where h is the height of the tree.

In the worst case, the height of the tree can be O(n) for a skewed tree (where n is the number of nodes), and in the best case (for a balanced tree), the height is O(log n).

### Space Complexity

- **Finding Minimum**: O(1), because no extra space is used other than a few pointers/variables.
- **Finding Maximum**: O(1), because no extra space is used other than a few pointers/variables.

### Complete Python Implementation
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def find_minimum(self):
        return self._find_minimum(self.root)

    def _find_minimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def find_maximum(self):
        return self._find_maximum(self.root)

    def _find_maximum(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.value

# Example usage
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(20)
bst.insert(3)
bst.insert(7)
bst.insert(15)
bst.insert(25)

print("Minimum value in BST:", bst.find_minimum())  # Output: 3
print("Maximum value in BST:", bst.find_maximum())  # Output: 25
```

In this implementation, the `BST` class includes methods to insert values and find the minimum and maximum values in the tree. The example usage demonstrates how to use these methods.