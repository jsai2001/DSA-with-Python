# Edit Distance

Time Complexity: O(mn)

Space Complexity: O(mn)

m and n are length of strings str1 & str2 respectivily.

Python solution for calculating the edit distance between two strings using dynamic programming:

```python
def edit_distance(str1, str2):
  """
  Calculates the minimum number of edits (insertions, deletions, substitutions)
  needed to transform one string into another.

  Args:
      str1: The first string.
      str2: The second string.

  Returns:
      The edit distance between str1 and str2.
  """

  m, n = len(str1), len(str2)

  # Create a DP table to store edit distances
  dp = [[0] * (n + 1) for _ in range(m + 1)]

  # Initialize base cases: transforming empty string to another string
  for i in range(m + 1):
    dp[i][0] = i  # i deletions needed to transform empty string to str2 of length i
  for j in range(n + 1):
    dp[0][j] = j  # j insertions needed to transform empty string to str1 of length j

  # Fill the DP table
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      # If characters match, no edit required
      if str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1]
      else:
        # Minimum edit distance among insertion, deletion, substitution
        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

  return dp[m][n]

# Example usage
str1 = "kitten"
str2 = "sitting"
distance = edit_distance(str1, str2)
print("Edit distance between", str1, "and", str2, "is", distance)
```

This code defines a function `edit_distance` that takes two strings as input and returns the minimum edit distance between them. It uses a dynamic programming approach to efficiently solve the problem. 

Here's a breakdown of the code:

1. **Base Cases:** We initialize the first row and column of the `dp` table to represent the edit distance needed to transform an empty string to the other string (all deletions or insertions).
2. **DP Table Filling:** We iterate through the table, considering the characters at each position in both strings. If the characters match, no edit is needed. Otherwise, we calculate the minimum edit distance by considering:
    - Deleting the character in str1
    - Inserting the character in str2
    - Substituting the character in str1 with the character in str2
3. **Return Value:** The final element `dp[m][n]` in the table represents the minimum edit distance between the entire strings `str1` and `str2`.

This solution provides a time complexity of O(mn) and space complexity of O(mn), where m and n are the lengths of the strings.