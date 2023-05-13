class PriorityQueue:
    def __init__(self):
        self.heap = [None for i in range(40)]
        self.size=-1
    
    #retrieving the parent node of the child node
    def parent(self,i):
        return (i-1)//2
    
    #retrieving the left child of the parent node
    def left_child(self,i):
        return i+1
    
    #retrieving the right child of the parent 
    def right_child(self,i):
        return i+2
    
    #Returning the element having the highest priority  
    def get_Max(self):
        return self.heap[0]
    
    #Returning the element having the minimum priority  
    def get_Min(self):
        return self.heap[self.size]
    
    #function to move the node up the tree in order to restore the heap property.
    def moveUp(self,i):
        while(i>0):
            #swapping parent node with a child node
            if(self.heap[self.parent(i)]<self.heap[i]):
                self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
            #updating the value of i to i/2
            i=i//2
    
    #function to move the node down the tree in order to restore the heap property
    def moveDown(self,k):
        index = k
        #getting the location of the Left Child
        left = self.left_child(k)
        if(left<=self.size and self.heap[left]>self.heap[index]):
            index = left
        #getting the location of the Right Child
        right = self.right_child(k)
        if(right<=self.size and self.heap[right]>self.heap[index]):
            index = right
        #If k is not equal to index
        if(k!=index):
            self.heap[index],self.heap[k]=self.heap[k],self.heap[index]
            self.moveDown(index)
    
    #Removing the element of maximum priority
    def removeMax(self):
        removed = self.heap[0]
        self.heap[0] = self.heap[self.size]
        self.size=self.size-1
        # print("Max element of the heap which is removed: ",removed)
        self.moveDown(0)
    
    #inserting the element in a priority queue
    def insert(self,p):
        self.size=self.size+1
        self.heap[self.size]=p
        #move Up to maintain heap property   
        self.moveUp(self.size)
    
    #Removing the element from the priority queue at a given index i.  
    def delete(self,i):
        #This denotes the replacing the node that we want with (max_element of the heap + 1) , 
        # so , it will be replaced as the new root node , so we can remove this node , 
        # very easy from the heap
        #Replace the node that we want to remove with (value of the max node of max_heap + 1)
        self.heap[i]=self.heap[0]+1
        #move the node stored at ith location (that we want to remove) is shifted to the root node,
        # which helps us to remove the ith location node
        self.moveUp(i)
        # Removing the node having maximum priority 
        # (the ith location node , which is shifted as the new root node , is removed)
        self.removeMax()

pq=PriorityQueue()
pq.insert(20)
pq.insert(19)
pq.insert(21)
pq.insert(18)
pq.insert(12)
pq.insert(17)
pq.insert(15)
pq.insert(16)
pq.insert(14)

print("Elements in a priority queue are: ")
for i in range(pq.size+1):
    if(pq.heap[i]!=None):
        print(pq.heap[i],end=' ')
print()

#deleting the element whose index is 2
pq.delete(2)

print("Elements in a priority queue after deleting the element are : ")
for i in range(pq.size+1):
    if(pq.heap[i]!=None):
        print(pq.heap[i],end=' ')
print()

max = pq.get_Max()
print("The element which is having the highest priority is ",max)

min = pq.get_Min()
print("The element which is having the minimum priority is : ",min)