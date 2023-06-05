'''
Time Complexity:
The time complexity of the above code/algorithm looks O(V^2) as there are two nested while loops. 
If we take a closer look, we can observe that the statements in inner loop are executed O(V+E) times (similar to BFS). 
The inner loop has decreaseKey() operation which takes O(LogV) time. 
So overall time complexity is O(E+V)*O(LogV) which is O((E+V)*LogV) = O(ELogV) (For a connected graph, V = O(E))

Space Complexity:
The space complexity of the above code/algorithm is O(V + E) because we need to store the adjacency list representation 
of the graph, the heap data structure, and the MST.
'''

# Prim's MST using adjacency list of graph
from collections import defaultdict
import sys

class Heap():
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []
    def newMinHeapNode(self,v,dist):
        minHeapNode = [v,dist]
        return minHeapNode
    # utility function to swap two nodes of min heap
    # needed for min heapify
    def swapMinHeapNode(self,a,b):
        self.array[a],self.array[b]=self.array[b],self.array[a]
    # Function used to heapify at given index 
    # This function also updates position of nodes
    # when they are swapped. Position is needed
    # for decreaseKey()
    def minHeapify(self,idx):
        smallest = idx
        left = 2*idx+1
        right = 2*idx+2
        if left<self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left
        if right<self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right
        # The nodes to be swapped in min heap
        # if idx is not smallest
        if smallest != idx:
            # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest
            # Swap nodes
            self.swapMinHeapNode(smallest, idx)
            self.minHeapify(smallest)
    # Standard function to extract minimum node from heap
    # we are swapping the minimum node from the heap which is first node with the last node
    # and then we are decreasing size by 1 to neglect the first node , which we shifted to 
    # the last , and then heapify the array again , basing on the root.
    def extractMin(self):
        # Return NULL if heap is empty
        if self.isEmpty() == True:
            return
        # Store the root node
        root = self.array[0]
        # Replace the root node with the last node
        lastNode = self.array[self.size-1]
        self.array[0] = lastNode
        # Update position of the last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)
        return root
        
    def isEmpty(self):
        return True if self.size == 0 else False
    # Main moto of this function is , we are updating the weight of the graph , 
    # so that , we create a minimum spanning tree in the full graph , as MST is a
    # subpart of the Complete graph's
    # In general the weight of the node is updated , the weight of the node denotes ,
    # the cost it takes to reach that particular node.
    def decreaseKey(self,v,dist):
        # Updating the distance
        # Get the index of v in  heap array 
        i = self.pos[v] 
        # Get the node and update its dist value
        self.array[i][1] = dist
        '''
        In while loop , we are checking whether current node is lesser than that of it's children , 
        If not we need to swap them , because being lesser than all it's child nodes is a property
        of minheap.
        '''
        # Travel up while the complete tree is not
        # heapified. This is a O(Logn) loop
        while i > 0 and self.array[i][1] < \
                self.array[(i - 1) // 2][1]: 
            # Swap this node with its parent
            self.pos[self.array[i][0]] = (i-1)/2
            self.pos[self.array[(i-1)//2][0]] = i
            self.swapMinHeapNode(i, (i - 1)//2) 
            # move to parent index
            i = (i - 1) // 2
    # A utility function to check if a given vertex 'v' is in min heap or not
    def isInMinHeap(self,v):
        if self.pos[v] < self.size:
            return True
        return False
    
def printArr(parent, n):
    for i in range(1,n):
        print("%d - %d"%(parent[i],i))

class Graph():
    def __init__(self,V):
        self.V = V
        self.graph = defaultdict(list)
    # Adds an edge to an undirected graph
    def addEdge(self,src,dest,weight):
        # Add an edge from src to dest.  A new node is
        # added to the adjacency list of src. The node
        # is added at the beginning. The first element of
        # the node has the destination and the second
        # elements has the weight
        newNode = [dest, weight]
        self.graph[src].insert(0,newNode)
        # Since graph is undirected, add an edge from
        # dest to src also
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)
    # The main function that prints the Minimum
    # Spanning Tree(MST) using the Prim's Algorithm.
    # It is a O(ELogV) function
    def PrimMST(self):
        # Get the number of vertices in a graph
        V = self.V
        # key values are used to pick minimum weight edge
        key = []
        # List to store the constructed MST
        parent = []
        # minHeap represents set E
        minHeap = Heap()
        # Initialize min heap with all vertices , key alues of all vertices (except the 0th vertex) is initially infinite
        for v in range(V):
            parent.append(-1)
            key.append(1e7)
            minHeap.array.append(minHeap.newMinHeapNode(v,key[v]))
            minHeap.pos.append(v)
        # Make key value of 0th vertex as 0 , so that it is extracted first
        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0])

        # Initially size of min heap is equal to V
        minHeap.size = V

        # In the following loop , min heap contains all nodes not yet added in the MST
        while minHeap.isEmpty() == False:
            # Extract the vertex with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]
            # Traverse through all adjacent vertices of u
            # (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph[u]:
                v = pCrawl[0]
                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less than
                # its previously calculated distance
                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]:
                    key[v] = pCrawl[1]
                    parent[v] = u
                    # update distance value in min heap also
                    minHeap.decreaseKey(v, key[v])
        printArr(parent, V)
    
# Driver program to test the above functions
graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.PrimMST()
    
        