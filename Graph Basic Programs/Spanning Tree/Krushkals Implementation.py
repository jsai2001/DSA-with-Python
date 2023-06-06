# Krushkal's algorithm in Python
'''
Time Complexity: O(E * logE) or O(E * logV) 

Sorting of edges takes O(E * logE) time. 
After sorting, we iterate through all edges and apply the find-union algorithm. 
The find and union operations can take at most O(logV) time.
So overall complexity is O(E * logE + E * logV) time. 
The value of E can be at most O(V2), so O(logV) and O(logE) are the same. 
Therefore, the overall time complexity is O(E * logE) or O(E*logV)

Auxiliary Space: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
'''
class Graph:
    def __init__(self,vertices):
        '''
        Initialize the graph , with V vertices , 
        and initialize an array to have adjacency list
        '''
        self.V = vertices
        self.graph = []
    def add_edge(self,u,v,w):
        '''
        Add an edge from u to v with weight w
        '''
        self.graph.append([u,v,w])
    # search function
    def find(self,parent,i):
        '''
        The following condition is checking the 
        abosolute parent of the current node is the last node ,
        it means that it is the end of the tree
        '''
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])
    def apply_union(self,parent,rank,x,y):
        '''
        This is the union function , where get the absolute parent of both x and y nodes , 
        and compare the ranks of them , comparing them is noting but comparing the clusters ,
        so , if we want to compare two nodes , where we have to form a link between them , we 
        will create a link from the node which has lesser rank to the node which have higher rank
        '''
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    # Applying krushkal's algorithm
    def krushkal_algo(self):
        result = []
        i,e = 0,0
        '''
        Sorting the adjacency list based on the weights on the edges
        '''
        self.graph = sorted(self.graph,key=lambda item: item[2])
        parent = []
        rank = []
        '''
        Accumulating the parent node with the current node value
        So , remember if the value of the parent node is the current node's value , 
        then we say that this is the last node of a cluster of tree.
        
        Initializing the rank of every node to 0 , rank is defined as number of nodes
        pointing to the current node , if two nodes are pointing towards current node,
        then we say the rank of the current node is two.
        '''
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e<self.V-1:
            u,v,w = self.graph[i]
            i = i+1
            x = self.find(parent,u)
            y = self.find(parent,v)
            '''
            Here , we are denoting the x!=y mean , we are preventing of creating a loop ,
            as loops shouldn't be there for a spanning tree.
            
            If there are two nodes , and their absolute parent nodes are same , it means that
            those two nodes have path someway connected , so , if we create another path between
            these two nodes , then there is a chance of creating a loop in the tree , so we only add
            an edge only if when x!=y
            '''
            if x != y:
                e = e+1
                result.append([u,v,w])
                self.apply_union(parent,rank,x,y)
        for u,v,weight in result:
            print("%d - %d: %d"%(u,v,weight))

g = Graph(6)

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)

g.krushkal_algo()
# https://youtu.be/Ub-fJ-KoBQM visit this link for algorithm explanation