### Maximum Sum Rectangle In 2D Matrix

To find the maximum sum submatrix in a given 2D matrix \( M \) of dimensions \( R x C \), we can use an efficient approach that leverages the Kadane's algorithm. This approach is a combination of dynamic programming and the maximum subarray problem. Here's a step-by-step explanation:

- **Time Complexity**: \( O(C^2 x R) \), where \( C \) is the number of columns and \( R \) is the number of rows.

- **Space Complexity**: \( O(R) \).

1. **Initial Setup**:
   - Consider each pair of columns and treat the elements between these columns as a 1D array.
   - Apply Kadane's algorithm to find the maximum sum subarray in this 1D array.

2. **Iterate over all column pairs**:
   - For each pair of columns, compute the sum of elements for every row between these columns, forming a temporary 1D array.
   - Use Kadane's algorithm on this temporary 1D array to find the maximum sum subarray.

3. **Keep track of the maximum sum encountered**:
   - Update the global maximum sum if the current subarray sum is higher.

Here is the Python implementation of this approach:

```python
def max_sum_submatrix(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')

    for left in range(cols):
        # Initialize a temporary list to store row sums
        row_sums = [0] * rows
        
        for right in range(left, cols):
            # Update row_sums with the sum of elements from left to right column
            for i in range(rows):
                row_sums[i] += matrix[i][right]

            # Apply Kadane's algorithm to find the maximum sum subarray in row_sums
            current_max = float('-inf')
            current_sum = 0

            for sum_val in row_sums:
                current_sum += sum_val
                if current_sum > current_max:
                    current_max = current_sum
                if current_sum < 0:
                    current_sum = 0

            # Update the global maximum sum
            if current_max > max_sum:
                max_sum = current_max

    return max_sum

# Example usage:
matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

print("Maximum sum submatrix:", max_sum_submatrix(matrix))
```

### Explanation of the Code:
1. **Initialization**: `max_sum` is initialized to negative infinity to handle all potential submatrix sums.
2. **Iterating over Column Pairs**: The outer loop picks a starting column (`left`). The inner loop picks an ending column (`right`), forming a submatrix between these two columns.
3. **Row Sums Calculation**: For each pair of columns, we calculate the row sums between these columns and store them in `row_sums`.
4. **Kadane's Algorithm**: We apply Kadane's algorithm on the `row_sums` array to find the maximum sum subarray for the current column pair.
5. **Update Global Maximum**: We update the global maximum submatrix sum if the current maximum found is greater.

This approach ensures that the solution is efficient, with a time complexity of \( O(C^2 x R) \), making it feasible for reasonably sized matrices.

The space complexity of the above approach is determined by the additional data structures we use to store intermediate results. Let's analyze it step by step:

1. **Temporary Row Sums Array**:
   - We use a list `row_sums` of size \( R \) to store the sum of elements for each row between the current pair of columns.
   - This list is reinitialized for each pair of columns, but its size remains \( R \) throughout.

2. **Additional Variables**:
   - Variables like `max_sum`, `current_max`, and `current_sum` are used to keep track of the maximum sums and intermediate calculations. These are constant space variables.

Thus, the dominant factor in the space complexity is the `row_sums` list.

### Space Complexity Analysis

- The `row_sums` list requires \( O(R) \) space, where \( R \) is the number of rows in the matrix.
- All other variables require \( O(1) \) space.

Therefore, the overall space complexity of this approach is:

\[ O(R) \]

This makes the space complexity linear with respect to the number of rows in the matrix. Here's the summary:

- **Time Complexity**: \( O(C^2 x R) \), where \( C \) is the number of columns and \( R \) is the number of rows.
- **Space Complexity**: \( O(R) \).