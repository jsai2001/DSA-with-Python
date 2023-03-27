class Node:
    def __init__(self,data):
        self.item   = data
        self.ref    = None
class LinkedList:
    def __init__(self):
        """
        Initializing the head node to None (Null)
        Initially the LL will be empty , so head points to null
        Head Node is the start node
        """
        self.start_node = None
    def traverse_list(self):
        """
        Checks if the list have an item , if have print the elements
        By traversing through nodes , else print "List has no element"
        Here n is the variable which holds the address of the head node.
        n traverses from the head node to the last node
        """
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item,end=" ")
                n = n.ref
        print()
    def insert_at_start(self,data):
        """
        We are assigning a Node into a variable with defined structure
        Having both item and ref as members for the variable "new_node"
        This is similar to the Structure
        """
        new_node            = Node(data)
        new_node.ref        = self.start_node
        self.start_node     = new_node
    def insert_at_end(self,data):
        """
        If the linked list is empty , we need to make the new node which we
        create as the start node and as well as last node , else if we have 
        some nodes , we iterate the linked list until the last node and tag
        the last node with the new node and make the new node as the last node
        """
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
    def insert_after_item(self,x,data):
        """
        We want to insert an item , after a particular value occured in the LL
        Take the reference of the head node , iterate it until current item is
        the one we need and break the loop , now we will have address of the node
        where we are having current value as x , and next to that we create a new
        node and link that node with x , x -> new_node
        """
        n = self.start_node
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("Item not in the list!!!")
        else:
            new_node        = Node(data)
            new_node.ref    = n.ref
            n.ref           = new_node
    def insert_before_item(self,x,data):
        """
        If the list is empty , print "List has no element" message and return
        Next check if the x is present on the first node , if yes , insert at start
        Assuming that data is present in between the LL , we need to traverse until
        n.ref has x , as we need to insert before the item.
        """
        if self.start_node is None:
            print("List has no element")
            return
        if x == self.start_node.item:
            new_node            = Node(data)
            new_node.ref        = self.start_node
            self.start_node     = new_node
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("Item is not in the list")
        else:
            new_node         = Node(data)
            new_node.ref     = n.ref
            n.ref            = new_node
    def insert_at_index(self,index,data):
        """
        If the node to be inserted at index 0 , then make the next of new_node
        to the start node and make the new_node as the start_node
        Assuming we want to anywhere in between other than the root , let's think
        we want to insert at index 3 then we must traverse the LL until index 2 and
        have a temp node pointing to index 2 , so we can insert a node at index 3
        """
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else:
            new_node        = Node(data)
            new_node.ref    = n.ref
            n.ref           = new_node
new_linked_list = LinkedList()
print("Adding elements from the end of the LL")
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.traverse_list()
print("Inserting element at start of LL")
new_linked_list.insert_at_start(20)
new_linked_list.traverse_list()
print("Insert a new element after item 10")
new_linked_list.insert_after_item(10,17)
new_linked_list.traverse_list()
print("Insert a new element before item 17")
new_linked_list.insert_before_item(17,25)
new_linked_list.traverse_list()
print("Insert an element at index 3")
new_linked_list.insert_at_index(3,8)
new_linked_list.traverse_list()
