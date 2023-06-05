import sys

# Time Complexity: O(V^2)
# Space Complexity: O(V)
# Responsibilities of this graph
# 1) Create a adjacency matrix for the graph
# 2) Find the minimum spann
# ing tree for that graph
class Graph():
    def __init__(self,vertices):
        '''
        Initializes number of possible vertices in the graph , 
        Initializes the adjacency list with zero's
        '''
        self.V      = vertices
        self.graph  = [[0 for column in range(vertices)] for row in range(vertices)]
    def printTree(self,parent):
        '''
        Provide the Edge and its corresponding weight details
        '''
        print("Edge \tWeight")
        for i in range(1,self.V):
            print(parent[i],"-",i,"\t",self.graph[i][parent[i]])
    def min_Key(self,key,visitedSet):
        '''
        This is the helper function , where we iterate through all the vertices ,
        and check the minimum of all the unvisited nodes connected through
        edges of weight key[v]
        
        For loop:
        First we chose the minimum value as an arbitary value as the maxint , 
        then iterate through all the vertices , and get an vertice v which is having minimum edge with u ,
        which is unvisited. And update the cost to reach vertex v in the key array. 
        
        Return the minimum edged vertice.
        '''
        min         = sys.maxsize
        for v in range(self.V):
            if key[v] < min and visitedSet[v] == False:
                min         = key[v]
                min_index   = v
        return min_index
    def prim(self):
        '''
        key array contains the details of the cost to reach node
        parent array contains the details of the parent node for respective vertex
        initializing key[0] is 0 , as cost to reach 0 is 0 , as this is the root node , as we assume
        visitedSet array contains the details of visited and unvisited nodes
        We are initializing the parent[0] as -1 , because , we don't have parent of 0
        
        For loop:
        We are iterating through all the vertices , and then, first we will find the unvisited node of minimum costed path
        to reach the vertex, and then we make that unvisited node as visited , then we will check the adjacent edges , and update the 
        key array and parent array , by the ending of this loop , we will get an array's , which have parent node details ,
        cost required to reach node v , and visited status of those nodes
        '''
        key         = [sys.maxsize] * self.V
        parent      = [None] * self.V
        key[0]      = 0
        visitedSet  = [False] * self.V
        
        parent[0]   = -1
        for cout in range(self.V):
            u = self.min_Key(key,visitedSet)
            visitedSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and visitedSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        # print the Edge & Weight details
        self.printTree(parent)

g = Graph(5)
g.graph = [ 
           [0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]
        ]
g.prim()    
        