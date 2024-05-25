## Maximum Sum Increasing Subsequence

Time Complexity: O(n^2)

Space Complexity: O(n)

Let's dive into the problem of finding the "Maximum Sum Increasing Subsequence" (MSIS) and implement it in Python with clear documentation.

### Problem Statement

Given an array of integers, the task is to find the maximum sum of an increasing subsequence in the array. A subsequence is derived from the array by deleting some or no elements without changing the order of the remaining elements.

### Approach

To solve this problem, we can use a dynamic programming approach. Here are the steps:

1. **Initialization**: Create an array `msis` where `msis[i]` will store the maximum sum of the increasing subsequence that ends with the element at index `i`.

2. **Base Case**: Each element is an increasing subsequence of length 1, so initialize `msis[i]` with the value of the element at index `i`.

3. **Build the `msis` array**:
    - For each element `arr[i]`, check all the previous elements `arr[j]` (where `j < i`).
    - If `arr[j]` is less than `arr[i]` and the sum of `arr[i]` and `msis[j]` is greater than `msis[i]`, update `msis[i]`.

4. **Result**: The maximum value in the `msis` array will be the result.

### Implementation

Here's a Python implementation with detailed documentation:

```python
def maximum_sum_increasing_subsequence(arr):
    """
    Function to find the maximum sum of an increasing subsequence in a given array.
    
    Parameters:
    arr (list of int): The input array of integers.
    
    Returns:
    int: The maximum sum of the increasing subsequence.
    """
    n = len(arr)
    
    # Initialize msis array where msis[i] will store the maximum sum of the increasing subsequence ending at index i
    msis = arr[:]  # Start with each element itself
    
    # Compute the MSIS values in a bottom-up manner
    for i in range(1, n):
        for j in range(i):
            # Check if arr[j] is less than arr[i] and msis[i] needs to be updated
            if arr[i] > arr[j] and msis[i] < msis[j] + arr[i]:
                msis[i] = msis[j] + arr[i]
    
    # The maximum value in msis[] is the maximum sum of increasing subsequence
    return max(msis)

# Example usage:
arr = [10, 5, 4, 3]
result = maximum_sum_increasing_subsequence(arr)
print("Maximum Sum of Increasing Subsequence is:", result)
```

### Explanation

- **Initialization**:
  ```python
  msis = arr[:]
  ```
  We initialize `msis` to be a copy of `arr` because the minimum sum for each element is the element itself.

- **Building the `msis` array**:
  ```python
  for i in range(1, n):
      for j in range(i):
          if arr[i] > arr[j] and msis[i] < msis[j] + arr[i]:
              msis[i] = msis[j] + arr[i]
  ```
  This double loop ensures that for each element `arr[i]`, we check all previous elements `arr[j]` to update `msis[i]` if `arr[j] < arr[i]` and adding `arr[i]` to the subsequence ending at `arr[j]` yields a larger sum.

- **Result**:
  ```python
  return max(msis)
  ```
  Finally, we return the maximum value in the `msis` array, which represents the maximum sum of any increasing subsequence in the array.

### Example

For the input array `[10, 5, 4, 3]`:

- `msis` starts as `[10, 5, 4, 3]`.
- After processing, `msis` remains `[10, 5, 4, 3]` because no increasing subsequences yield a higher sum than individual elements.

The output is `10`.

This solution efficiently computes the maximum sum increasing subsequence with a time complexity of \(O(n^2)\) and a space complexity of \(O(n)\).