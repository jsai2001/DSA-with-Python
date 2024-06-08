### Largest area rectangular sub-matrix with equal number of 1’s and 0’s

To solve the problem of finding the largest area rectangular sub-matrix with an equal number of 1’s and 0’s, we can use a technique similar to finding the largest subarray with an equal number of 0's and 1's in a 1D array. The key idea is to transform the problem into a 1D problem and then use a hash map to store the prefix sum indices.

- **Time Complexity:** \(O(n^2 . m)\)

- **Space Complexity:** \(O(n . m)\)

Here’s a step-by-step approach to solve the problem:

1. **Transform the matrix:** Convert the matrix into a new matrix where 0's are replaced with -1's. This transformation helps in calculating the prefix sums where the sum of subarray equals zero implies an equal number of 1’s and -1’s (i.e., 1’s and 0’s in the original matrix).

2. **Calculate prefix sums for sub-matrices:** For each pair of rows, calculate the prefix sum for each column and use a hash map to find the largest subarray with a sum of zero between these two rows.

3. **Update maximum area:** Track the maximum area encountered during the iteration.

Here is the Python implementation of the above approach:

```python
def largest_submatrix_with_equal_ones_zeros(matrix):
    def max_len_zero_sum(arr):
        hash_map = {}
        max_len = 0
        curr_sum = 0
        
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum == 0:
                max_len = i + 1
            if curr_sum in hash_map:
                max_len = max(max_len, i - hash_map[curr_sum])
            else:
                hash_map[curr_sum] = i
        return max_len
    
    if not matrix or not matrix[0]:
        return 0
    
    n = len(matrix)
    m = len(matrix[0])
    max_area = 0
    
    # Convert the matrix: Replace 0 with -1
    new_matrix = [[-1 if matrix[i][j] == 0 else 1 for j in range(m)] for i in range(n)]
    
    # Calculate the maximum area submatrix
    for top in range(n):
        temp = [0] * m
        for bottom in range(top, n):
            for col in range(m):
                temp[col] += new_matrix[bottom][col]
            
            # Find the maximum length of subarray with sum 0 in temp
            max_len = max_len_zero_sum(temp)
            max_area = max(max_area, max_len * (bottom - top + 1))
    
    return max_area

# Example usage:
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

print(largest_submatrix_with_equal_ones_zeros(matrix))  # Output: 6
```

### Explanation:

1. **Transform the Matrix:**
   - Replace each 0 with -1 in the matrix.

2. **Iterate over all pairs of rows:**
   - For each pair of rows `(top, bottom)`, create a temporary array `temp` that contains the column sums for the rows between `top` and `bottom`.

3. **Use Hash Map for Prefix Sum:**
   - For each `temp`, find the largest subarray with a sum of zero using a hash map.

4. **Calculate Area:**
   - The area of the submatrix is given by `max_len * (bottom - top + 1)`.

5. **Track Maximum Area:**
   - Update the `max_area` with the maximum area found during iterations.

This approach efficiently finds the largest rectangular submatrix with equal numbers of 1's and 0's by leveraging the prefix sum and hash map technique commonly used in 1D problems.

The time and space complexity of the approach can be analyzed as follows:

### Time Complexity

1. **Transform the Matrix:**
   - Replacing 0's with -1's takes \(O(n . m)\) time where \(n\) is the number of rows and \(m\) is the number of columns.

2. **Iterate over all pairs of rows:**
   - There are \(O(n^2)\) pairs of rows since for each row `top`, you can pair it with every row `bottom` below it including itself.

3. **Column Sum Calculation:**
   - For each pair of rows, you need to compute the sum for each column between those rows, which takes \(O(m)\) time.

4. **Finding the Maximum Length Subarray with Sum Zero:**
   - For each temporary array `temp`, finding the largest subarray with a sum of zero using a hash map takes \(O(m)\) time.

Combining these steps:
- The outer loop for the pairs of rows takes \(O(n^2)\) time.
- For each pair of rows, the inner steps (summing columns and finding max length) take \(O(m)\) time.

Therefore, the overall time complexity is:
\[ O(n^2 . m) \]

### Space Complexity

1. **Transform the Matrix:**
   - Requires \(O(n . m)\) space for the transformed matrix.

2. **Temporary Array:**
   - Requires \(O(m)\) space for the temporary array `temp`.

3. **Hash Map:**
   - The hash map used for finding the maximum length subarray can potentially store up to \(O(m)\) entries in the worst case.

Therefore, the overall space complexity is:
\[ O(n . m) \]

### Summary

- **Time Complexity:** \(O(n^2 . m)\)
- **Space Complexity:** \(O(n . m)\)

This complexity analysis shows that the approach is quite efficient for moderately sized matrices, but for very large matrices, performance might be a concern due to the \(n^2\) factor in the time complexity.