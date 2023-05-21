#To download in build binarytree python library
#we need to use the following command using pip
#-----------------------
# pip install binarytree
#-----------------------

# Possible execeptions
# Note: If left or right child node is not an instance of binarytree.Node class 
# then binarytree.exceptions.NodeTypeError is raised and if the node value is 
# not a number then binarytree.exceptions.NodeValueError is raised.

from binarytree import tree

# Create a random binary tree of any height
root = tree()
print("Binary tree of any height :")
print(root)

# Create a random binary tree of any given height
root2 = tree(height = 2)
print("Binary tree of given height :")
print(root2)

#Create a random perfect binary tree of given height
root3 = tree(height=2,is_perfect=True)
print("Perfect binary tree of given height :")
print(root3)

'''
Binary tree of any height :

  ______0
 /       \
8__       2
   \
    9
   / \
  4   1

Binary tree of given height :

4__
   \
    2
   / \
  5   0

Perfect binary tree of given height :

    __6__
   /     \
  0       4
 / \     / \
5   3   2   1
'''