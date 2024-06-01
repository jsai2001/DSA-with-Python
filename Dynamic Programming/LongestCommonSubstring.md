To find the length of the longest common substring between two strings using Python, you can use dynamic programming. Here's a detailed explanation along with the Python code, time complexity, and space complexity analysis.

- Time Complexity: O(m x n)

- Space Complexity: O(m x n)

### Dynamic Programming Approach

Dynamic programming is an efficient method to solve problems by breaking them down into simpler subproblems. For finding the longest common substring, we create a 2D table (matrix) where each cell represents the length of the longest common suffix of substrings ending at particular indices of the two input strings.

### Steps to Implement

1. **Initialize a 2D Table:**
   Create a 2D table `dp` where `dp[i][j]` will store the length of the longest common suffix of the substrings `s1[0..i-1]` and `s2[0..j-1]`.

2. **Fill the Table:**
   - If `s1[i-1] == s2[j-1]`, then `dp[i][j] = dp[i-1][j-1] + 1`.
   - Otherwise, `dp[i][j] = 0`.
   - Keep track of the maximum value in the table, which will be the length of the longest common substring.

3. **Return the Maximum Value:**
   The maximum value in the table will be the length of the longest common substring.

### Time and Space Complexity

- **Time Complexity:** \(O(m x n)\), where \(m\) and \(n\) are the lengths of the two strings.
- **Space Complexity:** \(O(m x n)\) due to the 2D table used for storing the lengths of common suffixes.

### Python Code

Here's the Python implementation of the above approach:

```python
def longest_common_substring(s1, s2):
    # Lengths of the input strings
    m, n = len(s1), len(s2)
    
    # Initialize the 2D DP table with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variable to store the length of the longest common substring
    max_length = 0
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0
    
    return max_length

# Example usage
s1 = "abcde"
s2 = "abfce"
print(f"The length of the longest common substring is {longest_common_substring(s1, s2)}")
```

### Explanation of the Code

1. **Initialization:**
   ```python
   m, n = len(s1), len(s2)
   dp = [[0] * (n + 1) for _ in range(m + 1)]
   max_length = 0
   ```

   - `m` and `n` are the lengths of the two strings.
   - `dp` is initialized as a 2D list of size `(m+1) x (n+1)` filled with zeros.
   - `max_length` will store the length of the longest common substring found.

2. **Filling the DP Table:**
   ```python
   for i in range(1, m + 1):
       for j in range(1, n + 1):
           if s1[i - 1] == s2[j - 1]:
               dp[i][j] = dp[i - 1][j - 1] + 1
               max_length = max(max_length, dp[i][j])
           else:
               dp[i][j] = 0
   ```

   - Iterate through each character of `s1` and `s2`.
   - If characters match, update `dp[i][j]` to `dp[i-1][j-1] + 1` and update `max_length`.
   - If characters do not match, set `dp[i][j]` to 0.

3. **Return the Result:**
   ```python
   return max_length
   ```

   - The function returns the maximum length of the common substring found.

This method efficiently finds the length of the longest common substring in \(O(m x n)\) time using \(O(m x n)\) space.