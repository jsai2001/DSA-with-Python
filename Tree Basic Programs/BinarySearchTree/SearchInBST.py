# Time Complexity: O(h) in average case , O(n) in worst case
# Space Complexity: O(1)
"""
To find a value in a Binary Search Tree (BST), 
you can follow a straightforward algorithm leveraging the properties of a BST. 
Here's a step-by-step explanation of how to do this:

Start at the root node: Begin the search at the root of the BST.
Compare the target value with the current node's value:
If the target value is equal to the current node's value, you have found the value, and the search is complete.
If the target value is less than the current node's value, move to the left child node.
If the target value is greater than the current node's value, move to the right child node.
Repeat the process: Continue comparing and moving left or right until you either find the target value or reach a leaf node (a node with no children).
If a leaf node is reached: If you reach a leaf node and the target value has not been found, the value is not present in the BST.
Here is a simple implementation in Python:
"""
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def search_bst(root, target):
    current = root
    while current:
        if target == current.value:
            return True  # Value found
        elif target < current.value:
            current = current.left
        else:
            current = current.right
    return False  # Value not found

# Example usage
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)

print(search_bst(root, 6))  # Output: True
print(search_bst(root, 7))  # Output: False
"""
Explanation:
TreeNode class: Defines the structure of a tree node, 
with attributes for the node's value, left child, and right child.
search_bst function: Takes the root of the BST and the target value as inputs. 
It traverses the tree starting from the root and follows the BST properties to find the target value.

Time Complexity:
The time complexity of searching in a BST is O(h), where h is the height of the tree. 
In the best case (balanced tree), h=logn, making the search operation efficient. 
However, in the worst case (skewed tree), h=n, leading to a linear time complexity.

Space Complexity:
The space complexity is O(1) for the iterative approach as it only requires a constant amount of space for the pointer to traverse the tree.
This approach ensures that you can efficiently find a value in a BST using its inherent properties.
"""