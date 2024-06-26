### Check if a Binary Tree contains duplicate subtrees of size 2 or more

To solve the problem of checking if a binary tree contains duplicate subtrees of size 2 or more, we can use a hashing technique to efficiently store and compare subtrees. Here’s a detailed solution:

### Problem Definition
Given a binary tree, determine if there are any duplicate subtrees of size 2 or more. A subtree is defined by its root and includes all its descendants.

- **Time Complexity:** \(O(n)\)

- **Space Complexity:** \(O(n)\)

### Approach
1. **Serialize Subtrees**: Use a post-order traversal to serialize each subtree. The serialization of a subtree will uniquely identify its structure and node values.
2. **Hashing**: Store the serialized subtrees in a hash map. If a serialized subtree appears more than once, it means there is a duplicate subtree.
3. **Subtree Size Check**: Ensure that we only consider subtrees of size 2 or more.

### Steps
1. Perform a post-order traversal of the binary tree.
2. For each subtree, serialize it into a string.
3. Use a hash map to store and count the serialized subtrees.
4. Check for duplicates in the hash map.

### Algorithm
```python
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def serialize_subtree(root, subtree_map):
    if root is None:
        return "#"
    
    left_serial = serialize_subtree(root.left, subtree_map)
    right_serial = serialize_subtree(root.right, subtree_map)
    
    # Serialize current subtree
    serial = f"{left_serial},{right_serial},{root.val}"
    
    # Only consider subtrees of size 2 or more
    if len(serial.split(',')) > 3:
        if serial in subtree_map:
            subtree_map[serial] += 1
        else:
            subtree_map[serial] = 1
    
    return serial

def has_duplicate_subtree(root):
    subtree_map = {}
    serialize_subtree(root, subtree_map)
    
    # Check if any serialized subtree appears more than once
    for key in subtree_map:
        if subtree_map[key] > 1:
            return True
    
    return False
```

### Explanation
- **TreeNode class**: Defines the structure of a node in the binary tree.
- **serialize_subtree function**: Recursively serializes each subtree using post-order traversal (left, right, root). It uses "#" to denote null nodes and constructs a string that uniquely identifies the subtree.
- **has_duplicate_subtree function**: Initializes a hash map to store the serialized subtrees and their counts. It then calls `serialize_subtree` to fill the hash map and checks for duplicates.

### Time Complexity
- The traversal of the tree is O(n), where n is the number of nodes in the tree.
- Serialization and hash map operations (insert and lookup) are average O(1) for each node.
- Thus, the overall time complexity is O(n).

### Space Complexity
- The space complexity is O(n) for the hash map to store serialized subtrees.
- Additionally, the recursion stack can go as deep as the height of the tree, which is O(h), where h is the height of the tree.
- In the worst case, the space complexity is O(n).

### Example
Consider the following binary tree:
```
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
```
- Subtree (2,4) appears more than once.
- The function `has_duplicate_subtree` will return `True` for this tree.