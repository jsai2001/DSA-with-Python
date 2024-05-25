## Longest Common Subsequence

Time Complexity: O(m*n)

Space Complexity: O(min(m, n))

## Space-Optimized LCS with Swapping Explanation and Code

**Challenge:**

The standard LCS solution using Dynamic Programming (DP) requires a 2D table, leading to O(m*n) space complexity (m and n are string lengths). This can be inefficient for large inputs.

**Solution:**

A space-optimized approach uses two 1D arrays (`prev` and `curr`) to store the previous and current rows of the DP table, reducing space complexity to O(min(m, n)).

**Key Concept: Swapping `prev` and `curr`**

1. **Initialization:**
   - `prev` and `curr` are initialized with size `m + 1` (or `n + 1`, both work). This ensures enough space for calculations involving characters from one string (and the empty string).

2. **Iteration:**
   - We iterate over the first string (i loop).
   - **Within each iteration (i):**
      - We use values in `prev` (representing the previous row for the current character in the first string) to calculate LCS lengths for the current character with each character in the second string (j loop).
      - We store these calculated LCS lengths in `curr` (representing the current row).

3. **Swapping:**
   - **Crucially, after the j loop finishes for the current iteration (i):**
      - We swap `prev` and `curr`. This seems counterintuitive at first, but it's essential for space optimization.

**Why Swapping Works:**

- We don't need the LCS lengths for the current character (stored in `curr`) anymore in the next iteration (i+1) because we'll be calculating LCS for the **next** character of the first string.
- By swapping `prev = curr`, we:
    - Discard values in `prev` (previous row for the current character).
    - Reuse `curr` to store LCS lengths for the **next** character (using the values from the now-swapped `prev`).

**Code Example:**

```python
def lcs_space_optimized(text1, text2):
  """
  This function finds the length of the Longest Common Subsequence (LCS) of two strings
  using a space-optimized approach.

  Args:
      text1: The first string.
      text2: The second string.

  Returns:
      The length of the LCS.
  """
  m = len(text1)
  n = len(text2)
  prev, curr = [0] * (max(m,n) + 1), [0] * (max(m,n) + 1)  # Corrected initialization

  # Iterate over the first string
  for i in range(1, m + 1):
    # Swap prev and curr for each iteration
    prev, curr = curr, prev

    # Iterate over the second string
    for j in range(1, n + 1):
      if text1[i - 1] == text2[j - 1]:
        curr[j] = prev[j - 1] + 1
      else:
        curr[j] = max(prev[j], curr[j - 1])

  # The length of LCS is the maximum value in the last row (curr)
  return max(curr)
```

**Summary:**

By understanding the role of swapping and how the arrays are reused, we can effectively solve LCS with reduced space complexity.

The space-optimized LCS solution has the following time and space complexity:

* **Time Complexity:** O(m*n)
* **Space Complexity:** O(min(m, n))

**Time Complexity:**

- The time complexity remains the same as the standard DP solution.
- We iterate over the first string (i loop) with a maximum of `m` iterations.
- Within each iteration, we iterate over the second string (j loop) with a maximum of `n` iterations.
- Inside the j loop, constant time operations like comparisons and assignments occur.

Therefore, the overall time complexity is dominated by the nested loops, resulting in O(m*n).

**Space Complexity:**

- This is where the optimization comes in.
- We only use two 1D arrays (`prev` and `curr`) of size `min(m, n) + 1`. This ensures enough space for calculations involving characters from one string (and the empty string).
- By swapping `prev` and `curr` after each iteration (i), we reuse the same two arrays for both the previous and current rows.
- This significantly reduces space complexity from O(m*n) (standard DP) to O(min(m, n)).

**In summary:**

The space-optimized LCS solution trades some additional calculations (swapping) for a significant reduction in space usage, making it suitable for handling larger inputs.