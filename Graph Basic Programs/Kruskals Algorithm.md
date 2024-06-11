### Kruskal’s Minimum Spanning Tree (MST) Algorithm

Kruskal's algorithm is a popular method for finding the minimum spanning tree (MST) of a connected, undirected graph. The MST of a graph is a subset of the edges that connects all vertices together, without any cycles, and with the minimum possible total edge weight.

- **Time Complexity:** \( O(E log V) \)
- **Space Complexity:** \( O(E + V) \)

### Steps of Kruskal’s Algorithm

1. **Sort all the edges in non-decreasing order of their weight.**
2. **Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If a cycle is not formed, include this edge. Else, discard it.**
3. **Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices.**

### Detailed Explanation

#### Step-by-Step Execution

1. **Sorting the edges:**
   - Sort all edges in the graph in ascending order based on their weight.

2. **Initializing the Disjoint Set (Union-Find):**
   - Create a disjoint-set data structure to manage the connected components of the graph. This structure helps in determining whether two vertices belong to the same component or different components efficiently.
   - Each vertex is initially in its own set.

3. **Processing each edge:**
   - Iterate through the sorted list of edges, and for each edge (u, v):
     - Use the union-find data structure to check if the vertices u and v belong to different sets.
     - If they do, include this edge in the MST and merge the sets containing u and v.
     - If they belong to the same set, discard the edge to avoid forming a cycle.

4. **Termination:**
   - The algorithm stops when we have included (V-1) edges in the MST.

### Pseudocode

```python
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, src, dest, weight):
        self.edges.append(Edge(src, dest, weight))

def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal_mst(graph):
    result = []
    i, e = 0, 0

    graph.edges = sorted(graph.edges, key=lambda edge: edge.weight)

    parent = []
    rank = []

    for node in range(graph.V):
        parent.append(node)
        rank.append(0)

    while e < graph.V - 1:
        edge = graph.edges[i]
        i = i + 1
        x = find(parent, edge.src)
        y = find(parent, edge.dest)

        if x != y:
            e = e + 1
            result.append(edge)
            union(parent, rank, x, y)
    
    for edge in result:
        print(f"Edge {edge.src} -- {edge.dest} == {edge.weight}")

# Example Usage
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

kruskal_mst(g)
```

### Time and Space Complexity

- **Time Complexity:**
  - Sorting the edges: \( O(E log E) \), where \( E \) is the number of edges.
  - Union-Find operations: The union and find operations take \( O(log V) \) time on average when using path compression and union by rank. Since each edge is processed once, this results in a complexity of \( O(E log V) \).

  Overall time complexity: \( O(E log E + E log V) \). Since \( log E \) is at most \( log V^2 \) (which is \( 2 log V \)), the overall time complexity can be simplified to \( O(E log V) \).

- **Space Complexity:**
  - The space complexity is dominated by the storage for the edges, parent, and rank arrays.
  - Space for storing edges: \( O(E) \).
  - Space for the parent and rank arrays: \( O(V) \).

  Overall space complexity: \( O(E + V) \).

### Conclusion

Kruskal’s algorithm is efficient and straightforward for finding the minimum spanning tree of a graph, especially when the graph is sparse (i.e., when the number of edges \( E \) is much less than \( V^2 \)). The algorithm uses the greedy approach and the union-find data structure to efficiently manage the components and ensure the resulting MST is minimal.

In the context of Kruskal's algorithm and the union-find data structure, the `rank` array is used to keep track of the "rank" of each node, which helps to optimize the union operation.

### Rank Array in Union-Find

The `rank` of a node is essentially a heuristic that represents an upper bound on the height of the node's subtree in the union-find structure. By always attaching the smaller tree under the root of the larger tree (union by rank), we can keep the overall tree flat, thus speeding up the find operations.

### Rank Comparisons in Union-Find

When performing the union operation, we compare the ranks of the roots of the trees containing the elements to be unioned. The tree with the smaller rank is made a subtree of the tree with the larger rank. If the ranks are the same, one tree becomes a subtree of the other and the rank of the new root is incremented by one.

### Detailed Explanation with Code

#### Find Function with Path Compression

The `find` function is used to find the root of the set containing a particular element. It uses path compression to make the tree flatter, which speeds up future operations.

```python
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]
```

#### Union Function with Union by Rank

The `union` function combines two sets. It uses the rank to decide which tree to attach to which.

```python
def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1
```

### Explanation of Union by Rank

- **Case 1:** `rank[root_x] < rank[root_y]`
  - Attach the tree with root `root_x` to the tree with root `root_y`. This is because the tree with root `root_x` has a smaller rank and hence, presumably, a smaller height.

- **Case 2:** `rank[root_x] > rank[root_y]`
  - Attach the tree with root `root_y` to the tree with root `root_x`. This is because the tree with root `root_y` has a smaller rank and hence, presumably, a smaller height.

- **Case 3:** `rank[root_x] == rank[root_y]`
  - Both trees have the same rank, so we arbitrarily choose one to attach to the other (in this case, `root_y` to `root_x`). Then, we increment the rank of the new root (`root_x`) by one since the height of the tree increases by one.