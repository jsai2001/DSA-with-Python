### Longest Palindromic Subsequence (LPS) Problem

- Time Complexity: O(n*n)

- Space Complexity: O(n*n)

The problem of finding the Longest Palindromic Subsequence (LPS) is a classic dynamic programming problem. The goal is to determine the length of the longest subsequence of a given string that is a palindrome.

A **subsequence** is a sequence derived from another sequence by deleting some elements without changing the order of the remaining elements. A **palindrome** is a sequence that reads the same backward as forward.

### Dynamic Programming Solution

To solve this problem, we can use a dynamic programming approach. Let's break down the solution:

1. **Define the State**:
   Let `dp[i][j]` represent the length of the longest palindromic subsequence in the substring `s[i:j+1]`.

2. **State Transition**:
   - If `s[i] == s[j]`, then the length of the longest palindromic subsequence can be extended by 2 from `dp[i+1][j-1]`. Therefore, `dp[i][j] = dp[i+1][j-1] + 2`.
   - If `s[i] != s[j]`, then the longest palindromic subsequence will be the maximum of the subsequences found by either excluding the current character from the beginning or from the end. Therefore, `dp[i][j] = max(dp[i+1][j], dp[i][j-1])`.

3. **Initialization**:
   - For a single character, the longest palindromic subsequence is 1, i.e., `dp[i][i] = 1` for all `i`.

4. **Result**:
   - The length of the longest palindromic subsequence of the entire string `s` will be `dp[0][n-1]` where `n` is the length of the string.

### Algorithm

```python
def longest_palindromic_subsequence(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0

    # Create a 2D array to store results of subproblems
    dp = [[0] * n for _ in range(n)]

    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build the table. Note that the lower diagonal values of the table are useless and not filled in the process.
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    
    return dp[0][n-1]
```

### Example

Consider the string `s = "bbbab"`:
- The longest palindromic subsequence is "bbbb" with a length of 4.

### Time and Space Complexity

- **Time Complexity**: \(O(n^2)\), where \(n\) is the length of the string. This is because we are filling up a table of size \(n \times n\), and each cell in the table is computed in constant time.
- **Space Complexity**: \(O(n^2)\), due to the storage required for the `dp` table.

### Summary

The dynamic programming solution efficiently computes the length of the longest palindromic subsequence by breaking down the problem into smaller subproblems and solving each subproblem only once. The overall complexity ensures that it is feasible to handle reasonably large strings within practical limits.