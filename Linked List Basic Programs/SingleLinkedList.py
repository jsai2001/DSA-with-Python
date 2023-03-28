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
    def get_count(self):
        '''
        Count number of elements in LL
        '''
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count = count + 1
            n = n.ref
        return count
    def search_item(self,x):
        '''
        Search x in LL
        '''
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("Item not found")
        return False
    def make_new_list(self):
        """
        Create a new linked list with n nodes added through the end of LL turn by turn
        """
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Enter the value for node: "))
            self.insert_at_end(value)
    def delete_at_start(self):
        '''
        Delete the first node of the LL
        '''
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node = self.start_node.ref
    def delete_at_end(self):
        '''
        Iterate through the linked list till the last element and then we need 
        to set the reference of the second last element to none , which converts
        second last element to the last element
        '''
        if self.start_node is None:
            print("The list has no element to delete")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
    def delete_element_by_value(self,x):
        '''
        If the start_node is empty , it means that there are no elements in LL
        If the first item is the value that we want to delete , then just shift 
        the start_node , or else iterate it until next element is None , and see 
        next element value is the element that we need to find, if yes stop the 
        iteration , we can skip the next node which have value x and join the 
        current node with the next node of next node , so next node will be out of
        linked list.
        We set reference of the previous node to the node which exists after the node which is being deleted.
        '''
        if self.start_node is None:
            print("The list has no element to delete")
            return
        #Deleting first node
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("Item is not found in the list")
        else:
            n.ref = n.ref.ref
    def reverse_linkedlist(self):
        '''
        Youtube video link (https://youtu.be/XgABnoJLtG4)
        Here actually visualize a scenario , where we are having three nodes
        head pointer points to the first node and to persist the previous node
        address we will be using temp node and to persist the next node address 
        we use temp2 node , so now we stored the addresses of prev and next nodes
        Now , To reverse the link of the linkedlist
        Step 1: Point temp to Null , head to first node , temp2 to the second node (head.ref)
        Step 2: Before reversing the link between node1 & node2 , we must reverse the
        node link for node1 , hypothitically it is just making the next of the first node to null
        Step 3: So , steps will be as follows
        Step 4: traverse the list as long as head is not None
        Step 5: point temp2 to head.ref
        Step 6: head.ref to temp && temp = head && head = temp2
        Step 7: At each iteration , temp2 and head both points to the same node and temp
        points to the previous node , and at last both head and temp2 will be null and
        the loop terminates , but the temp node consists of the last node of the
        earlier linkedlist , it means the present reversed linked list.
        '''
        temp = None
        head = self.start_node
        while head is not None:
            temp2 = head.ref
            head.ref = temp
            temp = head
            head = temp2
        self.start_node = temp
print("***************************************************************")
new_linked_list_1 = LinkedList()
print("Adding elements from the end of the LL")
new_linked_list_1.insert_at_end(5)
new_linked_list_1.insert_at_end(10)
new_linked_list_1.insert_at_end(15)
new_linked_list_1.traverse_list()
print("Inserting element at start of LL")
new_linked_list_1.insert_at_start(20)
new_linked_list_1.traverse_list()
print("Insert a new element after item 10")
new_linked_list_1.insert_after_item(10,17)
new_linked_list_1.traverse_list()
print("Insert a new element before item 17")
new_linked_list_1.insert_before_item(17,25)
new_linked_list_1.traverse_list()
print("Insert an element at index 3")
new_linked_list_1.insert_at_index(3,8)
new_linked_list_1.traverse_list()
print("Total number of variables in LL",new_linked_list_1.get_count())
print("Is 5 present in LL: ",new_linked_list_1.search_item(5))
print("Reverse the linked list: ")
new_linked_list_1.reverse_linkedlist()
new_linked_list_1.traverse_list()
print("**************************************************************")
new_linked_list_2 = LinkedList()
new_linked_list_2.insert_at_end(10)
new_linked_list_2.insert_at_end(20)
new_linked_list_2.insert_at_end(30)
new_linked_list_2.insert_at_end(40)
new_linked_list_2.insert_at_end(50)
print("new_linked_list_2: ")
new_linked_list_2.traverse_list()
new_linked_list_2.delete_at_start()
print("delete_at_start: ")
new_linked_list_2.traverse_list()
new_linked_list_2.delete_at_end()
print("delete_at_end: ")
new_linked_list_2.traverse_list()
new_linked_list_2.delete_element_by_value(30)
print("delete_element_by_value: ")
new_linked_list_2.traverse_list()
print("***************************************************************")

