from queue import Queue

class Graph:
    # Constructor
    def __init__(self,num_of_nodes,directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)
        # Directed or Undirected
        self.m_directed = directed
        # Graph representation - Adjacency List
        # We use a dictionary to implement an adjacency list
        self.m_adj_list = {node: set() for node in self.m_nodes}
    # Add edge to the graph
    def add_edge(self,node1,node2,weight=1):
        self.m_adj_list[node1].add((node2,weight))
        if not self.m_directed:
            self.m_adj_list[node2].add((node1,weight))
    # Print the graph representation
    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node",key,": ",self.m_adj_list[key])
    def bfs(self,start_node,target_node):
        # Set of visited nodes to prevent loops
        visited = set()
        queue = Queue()
        # Add the start_node to the queue and visited list
        queue.put(start_node)
        visited.add(start_node)
        # start_node has no parents
        parent = dict()
        parent[start_node] = None
        # Perform step 3
        path_found = False
        while not queue.empty():
            current_node = queue.get()
            if current_node == target_node:
                path_found = True
                break
            for (next_node,weight) in self.m_adj_list[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    parent[next_node] = current_node
                    visited.add(next_node)
        # Path reconstruction
        # If the path is found , To reconstruct the path , we are tracing back from the target node to the source node
        path = []
        if path_found:
            path.append(target_node)
            while parent[target_node] is not None:
                path.append(parent[target_node])
                target_node = parent[target_node]
            path.reverse()
        return path
    def bfs_traversal(self,start_node):
        visited = set()
        queue = Queue()
        queue.put(start_node)
        visited.add(start_node)        
        while not queue.empty():
            current_node = queue.get()
            print(current_node,end=' ')
            for (next_node,weight) in self.m_adj_list[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    visited.add(next_node)

graph = Graph(6,directed=False)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 5)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 5)

graph.print_adj_list()

# node 0 :  {(3, 1), (1, 1), (4, 1), (2, 1)}
# node 1 :  {(0, 1), (2, 1)}
# node 2 :  {(0, 1), (1, 1), (5, 1), (3, 1)}
# node 3 :  {(0, 1), (5, 1), (4, 1), (2, 1)}
# node 4 :  {(0, 1), (5, 1), (3, 1)}
# node 5 :  {(3, 1), (4, 1), (2, 1)}

path = []
path = graph.bfs(0, 5)
print(path)

# [0, 3, 5]

# Disconnected graphs: There are atleast two nodes that are not connected by a path

# This graph is undirected and has 5 nodes
graph = Graph(5,directed=False)

# Add edges to the graph
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(2, 3)

graph.bfs_traversal(0)

# Time complexity of the BFS algorithm is O(|V| + |E|), 
# where V is a set of the graph's nodes, 
# and E is a set consisting of all of its branches (edges).


