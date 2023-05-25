#To download in build binarytree python library
#we need to use the following command using pip
#-----------------------
# pip install binarytree
#-----------------------

# Possible execeptions
# Note: If left or right child node is not an instance of binarytree.Node class 
# then binarytree.exceptions.NodeTypeError is raised and if the node value is 
# not a number then binarytree.exceptions.NodeValueError is raised.

from binarytree import Node

root = Node(3)
root.left = Node(6)
root.right = Node(8)

# Getting binary tree
print('Binary tree :',root)

# Getting list of nodes
print('List of nodes :',list(root))

# Getting inorder of nodes
print('Inorder of nodes :',root.inorder)

# Getting preorder of nodes
print('Preorder of nodes :',root.preorder)

# Getting postorder of nodes
print('Postorder of nodes :',root.postorder)

# Checking tree properties
print('Size of tree :',root.size)
print('Height of tree :',root.height)

# Get all properites at once
print('Properties of tree : \n',root.properties)

# Output
'''
Binary tree : 
  3
 / \
6   8

List of nodes : [Node(3), Node(6), Node(8)]
Inorder of nodes : [Node(6), Node(3), Node(8)]
Preorder of nodes : [Node(3), Node(6), Node(8)]
Postorder of nodes : [Node(6), Node(8), Node(3)]
Size of tree : 3
Height of tree : 1
Properties of tree : 
 {'height': 1, 'size': 3, 'is_max_heap': False, 'is_min_heap': True, 'is_perfect': True, 'is_strict': True, 'is_complete': True, 'leaf_count': 2, 'min_node_value': 3, 'max_node_value': 8, 'min_leaf_depth': 1, 'max_leaf_depth': 1, 'is_balanced': True, 'is_bst': False, 'is_symmetric': False}
'''
