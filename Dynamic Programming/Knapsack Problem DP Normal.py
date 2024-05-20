# Time Complexity: O(nW)
# Space Complexity: O(nW)
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

Here's a step-by-step implementation in Python:
"""
def knapsack(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
max_value = knapsack(values, weights, W)
print(f"Maximum value in Knapsack = {max_value}") #220
"""
Explanation:
Initialization:

We initialize a 2D list dp where dp[i][w] represents the maximum value that can be attained with the first i items and a weight limit of w.
Filling the DP Table:

We iterate through each item and each possible weight limit.
For each item i and weight limit w:
If the weight of the current item weights[i-1] is less than or equal to w, we have two choices:
Include the item: The value becomes values[i-1] plus the maximum value with the remaining weight w - weights[i-1].
Exclude the item: The value remains the same as the maximum value without this item.
We take the maximum of these two choices.
If the item's weight is greater than w, we cannot include the item, so the value remains the same as without this item.
Result:

The value at dp[n][W] will be the maximum value that can be achieved with n items and a weight limit of W.
"""
