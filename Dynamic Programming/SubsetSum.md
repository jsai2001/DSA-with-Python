# Subset Sum

Time Complexity (O(n * target_sum))
Space Complexity (O(n * target_sum))

Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explanation: 
The two parts are {1, 5, 5} and {11}.
Example 2:

Input: N = 3
arr = {1, 3, 5}
Output: NO
Explanation: This array can never be 
partitioned into two such parts.

The partition problem for finding an exact solution is known to be NP-complete, meaning there's no known efficient solution for all cases. However, we can solve it efficiently for the special case of finding an equal subset sum using Dynamic Programming (DP). Here's the Python code for the optimal solution:

```python
def can_partition(nums):
  """
  This function checks if a set of numbers can be partitioned into two subsets with equal sum.

  Args:
      nums: A list of integers representing the set of numbers.

  Returns:
      True if a partition exists, False otherwise.
  """
  total_sum = sum(nums)
  # If the sum is odd, partition is not possible
  if total_sum % 2 != 0:
    return False

  # Half of the total sum is the target subset sum
  target_sum = total_sum // 2
  dp = [[False] * (target_sum + 1) for _ in range(len(nums) + 1)]

  # Base Case: Subset with sum 0 is always possible (empty subset)
  for i in range(len(dp)):
    dp[i][0] = True

  # Build the DP table
  for i in range(1, len(nums) + 1):
    for j in range(1, target_sum + 1):
      if nums[i - 1] <= j:
        # Include or exclude the current element
        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
      else:
        # Exclude the current element if its value is greater than the remaining sum
        dp[i][j] = dp[i - 1][j]

  return dp[len(nums)][target_sum]

# Example usage
numbers = [1, 5, 11, 5]
if can_partition(numbers):
  print("The set can be partitioned into two subsets with equal sum.")
else:
  print("The set cannot be partitioned into two subsets with equal sum.")
```

This code uses a 2D DP table `dp` to store if a subset sum can be formed for a particular index and sum value. It iteratively builds the table and finally checks if the target sum can be formed using the last element (`dp[len(nums)][target_sum]`).
 
This approach has a time complexity of O(n * target_sum) and space complexity of O(n * target_sum), where n is the number of elements.

The line `dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]` in the code defines how we fill the DP table (`dp`) for the partition problem. Let's break it down:

* `dp[i][j]`: This represents the cell in the table where `i` is the current index (referring to a specific number in the input list `nums`) and `j` is the target subset sum we're trying to achieve. The value in this cell will be `True` if a subset sum of `j` can be formed using elements from the first `i` numbers in the list.

* `dp[i - 1][j]`: This refers to the cell in the table one row above the current one. It represents if a subset sum of `j` can be formed using only the first `i - 1` elements (excluding the current element).

* `dp[i - 1][j - nums[i - 1]]`: This refers to the cell one row above and `nums[i - 1]` columns to the left. It represents if a subset sum of `j - nums[i - 1]` (remaining target sum after excluding the current element) can be formed using the first `i - 1` elements.

* `or`: The `or` operator here essentially checks for two possibilities:

    1. **Include the current element:** If a subset sum of `j` can be formed using only the first `i - 1` elements (`dp[i - 1][j]`), then including the current element (`nums[i - 1]`) will also lead to a subset sum of `j`.

    2. **Exclude the current element:** If a subset sum of `j - nums[i - 1]` (remaining target sum) can be formed using the first `i - 1` elements (`dp[i - 1][j - nums[i - 1]]`), then adding the current element (`nums[i - 1]`) will also result in a subset sum of `j`.

By considering both possibilities (`or`), the `dp[i][j]` cell is set to `True` if either of the conditions is met, indicating that a subset sum of `j` can be formed using the first `i` elements (including or excluding the current element).

The time and space complexity of the dynamic programming approach for solving the partition problem with the goal of finding an equal subset sum is indeed O(n * target_sum), where n is the number of elements in the list.

Here's a breakdown of why:

**Space Complexity (O(n * target_sum))**

- The code uses a 2D DP table `dp` to store intermediate results.
- The table has dimensions (n+1) x (target_sum+1).
    - The extra rows and columns compared to `n x target_sum` are to handle base cases where the subset sum might be 0 (achieved with an empty subset).
- This translates to a space complexity of O(n * target_sum).

**Time Complexity (O(n * target_sum))**

- The code iterates through the DP table to fill it up.
- The outer loop iterates over the number of elements (`n`).
- The inner loop iterates over the possible target sums (`target_sum`).
- Within each iteration, constant time operations are performed to check conditions and update the table.

**Overall, the total number of operations is proportional to (n * target_sum), resulting in a time complexity of O(n * target_sum).**

**Comparison with O(n^2)**

While the time complexity might seem similar to O(n^2) at first glance, there's a crucial difference. In this case, the `target_sum` is bounded by the sum of the elements in the input list (`nums`). This means `target_sum` is typically less than or equal to `n` (number of elements).

Therefore, O(n * target_sum) is generally considered more efficient than O(n^2) in this specific scenario.

**Note:** It's important to remember that the partition problem itself is NP-complete for finding an exact solution. This means there's no known efficient solution for all possible cases. However, the dynamic programming approach we discussed works well for the special case of finding an equal subset sum.
