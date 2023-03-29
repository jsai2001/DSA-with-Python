class Node:
    def __init__(self,data):
        self.item = data
        self.nref = None
        self.pref = None
class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
    def insert_in_emptylist(self,data):
        '''
        Inserting an element into empty list
        '''
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("List is not empty")
    def insert_at_start(self,data):
        '''
        Inserting an element to the start of the list
        '''
        if self.start_node is None:
            self.insert_in_emptylist(data)
            print("Node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node
    def insert_at_end(self,data):
        '''
        Insert an element at the end of LL
        '''
        if self.start_node is None:
            self.insert_in_emptylist(data)
            print("Node inserted")
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n
    def insert_after_item(self,x,data):
        '''
        Insert an item after particular element occurance
        '''
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("Item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node
    def insert_before_item(self,x,data):
        '''
        Insert new_node before a node with specific value
        '''
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("Item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.start_node = new_node
                n.pref = new_node
    def traverse_list(self):
        '''
        Traverse the LL
        '''
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item,end=" ")
                n = n.nref
        print()
    def delete_at_start(self):
        '''
        Delete the first node of the LL
        '''
        if self.start_node is None:
            print("The list has no elements to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_node.pref = None
    def delete_at_end(self):
        '''
        Delete at the end of the LL
        '''
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None
    def delete_element_by_value(self,x):
        '''
        Delete element by value
        Case 1: If the list is empty
        Case 2: If there is only one node in the LL
        Case 3: The first element is the one we want to delete
        Case 4: The value is in between the first element and the last
        Case 5: The value is present on last element
        '''
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
            return
        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return
        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")
    def reverse_linked_list(self):
        '''
        Reverse the Double LL
        '''
        if self.start_node is None:
            print("The list has no element to delete")
            return
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p
print("******************************************************")
new_linked_list = DoublyLinkedList()
new_linked_list.insert_in_emptylist(3)
new_linked_list.insert_before_item(3,2)
new_linked_list.insert_after_item(3,4)
new_linked_list.insert_before_item(4,9)
new_linked_list.insert_at_start(1)
new_linked_list.insert_at_end(5)
new_linked_list.insert_before_item(5,10)
new_linked_list.insert_before_item(1,0)
new_linked_list.insert_after_item(5,11)
new_linked_list.traverse_list()
print("******************************************************")
new_linked_list_1 = DoublyLinkedList()
new_linked_list_1.insert_at_start(5)
new_linked_list_1.insert_at_start(4)
new_linked_list_1.insert_at_start(3)
new_linked_list_1.insert_at_start(2)
new_linked_list_1.insert_at_start(1)
print("Original Linked List: ")
new_linked_list_1.traverse_list()
print("Reverse Linked List: ")
new_linked_list_1.reverse_linked_list()
new_linked_list_1.traverse_list()
print("Delete at start: ")
new_linked_list_1.delete_at_start()
new_linked_list_1.traverse_list()
print("Delete at end: ")
new_linked_list_1.delete_at_end()
new_linked_list_1.traverse_list()
print("Delete by value: 3 ")
new_linked_list_1.delete_element_by_value(3)
new_linked_list_1.traverse_list()
print("*******************************************************")
