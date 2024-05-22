# Time Complexity: O(n*m)
# Space Complexity: O(n*m)

Gold mine problem can be solved using dynamic programming in Python. Here's the approach:

**1. Problem Definition:**

Imagine a gold mine represented by a 2D grid. Each cell holds a certain amount of gold. The miner starts at any position in the first column and can move diagonally up-right, right, or diagonally down-right to collect gold. The goal is to find the path that yields the maximum total amount of gold collected.

**2. Dynamic Programming Solution:**

This solution builds upon the concept that the optimal value for a cell depends on the maximum values from the previous column's adjacent cells. We can iteratively calculate the maximum gold obtainable for each cell in the grid.

**3. Code Implementation:**

```python
def max_gold(mine):
  """
  Finds the maximum amount of gold collectable in the mine grid.

  Args:
      mine: A 2D list representing the gold mine, where each cell contains the amount of gold.

  Returns:
      The maximum amount of gold collectable.
  """
  rows, cols = len(mine), len(mine[0])
  dp = [[0 for _ in range(cols)] for _ in range(rows)]

  # Fill the first column with its own gold values
  for i in range(rows):
    dp[i][0] = mine[i][0]

  # Iterate through the grid from the second column onwards
  for col in range(1, cols):
    for row in range(rows):
      # Consider all valid moves from the previous column
      up_right = dp[row - 1][col - 1] if row > 0 else 0
      right = dp[row][col - 1]
      down_right = dp[row + 1][col - 1] if row < rows - 1 else 0

      # Update the current cell with the maximum obtainable gold
      dp[row][col] = max(up_right, right, down_right) + mine[row][col]

  # Find the maximum value in the last column (represents max gold obtainable)
  return max(row[-1] for row in dp)

# Example usage
mine = [
    [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]
]

max_gold_collectable = max_gold(mine)
print(f"Maximum Gold Collectable: {max_gold_collectable}")
```

**4. Explanation:**

- The `max_gold` function takes the mine grid as input.
- It initializes a `dp` (dynamic programming) table to store the maximum gold obtainable for each cell.
- The first column is filled with its own gold values.
- We iterate through the remaining columns, considering valid moves (diagonally up-right, right, diagonally down-right) from the previous column for each cell.
- The current cell's value is updated with the maximum obtainable gold from the previous moves plus its own gold.
- Finally, the maximum value in the last column represents the maximum total gold collectable.

This code utilizes dynamic programming to efficiently find the optimal path through the gold mine for maximum gold collection.

**Time Complexity (O(n * m)):** The time complexity arises from the nested loops iterating through the dp table (n rows and m columns). Within each cell's calculation, there are constant-time operations for finding the maximum value from the previous column's moves.

**Space Complexity (O(n * m)):** The space complexity is O(n * m) due to the creation of the dp table, which has the same dimensions as the input grid. This table stores intermediate results for efficient computation.