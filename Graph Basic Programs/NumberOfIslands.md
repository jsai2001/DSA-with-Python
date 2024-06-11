### Number Of Islands

To solve the problem of finding the number of islands in a grid, we can use either Depth-First Search (DFS) or Breadth-First Search (BFS). An island is defined as a group of connected '1's (land) surrounded by '0's (water). We will use DFS for this explanation.

- **Time Complexity:** \(O(M x N)\)
- **Space Complexity:** \(O(M x N)\)

### Problem Explanation

Given a 2D grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

### Steps to Solve

1. **Initialize a counter** to count the number of islands.
2. **Iterate through each cell** in the grid.
3. When a '1' (land) is encountered, increment the island counter and perform a DFS to mark all connected '1's as visited.
4. Continue until all cells are visited.
5. The final value of the island counter is the number of islands.

### Detailed Explanation with Code

Here's the Python code implementing the DFS approach:

```python
def num_islands(grid):
    if not grid:
        return 0

    def dfs(grid, r, c):
        rows, cols = len(grid), len(grid[0])
        # Base case for recursion
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        # Mark the cell as visited by setting it to '0'
        grid[r][c] = '0'
        # Perform DFS in all four possible directions
        dfs(grid, r - 1, c)  # up
        dfs(grid, r + 1, c)  # down
        dfs(grid, r, c - 1)  # left
        dfs(grid, r, c + 1)  # right

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # If a land cell is found
                island_count += 1  # Increment the island counter
                dfs(grid, r, c)  # Perform DFS to mark the whole island

    return island_count
```

### Example

Let's consider the following grid:

```
[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
```

- We start with the first cell (0,0) which is '1'. We increment the island count and mark all connected lands as visited (set to '0').
- We move to the next unvisited '1' (2,2) and repeat the process.
- Finally, we encounter the last group of '1's at (3,3) and (3,4).

The output for this grid is `3` islands.

### Time Complexity

The time complexity of this solution is \(O(M x N)\), where \(M\) is the number of rows and \(N\) is the number of columns in the grid. This is because each cell is visited once.

### Space Complexity

The space complexity is also \(O(M x N)\) in the worst case due to the recursive call stack in DFS, which can go as deep as the number of cells in the grid.

### Conclusion

This approach efficiently counts the number of islands by exploring all connected land cells using DFS and marking them as visited. It ensures that each cell is processed exactly once, making it both time and space efficient for this problem.