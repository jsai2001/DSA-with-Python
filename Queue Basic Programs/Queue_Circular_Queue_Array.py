'''
Complexity of the enqueue and dequeue operations of a 
circular queue is O(1) for array implementations.
'''

#Circular Queue implementation in Python
class CircularQueue():
    def __init__(self,max_size):
        self.max_size = max_size
        self.queue = [None]*max_size
        self.head = self.tail = -1
    #Insert an element into the circular queue
    def enqueue(self,data):
        if((self.tail+1)%self.max_size == self.head):
            print("The Circular Queue is full\n")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail+1)%self.max_size
            self.queue[self.tail] = data
    #Delete an element from the circular queue
    def dequeue(self):
        if(self.head == -1):
            print("The Circular Queue is empty\n")
        elif(self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1)%self.max_size
            return temp
    #Print elements of Queue
    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")
        elif(self.tail >= self.head):
            for i in range(self.head,self.tail+1):
                print(self.queue[i],end=' ')
            print()
        else:
            for i in range(self.head , self.max_size):
                print(self.queue[i], end=" ")
            for i in range(0,self.tail+1):
                print(self.queue[i],end=" ")
            print()

#CircularQueue will be instantiated and stored into the object
obj = CircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial Queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()
        