### Travelling Salesman Problem (TSP) using Dynamic Programming

The Travelling Salesman Problem (TSP) is a classic optimization problem. The problem is to find the shortest possible route that visits each city exactly once and returns to the origin city. The dynamic programming approach to solve TSP is known as the Held-Karp algorithm.

- **Time Complexity:** `O(n^2 * 2^n)`

- **Space Complexity:** `O(2^n * n)`

### Dynamic Programming Approach

The dynamic programming approach uses a bitmask to represent subsets of cities and memoization to store the minimum cost of visiting these subsets.

#### Steps to Solve TSP using Dynamic Programming

1. **Initialization:**
   - Define `dp[mask][i]` as the minimum cost to visit all the cities in `mask` ending at city `i`.
   - `mask` is a bitmask where the `j`-th bit is `1` if city `j` is included in the subset.
   - The array size is `dp[2^n][n]` where `n` is the number of cities.

2. **Base Case:**
   - `dp[1 << i][i] = cost[0][i]` for all `i` from 1 to n-1. This means that the cost to go from the start city (city 0) to city `i` is just the direct distance from city 0 to city `i`.

3. **Transition:**
   - For each subset `mask` and for each `i` in `mask`, update `dp[mask][i]` by considering the transition from every city `j` in `mask` to `i`:
     ```python
     dp[mask][i] = min(dp[mask][i], dp[mask ^ (1 << i)][j] + cost[j][i])
     ```
   - Here, `mask ^ (1 << i)` represents the subset `mask` without city `i`.

4. **Result:**
   - The final result will be the minimum cost to visit all cities and return to the starting city:
     ```python
     min(dp[(1 << n) - 1][i] + cost[i][0] for i in range(1, n))
     ```

#### Implementation

Here is the Python code to solve TSP using dynamic programming:

```python
def tsp(cost):
    n = len(cost)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Starting from the first city

    for mask in range(1, 1 << n):
        for i in range(n):
            if mask & (1 << i):
                for j in range(n):
                    if mask & (1 << j) and i != j:
                        dp[mask][i] = min(dp[mask][i], dp[mask ^ (1 << i)][j] + cost[j][i])

    return min(dp[(1 << n) - 1][i] + cost[i][0] for i in range(1, n))

# Example usage
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(tsp(cost))
```

### Complexity Analysis

- **Time Complexity:**
  - The total number of states is `O(2^n * n)` because there are `2^n` subsets of cities and each subset can end at any of the `n` cities.
  - For each state, we consider `O(n)` transitions. Therefore, the time complexity is `O(n^2 * 2^n)`.

- **Space Complexity:**
  - The space required for the `dp` array is `O(2^n * n)`.
  - Additional space is used for the `cost` matrix and variables, which is `O(n^2)`.

Thus, the space complexity is dominated by the `dp` array, resulting in `O(2^n * n)`.

### Conclusion

The dynamic programming solution for the Travelling Salesman Problem provides a feasible approach for small to medium-sized instances due to its exponential time and space complexity. For larger instances, heuristic or approximation algorithms are typically used.

Certainly! Let's break down the formula and the bit manipulation involved in the dynamic programming solution for the Travelling Salesman Problem (TSP) in more detail.

### Understanding `1 << i`

The expression `1 << i` is a bitwise operation that shifts the number `1` to the left by `i` positions. In binary representation, this effectively creates a bitmask where only the `i`-th bit is set to `1` and all other bits are `0`.

#### Example:
- `1 << 0` results in `0001` (binary) which is `1` (decimal).
- `1 << 1` results in `0010` (binary) which is `2` (decimal).
- `1 << 2` results in `0100` (binary) which is `4` (decimal).
- `1 << 3` results in `1000` (binary) which is `8` (decimal).

### Bitmask Representation

A bitmask is a way to represent subsets of a set using bits. Each bit in an integer represents whether a corresponding element (e.g., city) is included in the subset.

- If the bit is `1`, the city is included in the subset.
- If the bit is `0`, the city is not included.

### Base Case Explanation

The formula `dp[1 << i][i] = cost[0][i]` initializes the base case of our dynamic programming solution. Here’s what it means:

- `1 << i` creates a bitmask where only the `i`-th bit is `1`, representing the subset that includes only the city `i` (assuming city `0` is the starting point and always included initially).
- `dp[1 << i][i]` stores the minimum cost to visit the subset of cities represented by `1 << i` and ending at city `i`.
- `cost[0][i]` is the direct travel cost from the starting city `0` to city `i`.

### Transition Explanation

The transition formula is:
```python
dp[mask][i] = min(dp[mask][i], dp[mask ^ (1 << i)][j] + cost[j][i])
```
Let’s break it down:

- **`mask`**: Represents the current subset of cities.
- **`i`**: The current city we are ending at within the subset `mask`.
- **`j`**: Another city in the subset `mask` (except `i`), which we consider as the previous city before reaching `i`.

#### Explanation of `mask ^ (1 << i)`

- **`mask ^ (1 << i)`**: This removes city `i` from the subset `mask`. The `^` operator is a bitwise XOR.
  - If `mask` is `0110` (i.e., it includes cities `1` and `2`), and `i` is `2`, then `1 << i` is `0100`. `mask ^ (1 << i)` is `0110 ^ 0100` which results in `0010` (i.e., the subset including only city `1`).

### Overall Transition

- **`dp[mask][i]`**: Minimum cost to visit all cities in `mask` ending at `i`.
- **`dp[mask ^ (1 << i)][j]`**: Minimum cost to visit all cities in the subset excluding `i` and ending at `j`.
- **`cost[j][i]`**: Cost to travel from city `j` to city `i`.

By considering all possible previous cities `j` in the subset (except `i`), we update the minimum cost to reach `i` by possibly transitioning from `j` to `i`.

### Final Result

The final result will be the minimum cost to visit all cities and return to the starting city:
```python
min(dp[(1 << n) - 1][i] + cost[i][0] for i in range(1, n))
```
Here, `(1 << n) - 1` represents the bitmask with all `n` cities included (all bits set to `1`). This loop checks the cost of returning to the starting city from each possible ending city.

### Full Python Implementation

Here is the full implementation with comments for clarity:

```python
def tsp(cost):
    n = len(cost)
    # Initialize dp table with infinity
    dp = [[float('inf')] * n for _ in range(1 << n)]
    # Starting point, cost from 0 to 0 is 0
    dp[1][0] = 0

    for mask in range(1, 1 << n):
        for i in range(n):
            if mask & (1 << i):
                for j in range(n):
                    if mask & (1 << j) and i != j:
                        dp[mask][i] = min(dp[mask][i], dp[mask ^ (1 << i)][j] + cost[j][i])

    # Find the minimum cost to visit all cities and return to the start
    return min(dp[(1 << n) - 1][i] + cost[i][0] for i in range(1, n))

# Example usage
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(tsp(cost))
```

### Complexity Analysis

- **Time Complexity:** `O(n^2 * 2^n)`
  - We have `2^n` subsets.
  - For each subset, we consider up to `n` ending cities.
  - For each ending city, we consider up to `n` transitions.

- **Space Complexity:** `O(2^n * n)`
  - The `dp` array requires `2^n` subsets, each storing `n` values.

This solution is optimal for small to medium-sized problems but becomes impractical for very large `n` due to exponential growth.