## Word Wrap Problem

- **Time Complexity:** \(O(n^2)\)

- **Space Complexity:** \(O(n^2)\)

To solve the problem of minimizing the total cost for neatly printing words on multiple lines with the given constraints, we can use dynamic programming. Let's delve into the approach, and then we'll discuss the time and space complexity.

### Approach

1. **Define the Problem:** 
   - Let `nums` be the array where `nums[i]` is the number of characters in the i-th word.
   - `K` is the maximum number of characters per line.
   - We need to minimize the total cost, where the cost of a line is the square of the number of extra spaces at the end of the line.

2. **Dynamic Programming Solution:**
   - Use a dynamic programming array `dp` where `dp[i]` represents the minimum cost to arrange words from `i` to `n-1`.
   - Another array `breaks` can be used to store the points where lines are broken to reconstruct the solution.

3. **Compute Extra Spaces:**
   - For each pair of indices `i` and `j` (where `i <= j`), calculate the extra spaces if words from `i` to `j` are put on one line.
   - If `sum(nums[i:j+1]) + (j - i) <= K`, compute the extra spaces as `K - sum(nums[i:j+1]) - (j - i)`, otherwise mark it as not feasible.

4. **Recurrence Relation:**
   - The recurrence relation is `dp[i] = min((extra_spaces[i][j])^2 + dp[j+1])` for all `j` from `i` to `n-1`.

5. **Initialization:**
   - `dp[n] = 0` since there's no cost if no words are left.

### Algorithm

Here is the algorithm to implement the solution:

```python
def minimize_cost(nums, K):
    n = len(nums)
    extra_spaces = [[0] * n for _ in range(n)]
    for i in range(n):
        extra_spaces[i][i] = K - nums[i]
        for j in range(i + 1, n):
            extra_spaces[i][j] = extra_spaces[i][j-1] - nums[j] - 1

    dp = [float('inf')] * (n + 1)
    dp[n] = 0
    breaks = [-1] * n

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if extra_spaces[i][j] < 0:
                break
            cost = (extra_spaces[i][j])**2 + dp[j+1]
            if cost < dp[i]:
                dp[i] = cost
                breaks[i] = j + 1

    return dp[0]

# Example usage
nums = [3, 2, 2, 5]
K = 6
print(minimize_cost(nums, K))  # Output: minimized cost
```

### Time and Space Complexity

1. **Time Complexity:**
   - The nested loop to calculate extra spaces takes `O(n^2)` time.
   - Filling up the `dp` array also takes `O(n^2)` time since for each `i`, it can go through all `j` from `i` to `n-1`.
   - Hence, the overall time complexity is `O(n^2)`.

2. **Space Complexity:**
   - We use an `extra_spaces` matrix of size `n x n`, which takes `O(n^2)` space.
   - The `dp` and `breaks` arrays take `O(n)` space each.
   - Thus, the overall space complexity is `O(n^2)`.

This dynamic programming approach efficiently solves the problem within reasonable time and space constraints for typical values of `n`.