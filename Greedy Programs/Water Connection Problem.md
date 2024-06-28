### Water Connection Problem

To solve the problem, we need to identify which houses will have tanks and which will have taps based on the given conditions. The solution requires us to identify the connected components of the network of pipes and minimize the diameter of pipes between the tanks and taps.

- **Time Complexity:** \(O(p)\)

- **Space Complexity:** \(O(n+p)\)

Here's the step-by-step solution:

### Steps to Solve the Problem:

1. **Identify the Sources and Sinks:**
   - A house with one outgoing pipe and no incoming pipe is a source (needs a tank).
   - A house with one incoming pipe and no outgoing pipe is a sink (needs a tap).

2. **Track the Pipe Connections:**
   - Use dictionaries to keep track of incoming and outgoing pipes for each house.
   - Use another dictionary to keep track of the minimum diameter of pipes between houses.

3. **Find Connected Components:**
   - Use Depth First Search (DFS) to traverse the connected components starting from each source to find the corresponding sink.
   - While traversing, keep track of the minimum diameter of pipes in the current path.

4. **Output the Results:**
   - For each source, output the source, the corresponding sink, and the minimum diameter of the path.

### Implementation:

Here is the Python code to achieve the solution:

```python
def find_tanks_and_taps(n, p, connections):
    from collections import defaultdict
    
    outgoing = defaultdict(int)
    incoming = defaultdict(int)
    pipes = {}
    
    for a, b, d in connections:
        outgoing[a] = b
        incoming[b] = a
        pipes[(a, b)] = d
    
    sources = set(outgoing.keys()) - set(incoming.keys())
    sinks = set(incoming.keys()) - set(outgoing.keys())
    
    def dfs(house):
        min_diameter = float('inf')
        while house in outgoing:
            next_house = outgoing[house]
            min_diameter = min(min_diameter, pipes[(house, next_house)])
            house = next_house
        return house, min_diameter
    
    results = []
    
    for source in sources:
        sink, min_diameter = dfs(source)
        results.append((source, sink, min_diameter))
    
    results.sort()
    
    t = len(results)
    output = f"{t}\n"
    for result in results:
        output += " ".join(map(str, result)) + "\n"
    
    return output.strip()

# Example Usage:
n = 9  # Number of houses
p = 6  # Number of pipes
connections = [
    (7, 4, 98),
    (5, 9, 72),
    (4, 6, 10),
    (2, 8, 22),
    (9, 7, 17),
    (3, 1, 66)
]

print(find_tanks_and_taps(n, p, connections))
```

### Explanation:

1. **Data Structures:**
   - `outgoing`: Dictionary to store the house that each house is connected to via an outgoing pipe.
   - `incoming`: Dictionary to store the house that is connected to each house via an incoming pipe.
   - `pipes`: Dictionary to store the diameter of the pipe between two houses.

2. **Sources and Sinks:**
   - `sources`: Set of houses that have outgoing pipes but no incoming pipes.
   - `sinks`: Set of houses that have incoming pipes but no outgoing pipes.

3. **DFS to Find Sink and Min Diameter:**
   - Start from each source and use DFS to find the corresponding sink and the minimum diameter of the pipes in the path.

4. **Results:**
   - Collect the results and sort them.
   - Format the output as required.

### Time Complexity:

- **Building the graph**: O(p) where p is the number of pipes.
- **DFS traversal**: O(p) in the worst case if each house has exactly one outgoing pipe.
- **Overall Time Complexity**: O(p) since we process each pipe once.

### Space Complexity:

- **Data Structures**: O(n + p) for dictionaries to store outgoing, incoming, and pipes.
- **Overall Space Complexity**: O(n + p).

This solution efficiently handles the problem by leveraging graph traversal techniques and ensures minimal diameter pipes between tanks and taps.