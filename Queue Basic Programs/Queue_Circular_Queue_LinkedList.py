'''Declaring a structure for the node'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        '''
        Initializing the Queue with two variables
        1) front
        2) rear
        '''
        self.front = -1
        self.rear = -1
    def enqueue(self,data):
        newnode = Node(data)
        '''
        Checking if Queue is empty or not
        '''
        if(self.rear == -1):
            self.front = self.rear = newnode
            self.rear.next = self.front
        else:
            self.rear.next = newnode
            self.rear = newnode
            self.rear.next = self.front
    def dequeue(self):
        newnode = self.front
        '''
        Checking whether the queue is empty or not
        '''
        if((self.front == -1) and (self.rear==-1)):
            print("\nQueue is empty")
        #Checking whether the single element is left in the queue
        elif(self.front == self.rear):
            self.front = -1
            self.rear = -1
            del newnode
        else:
            self.front = self.front.next
            self.rear.next = self.front
            del newnode
    #Function to get the front of the Queue
    def peek(self):
        if((self.front == -1) and (self.rear==-1)):
            print("\nQueue is empty")
        else:
            print("\nThe front element is ",self.front.data)
    #Function to display all the elements of the queue
    def display(self):
        newnode = self.front
        print("\nThe elements in a Queue are: ")
        if((self.front == -1) and (self.rear == -1)):
            print("Queue is empty")
        else:
            while(newnode.next!=self.front):
                print(newnode.data)
                newnode=newnode.next
            print(newnode.data)

q = Queue()
q.enqueue(34)
q.enqueue(10)
q.enqueue(23)
q.display()
q.dequeue()
q.display()
q.peek()