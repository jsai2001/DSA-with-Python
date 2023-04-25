class Node:
    def __init__(self,data=None):
        '''
        Initially, upon creation of a node, 
        it will point to itself in both directions to form a doubly circular linked list 
        with only one item.
        '''
        self.data = data
        self.previous = self
        self.next = self
class DCLL:
    def __init__(self):
        '''
        Initially, upon creation of a node, 
        it will point to itself in both directions to form a doubly circular linked list with only one item.
        '''
        self.head = None
        self.count = 0
    def __repr__(self):
        '''
        The __repr__ method will return a string that will 
        print the contents of the list appropriately on the screen.
        '''
        string = ""
        if(self.head == None):
            string += "Doubly Circular Linked List Empty"
            return string
        string += f"Doubly Circular Linked List:\n{self.head.data}"
        temp = self.head.next
        while(temp!=self.head):
            string+=f" -> {temp.data}"
            temp = temp.next
        return string
    def append(self,data):
        '''
        We can either append or insert nodes in the list. 
        The append method is created just for convenience as it calls the insert method and sends the appropriate values.
        '''
        self.insert(data,self.count)
        return
    def insert(self,data,index):
        '''
        In the insert method, we first check if the index is in range or not, 
        and if not, we raise a ValueError. Then, if the list is empty, 
        then we simply assign a new node to the head and make the count equal to 1. 
        Now we reach the node just before the index where the new node is to be inserted.

        At this point, we make the previous of the node at the specified index equal to the new node. 
        Then we make the new node’s next and previous equal to the node at the specified index 
        and the node before the specified index respectively. 
        And now we make the next of the node before the specified index equal to the new node. 
        Finally, if the specified index was 0, then we make the head point to the node just before where it was pointing.
        '''
        if(index>self.count)|(index<0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
        if self.head == None:
            self.head = Node(data)
            self.count = 1
            return
        temp = self.head
        if(index == 0):
            temp = temp.previous
        else:
            for _ in range(index-1):
                temp = temp.next
        temp.next.previous = Node(data)
        temp.next.previous.next , temp.next.previous.previous = temp.next , temp
        temp.next = temp.next.previous
        if(index == 0):
            self.head = self.head.previous
        self.count += 1
        return
    def remove(self,index):
        '''
        In this method too we first check if the index is out of range and throw a ValueError if it is. 
        Then if there is one node only, we simply make the head as None and make the count as 0 and return.

        If not, we reach the required node to be deleted, 
        and if the target node is the head, we make the head point to the node after it so that we don’t lose the list.

        Finally, we make the next of the node before the specified index point to the node after the specified index, 
        and we make the previous of the node after the specified index point to the node before the specified index. 
        This will make the node at the specified index unreachable from the list (basically skipped), 
        and we decrement the count to finish the method
        '''
        if(index>=self.count)|(index<0):
            raise ValueError(f"Index out of range: {index}, size:{self.count}")
        if self.count == 1:
            self.head = None
            self.count = 0
            return
        target = self.head
        for _ in range(index):
            target = target.next
        if target is self.head:
            self.head = self.head.next
        target.previous.next , target.next.previous = target.next , target.previous
        self.count-=1
    def index(self,data):
        '''
        The index method searches linearly through the list and returns the index if the item is found, 
        None otherwise.
        '''
        temp = self.head
        for i in range(self.count):
            if(temp.data==data):
                return i
            temp = temp.next
        return None
    def get(self,index):
        '''
        The get method returns the item at the specified index, 
        and raises a ValueError if the index is out of range
        '''
        if(index>=self.count)|(index<0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.data
    def size(self):
        '''
        The size method returns the number of items in the list.
        '''
        return self.count
    def display(self):
        '''
        The display method prints the list.
        '''
        print(self)

nums = DCLL()
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
print("Item at 4:",nums.get(4))
print("Size of list: ",nums.size())

nums.display()