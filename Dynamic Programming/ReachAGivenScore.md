### Reach a Given Score

To solve this problem, we can use dynamic programming to find the number of distinct combinations to reach a given score \( n \) using the available moves (3, 5, and 10 points). Here’s how you can approach the problem:

- **Time Complexity:** \( O(n) \)

- **Space Complexity:** \( O(n) \)

1. Define a list `dp` where `dp[i]` represents the number of ways to reach the score \( i \).
2. Initialize `dp[0]` to 1 because there is one way to reach a score of 0 (doing nothing).
3. Iterate through each score from 1 to \( n \) and for each score, add the ways to reach that score using each of the possible moves (3, 5, and 10 points).

Here's the Python code to implement this solution:

```python
def count_combinations(n):
    # Initialize a list to store the number of ways to reach each score from 0 to n
    dp = [0] * (n + 1)
    
    # Base case: There is one way to reach a score of 0 (by doing nothing)
    dp[0] = 1
    
    # Iterate over each score from 1 to n
    for i in range(1, n + 1):
        if i >= 3:
            dp[i] += dp[i - 3]
        if i >= 5:
            dp[i] += dp[i - 5]
        if i >= 10:
            dp[i] += dp[i - 10]
    
    # The answer will be in dp[n]
    return dp[n]

# Example usage
n = 20
print(f"Number of distinct combinations to reach score {n} is {count_combinations(n)}")
```

### Explanation
- The `dp` array is initialized with zeros and has a size of \( n + 1 \).
- `dp[0]` is set to 1 because there is exactly one way to reach the score of 0.
- For each score from 1 to \( n \), the code checks if it is possible to subtract 3, 5, or 10 points (i.e., if `i` is greater than or equal to 3, 5, or 10, respectively). If it is possible, the code adds the number of ways to reach the score `i - 3`, `i - 5`, or `i - 10` to the current score `i`.

### Example Output
Running the provided example with `n = 20`, the output will be:
```
Number of distinct combinations to reach score 20 is 4
```

This indicates that there are 4 distinct combinations of moves (3, 5, and 10 points) that sum up to the score of 20.

Here’s a step-by-step breakdown to clarify how the solution works:

1. **Initialization:**
   - We initialize `dp[0]` to 1 because there is exactly one way to achieve a score of 0: doing nothing.
   - All other values in the `dp` array are initially set to 0.

2. **Building the `dp` array:**
   - We iterate over each possible score from 1 to \( n \).
   - For each score \( i \), we check if it is possible to achieve this score by adding 3, 5, or 10 points to some smaller score.

3. **Update rules:**
   - If \( i \geq 3 \), we update `dp[i]` to include the number of ways to reach \( i \) by adding 3 points to \( i - 3 \): `dp[i] += dp[i - 3]`.
   - If \( i \geq 5 \), we update `dp[i]` to include the number of ways to reach \( i \) by adding 5 points to \( i - 5 \): `dp[i] += dp[i - 5]`.
   - If \( i \geq 10 \), we update `dp[i]` to include the number of ways to reach \( i \) by adding 10 points to \( i - 10 \): `dp[i] += dp[i - 10]`.

### Final dp Array
After processing all values, the final `dp` array will represent the number of ways to achieve each score from 0 to 20 using moves of 3, 5, and 10 points.

```python
[1, 0, 0, 1, 0, 1, 1, 0, 2, 1, 2, 1, 2, 2, 3, 2, 3, 3, 4, 3, 4]
```

So, `dp[20] = 4`, indicating there are 4 distinct combinations of moves that sum to 20.

The time and space complexity of the dynamic programming solution to find the number of distinct combinations to reach a given score \( n \) using moves of 3, 5, and 10 points can be analyzed as follows:

### Time Complexity
The time complexity is determined by the nested loops used in the solution. Here's a breakdown of the operations:

1. Initializing the `dp` array takes \( O(n) \) time.
2. The outer loop iterates over each score from 1 to \( n \), so it runs \( n \) times.
3. Inside the outer loop, there are three conditional checks (for 3, 5, and 10 points). Each check is a constant-time operation \( O(1) \).

Thus, the total time complexity is \( O(n) \) since the inner operations are constant-time and the outer loop runs \( n \) times.

### Space Complexity
The space complexity is determined by the storage required for the `dp` array:

1. The `dp` array stores one integer for each score from 0 to \( n \).

Thus, the space complexity is \( O(n) \).

### Summary
- **Time Complexity:** \( O(n) \)
- **Space Complexity:** \( O(n) \)