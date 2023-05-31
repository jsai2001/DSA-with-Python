#Adjacency Matrix representation of an undirected graph
V=4 #number of vertices in the graph

#Function to initialize the matrix with zero
def init(arr):
    for i in range(V):
        for j in range(V):
            arr[i][j]=0
            
#Function to add edges to the graph
def insertEdge(arr,i,j):
    arr[i][j]=1
    arr[j][i]=1
    
#Function to print the matrix elements
def printAdjMatrix(arr):
    for i in range(V):
        print(i,end=' | ')
        for j in range(V):
            print(arr[i][j],end=' ')
        print()

adjMatrix=[[0 for i in range(V)] for j in range(V)]

init(adjMatrix)
insertEdge(adjMatrix,0,1)
insertEdge(adjMatrix,0,2)
insertEdge(adjMatrix,1,2)
insertEdge(adjMatrix,2,0)
insertEdge(adjMatrix,2,3)

printAdjMatrix(adjMatrix)
