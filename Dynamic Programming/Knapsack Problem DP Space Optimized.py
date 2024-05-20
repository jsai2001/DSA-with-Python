# Time Complexity: O(nW)
# Space Complexity: O(W)
"""
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or dont pick it (0-1 property).

Example 1:

Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3
Explanation: Choose the last item that weighs 1 unit and holds a value of 3. 
"""
"""
Dynamic Programming Approach
The dynamic programming approach builds a 2D table where the entry dp[i][w] represents the maximum value that can be achieved with the first i items and a weight limit of w.

Here's a step-by-step implementation Space Optimized approch in Python:
"""
"""
The space complexity of the dynamic programming solution provided above is O(nW), where n is the number of items and W is the maximum weight capacity of the knapsack.

Detailed Explanation:
2D DP Table:

We use a 2D list dp with dimensions (n+1) x (W+1).
dp[i][w] stores the maximum value that can be obtained using the first i items and a total weight limit w.
Space Complexity Calculation:

The total number of elements in the dp table is (n+1) * (W+1).
Therefore, the space complexity is O(nW).

Space Optimization:
In practice, we can reduce the space complexity to O(W) by using a 1D array instead of a 2D array. This optimization is possible because we only need the current and the previous row of the dp table at any point in time.

Here’s an optimized implementation:
"""
def knapsack(values, weights, W):
    n = len(values)
    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[W]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
max_value = knapsack(values, weights, W)
print(f"Maximum value in Knapsack = {max_value}")
"""
Explanation of the Optimized Approach:
Initialization:

We initialize a 1D list dp with size W + 1 to store the maximum value for each weight limit from 0 to W.
Filling the DP Array:

We iterate through each item.
For each item, we iterate through the weight limits in reverse order (from W to weights[i]), updating the dp array.
This reverse order ensures that we do not overwrite the values in dp that we need to use for the current item.
Result:

The value at dp[W] will be the maximum value that can be achieved with a weight limit of W.

Space Complexity of the Optimized Approach:
The space complexity of this optimized approach is O(W) because we are using a single 1D array of size W + 1.
"""
