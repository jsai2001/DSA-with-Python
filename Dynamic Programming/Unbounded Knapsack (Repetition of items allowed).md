### Unbounded knapsack problem

To solve the unbounded knapsack problem, where each item can be taken any number of times, we can use dynamic programming (DP). Here's a detailed explanation of how to approach this problem:

- Time Complexity: \( O(N x W) \)

- Space Complexity: \( O(W) \)

## Problem Statement
Given:
- \( N \) items, each with a weight \( w[i] \) and a value \( val[i] \).
- A knapsack with a weight limit \( W \).

We need to determine the maximum value that can be obtained by filling the knapsack without exceeding the weight limit \( W \). Each item can be taken any number of times.

## Approach

### Dynamic Programming Solution

1. **Define the DP array:**
   - Let `dp[j]` represent the maximum value that can be obtained with a knapsack capacity of \( j \).

2. **Initialization:**
   - Initialize `dp[0]` to 0 because the maximum value with a knapsack of capacity 0 is 0.
   - Initialize the rest of `dp` array to 0 or some other value indicating an uninitialized state.

3. **DP Transition:**
   - For each item, update the `dp` array from the current weight to the maximum capacity \( W \):
     \[
     \text{dp}[j] = \max(\text{dp}[j], \text{dp}[j - w[i]] + \text{val}[i])
     \]
   - This means that for each item and each possible knapsack capacity, we decide whether to include the item (and thus add its value to the knapsack's total value).

4. **Result:**
   - The value of `dp[W]` will be the maximum value achievable with the knapsack of capacity \( W \).

### Pseudocode

```python
def unbounded_knapsack(W, weights, values):
    N = len(weights)
    dp = [0] * (W + 1)

    for i in range(N):
        for j in range(weights[i], W + 1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[W]
```

### Explanation

1. **Initialization:**
   - `dp` array of size \( W + 1 \) is initialized to 0.
   
2. **Iterate over each item:**
   - For each item `i` (from 0 to \( N-1 \)), iterate through possible weights `j` (from `weights[i]` to \( W \)).
   
3. **Update `dp` array:**
   - Update `dp[j]` by considering whether including item `i` leads to a higher value than not including it.

4. **Return the result:**
   - The maximum value for a knapsack of capacity \( W \) is found at `dp[W]`.

### Time Complexity

- The time complexity of this algorithm is \( O(N x W) \), where \( N \) is the number of items and \( W \) is the maximum weight capacity of the knapsack.
  - This is because we iterate through each item and for each item, we iterate through all possible weights from the item's weight up to \( W \).

### Space Complexity

- The space complexity is \( O(W) \) because we use a single-dimensional DP array of size \( W + 1 \).

## Example

Suppose we have the following items and knapsack:
- Weights: [2, 3, 4]
- Values: [5, 4, 8]
- Knapsack capacity \( W \) = 6

Using the given function, we would determine the maximum value that can be obtained:

```python
W = 6
weights = [2, 3, 4]
values = [5, 4, 8]

max_profit = unbounded_knapsack(W, weights, values)
print(max_profit)  # Output should be 15
```

This example means we can take the first item three times (since 2 * 3 = 6 and 5 * 3 = 15), leading to a maximum profit of 15.