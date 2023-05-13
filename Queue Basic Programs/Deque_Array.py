class Deque:
    def __init__(self):
        self.size = 5
        self.front = -1
        self.rear = -1
        self.deque = [None] * self.size        
    def insert_front(self,x):
        ''' 
        insert_front function will insert the value from the front
        '''
        if(self.front == 0 and self.rear == self.size-1) or (self.front == self.rear+1):
            print("Overflow")
        elif(self.front == -1) and (self.rear == -1):
            self.front = 0
            self.rear = 0
            self.deque[self.front] = x
        elif(self.front == 0):
            self.front = self.size -1
            self.deque[self.front] = x
        else:
            self.front = self.front - 1
            self.deque[self.front] = x
    def insert_rear(self,x):
        '''
        insert_rear function will insert the value from the rear 
        '''
        if(self.front == 0 and self.rear == self.size-1) or (self.front == self.rear+1):
            print("Overflow")
        elif(self.front == -1 and self.rear == -1):
            self.rear = 0
            self.deque[self.rear]=x
        else:
            self.rear+=1
            self.deque[self.rear]=x
    def display(self):
        '''
        display function prints all the value of deque.    
        '''
        iterator = self.front
        print("\nElements in a deque are: ")
        while(iterator!=self.rear):
            print(self.deque[iterator],end=" ")
            iterator=(iterator+1)%self.size
        print(self.deque[self.rear])
    def getfront(self):
        '''
        getfront function retrieves the first value of the deque.   
        '''
        if((self.front == -1) and (self.rear == -1)):
            print("Deque is empty")
        else:
            print("The value of the element at front is: ",self.deque[self.front])
    def getrear(self):
        '''
        getrear function retrieves the last value of the deque.  
        '''
        if(self.front==-1 and self.rear==-1):
            print("Deque is empty")
        else:
            print("The value of the element at rear is ",self.deque[self.rear])
    def delete_front(self):
        '''
        delete_front() function deletes the element from the front 
        '''
        if(self.front == -1 and self.rear == -1):
            print("Deque is empty")
        elif(self.front == self.rear):
            print("The deleted element is ",self.deque[self.front])
            self.front = -1
            self.rear = -1
        elif(self.front == (self.size - 1)):
            print("The deleted element is ",self.deque[self.front])
            self.front = 0
        else:
            print("The deleted element is ",self.deque[self.front])
            self.front = self.front + 1
    def delete_rear(self):
        '''
        delete_rear() function deletes the element from the rear
        '''
        if(self.front == -1 and self.rear == -1) :
            print("Deque is empty")
        elif(self.front == self.rear):
            print("The deleted element is ",self.deque[self.rear])
            self.front = -1
            self.rear = -1
        elif(self.rear == 0):
            print("The deleted element is ",self.deque[self.rear])
            self.rear = self.size - 1
        else:
            print("The deleted element is ",self.deque[self.rear])
            self.rear = self.rear - 1

DQ = Deque()
DQ.insert_front(20)
DQ.insert_front(10)
DQ.insert_rear(30)
DQ.insert_rear(50)
DQ.insert_rear(80)
DQ.display() # Calling the display function to retrieve the values of deque

DQ.getfront();  # Retrieve the value at front-end  
DQ.getrear();  # Retrieve the value at rear-end   
DQ.delete_front();    
DQ.delete_rear();    
DQ.display(); # calling display function to retrieve values after deletion   