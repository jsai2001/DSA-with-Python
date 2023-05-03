#Enqueue and Dequeue both have O(1) timecomplexity
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.queueSize = 0
    def enQueue(self,data):
        temp = Node(data)
        if self.front is None:
            self.front = temp
            self.queueSize = self.queueSize+1
        else:
            curr = self.front
            while curr.next != None:
                curr = curr.next
            curr.next = temp
            self.queueSize = self.queueSize+1
    def deQueue(self):
        try:
            if self.front == None:
                raise Exception("Queue is Empty")
            else:
                temp = self.front
                self.front = self.front.next
                tempdata = temp.data
                self.queueSize = self.queueSize-1
                del temp
                return tempdata
        except Exception as e:
            print(str(e))
    def isEmpty(self):
        if self.queueSize == 0:
            return True
        else:
            return False
    def size(self):
        return self.queueSize
    def front_element(self):
        try:
            if self.front == None:
                raise Exception("Queue is Empty")
            else:
                return self.front.data
        except Exception as e:
            print(str(e))
    def queueDisplay(self):
        try:
            if self.front == None:
                raise Exception("Queue is Empty")
            else:
                temp = self.front
                while temp!=None:
                    print(temp.data,"->",end="")
                    temp = temp.next
                print()
        except Exception as e:
            print(str(e))
        
            
q = Queue()
#Print queue elements
q.queueDisplay()
#Insert elements in the queue
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
q.enQueue(50)
#Print queue elements
q.queueDisplay()
#Insert element in queue
q.enQueue(60)
#Print queue elements
q.queueDisplay()

q.deQueue()
q.deQueue()
print("\n\nafter two node deletion\n")

# Print queue elements
q.queueDisplay()

# Print front of queue
q.front_element()

'''
#Create a new queue of capacity 4
    q = Queue(4)
    #Print queue elements
    q.queueDisplay()
    #Insert elements in the queue
    q.queueEnqueue(20)
    q.queueEnqueue(30)
    q.queueEnqueue(40)
    q.queueEnqueue(50)
    #Print queue elements
    q.queueDisplay()
    #Insert element in queue
    q.queueEnqueue(60)
    #Print queue elements
    q.queueDisplay()
    
    q.queueDequeue()
    q.queueDequeue()
    print("\n\nafter two node deletion\n")
 
    # Print queue elements
    q.queueDisplay()
 
    # Print front of queue
    q.queueFront()
'''