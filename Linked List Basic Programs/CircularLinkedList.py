class Node:
    def __init__(self,data=None):
        '''
        Every node can have a value , or may not have
        But by default , the next of current node will the node itself
        If we didn't declare one
        '''
        self.data = data
        self.next = self
class CLL:
    def __init__(self):
        '''
        In the constructor, we are initializing two members, we are setting the head as None 
        because there are no nodes in the list, and we are setting the count as 0 
        for the same reason.
        '''
        self.head = None
        self.count = 0
        
    def __repr__(self):
        '''
        The string that will print the linked list will be returned by the __repr__ process. 
        So either the list is empty, in which case we print that, or the list isn’t empty,
        in which case we print each node’s data one by one.
        '''
        string = ""
        if(self.head == None):
            string += "Circular Linked List Empty"
            return string
        string += f"Circular Linked List:\n{self.head.data}"
        temp = self.head.next
        while(temp != self.head):
            string += f" -> {temp.data}"
            temp = temp.next
        return string
    
    def append(self,data):
        '''
        Nodes can either be appended or inserted at a specified position in this implementation.
        To append, we simply call the insert method and send the size of the list as the index.
        '''
        self.insert(data,self.count)
        return
    
    def insert(self,data,index):
        '''
        In the insert method, we first check if the specified index is valid or not, 
        if not, we throw a ValueError. After passing the check, if the list is empty, 
        we simply assign the new node to the head, increment the count, and return from the method.

        If the list isn’t empty, we first reach the node before the specified index. 
        For example, if the given index is 5, then we reach the node at the 4th index, 
        and because the list is circular, if the given index is 0, 
        then we reach the last node of the list.

        Now, we assign the new node to the next of the node before the specified index, 
        and we make the new node’s next link to the node at the specified index. 
        This will make sure that the new node is inserted before the node that was at the specified index, 
        and hence taken its index and pushed it ahead.

        Now, if the given index was 0, we have inserted a node after the last node of the list, 
        so we simply make the head point to the new node making it the new head of the list.
        '''
        if (index>self.count) | (index<0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
        if self.head == None:
            self.head = Node(data)
            self.count+=1
            return
        temp = self.head
        '''
        The for loop below , is to get to the one node before the index 
        to insert into the LinkedList
        If we need to insert into the first node then before index is self.count-1
        Else it will be index-1
        '''
        for _ in range(self.count-1 if index-1==-1 else index-1):
            temp = temp.next
        aftertemp = temp.next
        #New node goes between temp and aftertemp
        temp.next = Node(data)
        temp.next.next = aftertemp
        if( index == 0 ):
            self.head = temp.next
        self.count += 1
        return
    
    def remove(self,index):
        '''
        To remove an item we must specify where the item is to be removed from. 
        If the specified index is out of range, we raise a ValueError. 
        If there’s only one item on the list, we simply make the head None and the count 0, 
        and return from the method.

        Otherwise, we have to reach the node before the specified index and the node after the specified index.
        For example, if the specified index is 4 then we need to reach the 3rd node and the 5th node, 
        and because the list is circular if the specified index is 0, 
        we need to reach the last node (before it) and the 1st node (after it).

        After this, we simply assign the node after the specified index to the next of the node before the specified index. 
        This will skip the node at the specified index, hence removing it from the list. 
        If the specified index is 0, then the head has been removed from the list, 
        so we simply have to assign the node that was after the specified index to the head and the list will be restored. 
        Don’t forget to decrement the count of the list.
        '''
        if (index>=self.count) | (index<0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
        if self.count == 1:
            self.head = None
            self.count = 0
            return
        
        before = self.head
        for _ in range(self.count-1 if index-1==-1 else index-1):
            before = before.next
        after = before.next.next
        
        before.next = after
        if(index == 0):
            self.head = after
        self.count-=1
        return
    
    def index(self,data):
        '''
        The index method searches for an item in the list. 
        If found, it returns its index, otherwise, it returns None.
        '''
        temp = self.head
        for i in range(self.count):
            if(temp.data==data):
                return i
            temp = temp.next
        return None
    def size(self):
        '''
        The size method returns the number of nodes in the list
        '''
        return self.count
    def display(self):
        '''
        display method prints the list.
        '''
        print(self)
        
nums = CLL()
print(nums)

nums.append(1)
nums.append(2)
nums.append(3)
nums.append(4)
nums.append(5)
#We overrided the print function using the __repr__ constructor
print(nums)

nums.insert('Zero',0)
print(nums)

nums.insert('Two.Five',3)
print(nums)

nums.insert('Six',7)
print(nums)

nums.remove(3)
print(nums)

nums.remove(0)
print(nums)

nums.remove(5)
print(nums)

print("Index of 3: ",nums.index(3))
print("Size of list: ",nums.size())

nums.display()


    