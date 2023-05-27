# AVL Tree implementation in python
# Refer notes , before visiting the code
class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def insert_node(self,root,value):
        if not root: #If there is no root node yet! , then create one
            return Node(value)
        elif value<root.data: 
            #Iterate left to insert , if the node's value to be inserted is lesser than the current node's value
            root.left = self.insert_node(root.left,value)
        else:
            #Iterate right to insert , if the node's value to be inserted is greater than the current node's value
            root.right = self.insert_node(root.right,value)
        
        root.height = 1 + max(self.avl_Height(root.left),self.avl_Height(root.right))
        
        # Update the balance factor and balance the tree
        balanceFactor = self.avl_BalanceFactor(root)
        if balanceFactor > 1:
            if value < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if value > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
        
    def avl_Height(self,root):
        if not root: #If it is a leaf node or the tree is empty
            return 0
        return root.height
    
    # Get balance factors of the node
    def avl_BalanceFactor(self,root):
        if not root:
            return 0
        return self.avl_Height(root.left) - self.avl_Height(root.right)
    
    def avl_MinValue(self,root):
        if root is None or root.left is None: #Return left most node
            return root
        return self.avl_MinValue(root.left)
    
    def preOrder(self,root):
        if not root:
            return
        print(" {0} ".format(root.data),end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)
    
    def leftRotate(self,b):
        # This is typical left rotate of the V traingle
        # Try to draw the tree on paper and check it
        a = b.right
        T2 = a.left
        
        a.left = b
        b.right = T2
        
        b.height = 1 + max(self.avl_Height(b.left),self.avl_Height(b.right))
        a.height = 1 + max(self.avl_Height(a.left),self.avl_Height(a.right))
        return a
    
    def rightRotate(self,b):
        # This is typical right rotate of the V traingle
        # Try to draw the tree on paper and check it
        a = b.left
        T3 = a.right
        
        a.right = b
        b.left = T3
        
        b.height = 1 + max(self.avl_Height(b.left),self.avl_Height(b.right))
        a.height = 1 + max(self.avl_Height(a.left),self.avl_Height(a.right))
        return a
    
    def delete_node(self,root,value):
        # Find the node to be deleted and remove it
        if not root:
            return root
        elif value < root.data:
            root.left = self.delete_node(root.left,value)
        elif value > root.data:
            root.right = self.delete_node(root.right,value)
        else:
            if root.left is None: #If leaf node
                temp = root.right
                root = None
                return temp
            elif root.right is None: #If leaf node
                temp = root.left
                root = None
                return temp
            #The following lines are for deletion of node , if it
            #Present in-between the root and the leaf nodes
            #Replace the current node , which is to be deleted with minimum value
            #In right subtree , and delete that minimum node from the tree later
            #To avoid duplicates
            temp = self.avl_MinValue(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right,temp.data)
        if root is None:
            return root
        
        #Update the balance factor of nodes
        root.height = 1 + max(self.avl_Height(root.left),self.avl_Height(root.right))
        balanceFactor = self.avl_BalanceFactor(root)
        
        #Balance the tree
        if balanceFactor > 1:
            if self.avl_BalanceFactor(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.avl_BalanceFactor(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
Tree = AVLTree()
root = None
root = Tree.insert_node(root,40)
root = Tree.insert_node(root,60)
root = Tree.insert_node(root,50)
root = Tree.insert_node(root,70)
print("PRE-ORDER")
Tree.preOrder(root)

