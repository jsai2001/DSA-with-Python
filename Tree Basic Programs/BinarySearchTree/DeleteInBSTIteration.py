# Time Complexity: O(h)
# Space Complexity: O(1) (due to the recursion stack not involved in deletion process (not considering inorder and insert functions))
"""
Deleting a node from a Binary Search Tree (BST) in Python involves several steps. 
The complexity arises because there are three main scenarios to handle:

The node to be deleted is a leaf node (no children).
The node to be deleted has one child.
The node to be deleted has two children.

Here’s a detailed guide to implement the deletion function in a BST:

Steps to Delete a Node
Find the Node to be Deleted: Traverse the tree to locate the node.

Handle Different Cases:
Node is a Leaf: Simply remove it.
Node has One Child: Replace the node with its child.
Node has Two Children: Find the in-order successor (smallest node in the right subtree) or in-order predecessor (largest node in the left subtree), 
replace the node’s value with the successor/predecessor value, and then delete the successor/predecessor.

Implementation
Below is the Python implementation of deleting a node in a BST:

Code with Iterative Approach (for O(1) space complexity)
To achieve O(1) space complexity, you would need to implement the deletion function iteratively. 
Here is how you can do it:
"""
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def deleteNode(root, key):
    parent = None
    current = root

    # Find the node to be deleted and its parent
    while current is not None and current.val != key:
        parent = current
        if key < current.val:
            current = current.left
        else:
            current = current.right

    # Node not found
    if current is None:
        return root

    # Node with two children
    if current.left is not None and current.right is not None:
        # Find in-order successor (smallest in the right subtree)
        successor_parent = current
        successor = current.right
        while successor.left is not None:
            successor_parent = successor
            successor = successor.left

        # Replace current's value with successor's value
        current.val = successor.val

        # Set current to successor and update parent
        parent = successor_parent
        current = successor

    # Node with one child or no child
    if current.left is not None:
        child = current.left
    else:
        child = current.right

    # If the node to be deleted is the root node
    if parent is None:
        root = child
    elif parent.left == current:
        parent.left = child
    else:
        parent.right = child

    return root

# Helper functions as before
def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Example usage
root = None
keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    root = insert(root, key)

print("Inorder traversal of the given tree")
inorder(root)
print()

root = deleteNode(root, 20)
print("Inorder traversal of the modified tree after deleting 20")
inorder(root)
print()

root = deleteNode(root, 30)
print("Inorder traversal of the modified tree after deleting 30")
inorder(root)
print()

root = deleteNode(root, 50)
print("Inorder traversal of the modified tree after deleting 50")
inorder(root)
print()
"""
In this iterative approach, the space complexity is O(1) as it does not use the call stack for recursion. 
However, the time complexity remains O(h).
"""