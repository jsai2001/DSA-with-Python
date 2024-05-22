## Longest Common Subsequence

Time Complexity: O(m*n)

Space Complexity: O(m*n)

The longest common subsequence (LCS) problem is to find the longest sequence of characters that appear in the same order within two given strings. Here's an optimal solution for finding LCS in Python using dynamic programming (DP):

```python
def lcs(text1, text2):
  """
  This function finds the longest common subsequence (LCS) of two strings.

  Args:
      text1: The first string.
      text2: The second string.

  Returns:
      The length of the LCS and the LCS itself.
  """
  m = len(text1)
  n = len(text2)

  # Create a DP table to store the lengths of LCS ending at each index
  dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

  # Fill the DP table
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if text1[i - 1] == text2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

  # Backtrack to find the LCS
  lcs_len = dp[m][n]
  lcs = ""
  i, j = m, n
  while i > 0 and j > 0:
    if text1[i - 1] == text2[j - 1]:
      lcs = text1[i - 1] + lcs
      i -= 1
      j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
      i -= 1
    else:
      j -= 1

  return lcs_len, lcs

# Example usage
text1 = "AGGTAB"
text2 = "GXTXAYB"
lcs_len, lcs = lcs(text1, text2)

print("Length of LCS:", lcs_len)
print("LCS:", lcs)
```

This code defines a function `lcs` that takes two strings as input and returns the length and the actual LCS of the two strings. It uses a DP approach to efficiently build a table that stores the lengths of LCS ending at each index. The table is then used to backtrack and find the actual LCS.

Here's a breakdown of how the code works:

1. **Initialization:**
   - The `lcs` function takes two strings `text1` and `text2` as input.
   - It creates a DP table `dp` of size (m + 1) x (n + 1), where m and n are the lengths of `text1` and `text2` respectively. The table will store the lengths of LCS ending at each index.

2. **Filling the DP table:**
   - The table is filled in a bottom-up manner.
   - We iterate through the table starting from index (1, 1) to (m, n).
   - At each index (i, j), we check if the characters at indices i-1 in `text1` and j-1 in `text2` are equal.
     - If they are equal, the LCS ending at index (i, j) is one character longer than the LCS ending at index (i-1, j-1). So, `dp[i][j] = dp[i - 1][j - 1] + 1`.
     - If they are not equal, the LCS ending at index (i, j) is the maximum of the LCS ending at index (i-1, j) (excluding the character at index i-1 in `text1`) and the LCS ending at index (i, j-1) (excluding the character at index j-1 in `text2`). So, `dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])`.

3. **Backtracking to find LCS:**
   - After filling the DP table, we backtrack to find the actual LCS. We start from the bottom right corner of the table (index (m, n)).
   - We use a variable `lcs` to store the LCS string being built.
   - We iterate until we reach the top left corner of the table (index (0, 0)).
   - At each step, we check the value in the current cell of the DP table

Time Complexity:
- The code iterates through the DP table twice.
- Once to fill the table, which involves nested loops iterating from 1 to m and 1 to n. This contributes O(m * n) time complexity.
- Once to backtrack and find the LCS, but this loop also iterates a maximum of m + n times in the worst case. So, it doesn't significantly affect the overall time complexity which remains O(m * n).

Space Complexity:
- The code creates a DP table of size (m + 1) x (n + 1). This table requires O(m * n) space to store the intermediate results.