# Time Complexity: O(h)
# Space Complexity: O(h) (due to the recursion stack in the recursive implementation)
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
"""
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def deleteNode(root, key):
    # Base case: if the root is None
    if root is None:
        return root

    # If the key to be deleted is smaller than the root's key,
    # then it lies in the left subtree
    if key < root.val:
        root.left = deleteNode(root.left, key)

    # If the key to be deleted is greater than the root's key,
    # then it lies in the right subtree
    elif key > root.val:
        root.right = deleteNode(root.right, key)

    # If the key is the same as the root's key, then this is the node
    # to be deleted
    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.val)

    return root

def minValueNode(node):
    current = node

    # Loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current

# Helper function to insert a new node with the given key
def insert(root, key):
    if root is None:
        return TreeNode(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

# Helper function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Example usage:
# Creating a sample BST
root = None
keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    root = insert(root, key)

print("Inorder traversal of the given tree")
inorder(root)
print()

# Deleting node with key 20
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree after deleting 20")
inorder(root)
print()

# Deleting node with key 30
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree after deleting 30")
inorder(root)
print()

# Deleting node with key 50
root = deleteNode(root, 50)
print("Inorder traversal of the modified tree after deleting 50")
inorder(root)
print()
"""
Explanation
TreeNode Class: Defines the structure of a node in the BST.
deleteNode Function: Handles the deletion process.
minValueNode Function: Finds the smallest node in a given subtree, used to find the in-order successor.
insert Function: Inserts a new node in the BST (used for building the initial tree).
inorder Function: Performs an in-order traversal of the tree, used for displaying the tree.
This code includes an example to demonstrate the process of deleting nodes and verifying the structure of the BST after each deletion.
"""
"""
Time Complexity
The time complexity of the delete operation in a Binary Search Tree (BST) is O(h), 
where h is the height of the tree. This is because:

Traversal to Find the Node: In the worst case, you might need to traverse from the root to a leaf node to find the node to be deleted, 
which takes O(h) time.
Adjusting the Tree: Once the node is found, the adjustments (whether removing a node, replacing with a child, 
or finding and replacing with an in-order successor/predecessor) also take O(h) time in the worst case, 
primarily due to the traversal to find the in-order successor/predecessor.

Space Complexity
The space complexity of the delete operation is O(h) in the worst case due to the recursion stack, 
where h is the height of the tree. This is because the function uses recursive calls to traverse the tree, 
and the maximum depth of the recursion stack will be equal to the height of the tree.

If you implement the function iteratively, 
the space complexity could be reduced to O(1) since no additional stack space would be required. 
However, the provided implementation is recursive, so the space complexity remains O(h).

Recap of Complexities
Time Complexity: O(h)
Space Complexity: O(h) (due to the recursion stack in the recursive implementation)
"""