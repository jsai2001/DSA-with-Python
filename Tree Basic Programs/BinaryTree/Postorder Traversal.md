### Postorder traversal of a binary tree

Postorder traversal of a binary tree involves visiting the nodes in the order of left subtree, right subtree, and then the root node. This traversal can be implemented both recursively and iteratively. Below are both approaches with detailed explanations and analyses of their time and space complexities.

- **Time Complexity:** \(O(N)\)

- **Space Complexity:** \(O(N)\)

### Recursive Approach

**Algorithm:**

1. Traverse the left subtree.
2. Traverse the right subtree.
3. Visit the root node.

**Code Implementation:**

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def postorder_traversal_recursive(node, result=None):
    if result is None:
        result = []
    
    if node:
        postorder_traversal_recursive(node.left, result)
        postorder_traversal_recursive(node.right, result)
        result.append(node.value)
    
    return result

# Example usage:
# root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
# print(postorder_traversal_recursive(root))
```

**Time Complexity:**
- **O(n)**, where \( n \) is the number of nodes in the tree. Each node is visited exactly once.

**Space Complexity:**
- **O(h)** for the call stack, where \( h \) is the height of the tree. In the worst case (a completely unbalanced tree), this could be O(n).

### Iterative Approach

**Algorithm:**

1. Use a stack to simulate the recursive call stack.
2. Push the root node and initialize an empty stack and result list.
3. Pop a node, push its value to a temporary stack, and push its left and right children (if they exist) to the main stack.
4. After processing all nodes, pop nodes from the temporary stack to get the postorder traversal.

**Code Implementation:**

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def postorder_traversal_iterative(root):
    if not root:
        return []

    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return result[::-1]

# Example usage:
# root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
# print(postorder_traversal_iterative(root))
```

**Time Complexity:**
- **O(n)**, where \( n \) is the number of nodes in the tree. Each node is visited exactly once.

**Space Complexity:**
- **O(n)**, for the stack and the result list. In the worst case, the stack will hold all nodes (for example, in a skewed tree).

### Explanation of Iterative Approach:

1. **Initialization:**
   - `stack` is initialized with the root node.
   - `result` is initialized as an empty list.

2. **Traversal:**
   - Pop the top node from the stack and append its value to `result`.
   - Push the left and right children of the node to the stack (if they exist).
   - Repeat until the stack is empty.

3. **Final Step:**
   - Since `result` contains nodes in the order of root, right, and left, reverse the `result` list to get the correct postorder traversal (left, right, root).

This method uses a single stack and reverses the order at the end, making it efficient and straightforward. 

Both approaches are efficient in terms of time complexity, but the iterative method is generally preferred in practice due to its controlled space usage and avoidance of potential stack overflow in deeply nested trees.