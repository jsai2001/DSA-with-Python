#To download in build binarytree python library
#we need to use the following command using pip
#-----------------------
# pip install binarytree
#-----------------------

# Possible execeptions
# Note: If left or right child node is not an instance of binarytree.Node class 
# then binarytree.exceptions.NodeTypeError is raised and if the node value is 
# not a number then binarytree.exceptions.NodeValueError is raised.

#Creating binary tree from given list
from binarytree import build

'''
Instead of using the Node method repeatedly, 
we can use build() method to convert a list of values into a binary tree.
Here, a given list contains the nodes of tree such that the element at index i 
has its left child at index 2*i+1, the right child at index 2*i+2 
and parent at (i – 1)//2. The elements at index j for j>len(list)//2 are leaf nodes. 
None indicates the absence of a node at that index. 
We can also get the list of nodes back after building a binary tree using values attribute.
'''

# List of nodes
nodes =[3, 6, 8, 2, 11, None, 13]

# Building the binary tree
binary_tree = build(nodes)
print('Binary tree from list :\n',binary_tree)

# Getting list of nodes from binarytree
print('\nList from binary tree :',binary_tree.values)