# Binary tree node structure
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
'''
Properties of binary search tree
* no duplicate elements in a binary search tree.
* element at the left child of a node is always less than the element at the current node.
* left subtree of a node has all elements less than the current node.
* element at the right child of a node is always greater than the element at the current node.
* right subtree of a node has all elements greater than the current node
'''

class BinarySearchTreeNode:
    def __init__(self):
        self.parent = None
    
    def create(self,item):# Create a new node
        self.node = Node(item)
        return self.node
    
    # Inorder traversal of tree
    def inorder(self,root):
        if(root==None):
            return
        self.inorder(root.left) #Traverse left subtree
        print(root.data,end=" ") #Traverse root node
        self.inorder(root.right) #Traverse right subtree
    
    # Find the inorder successor of current node , that to be deleted
    def findMinimum(self,cur):
        while(cur.left!=None):
            cur=cur.left
        return cur
    
    # Insertion of new node in BST
    def insertion(self,root,item):
        if(root==None):
            return self.create(item) #Return new node if tree is empty
        if(item<root.data):
            root.left=self.insertion(root.left,item)
        else:
            root.right=self.insertion(root.right,item)
        return root
    
    # Searching a node in BST
    def search(self,cur,item):
        while(cur!=None and cur.data!=item):
            self.parent=cur
            if(item<cur.data):
                cur=cur.left
            else:
                cur=cur.right
        if(cur.data==item):
            return cur
        else:
            return 0
    
    # Deletion of a node in BST
    def deletion(self,root,item):
        #Initially starting with root
        cur=root
        #After finding the node to be deleted
        cur = self.search(cur,item)
        if(cur==0):
            print("\nThere is no "+item+" valued node to delete")
        else:
            # Find the node to be deleted
            if(cur==None):
                return
            if(cur.left==None and cur.right==None):
                if(cur!=root):
                    if(self.parent.left==cur):
                        self.parent.left=None
                    else:
                        self.parent.right=None
                else:
                    root=None
                del cur
            elif(cur.left and cur.right):
                succ = self.findMinimum(cur.right)
                val = succ.data
                self.deletion(root,succ.data)
                cur.data = val
            else:
                child = cur.left if cur.left else cur.right
                if(cur!=root):
                    if(cur==self.parent.left):
                        self.parent.left=child
                    else:
                        self.parent.right=child
                else:
                    root = child
                del cur

BST = BinarySearchTreeNode()
root = BST.create(45)
root = BST.insertion(root, 30)  
root = BST.insertion(root, 50)  
root = BST.insertion(root, 25)  
root = BST.insertion(root, 35)  
root = BST.insertion(root, 45)  
root = BST.insertion(root, 60)  
root = BST.insertion(root, 4)

print("\nThe inorder traversal of the given binary tree is :")
BST.inorder(root)
BST.deletion(root,25)

print("\nAfter deleting node 25, the inorder traversal of the given binary tree is :")
BST.inorder(root)
BST.insertion(root,2)

print("\nAfter inserting node 2, the inorder traversal of the given binary tree is :")
BST.inorder(root)