### Kadane's Algorithm

- Time Complexity: O(n)

- Space Complexity: O(1)

### Problem Statement:
We are given an array `Arr` of `N` integers. Our task is to find the contiguous sub-array (which must contain at least one element) that has the maximum sum, and then return this maximum sum.

### Approach:
To solve this problem, we can use the Kadane's algorithm, which is a dynamic programming approach.

#### Kadane's Algorithm:
1. Initialize two variables:
   - `max_so_far` to store the maximum sum found so far.
   - `max_ending_here` to store the maximum sum of subarray ending at the current position.

2. Iterate through the array:
   - For each element in the array, update `max_ending_here`:
     - Set `max_ending_here` to the maximum of the current element or the sum of the current element and the previous `max_ending_here`.
   - Update `max_so_far` if `max_ending_here` is greater.

3. Finally, return `max_so_far`.

### Pseudocode:
```
Kadane's Algorithm(Arr):
    max_so_far = Arr[0]
    max_ending_here = Arr[0]
    
    for i from 1 to length(Arr) - 1:
        max_ending_here = max(Arr[i], max_ending_here + Arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
```

### Time Complexity:
The time complexity of Kadane's algorithm is O(n), where n is the size of the input array. This is because we iterate through the array only once.

### Space Complexity:
The space complexity of Kadane's algorithm is O(1), as we are using only a constant amount of extra space for storing variables `max_so_far` and `max_ending_here`.

### Example:
Let's consider an array `Arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`.

Applying Kadane's algorithm:
```
max_so_far = -2
max_ending_here = -2

For i = 1, Arr[i] = 1
max_ending_here = max(1, -2 + 1) = 1
max_so_far = max(-2, 1) = 1

For i = 2, Arr[i] = -3
max_ending_here = max(-3, 1 - 3) = -2
max_so_far = max(1, -2) = 1

For i = 3, Arr[i] = 4
max_ending_here = max(4, -2 + 4) = 4
max_so_far = max(1, 4) = 4

For i = 4, Arr[i] = -1
max_ending_here = max(-1, 4 - 1) = 3
max_so_far = max(4, 3) = 4

For i = 5, Arr[i] = 2
max_ending_here = max(2, 3 + 2) = 5
max_so_far = max(4, 5) = 5

For i = 6, Arr[i] = 1
max_ending_here = max(1, 5 + 1) = 6
max_so_far = max(5, 6) = 6

For i = 7, Arr[i] = -5
max_ending_here = max(-5, 6 - 5) = 1
max_so_far = max(6, 1) = 6

For i = 8, Arr[i] = 4
max_ending_here = max(4, 1 + 4) = 5
max_so_far = max(6, 5) = 6

Return 6
```

Hence, the maximum sum of a contiguous sub-array in `Arr` is 6.

Sure, here's the Python code implementing Kadane's algorithm:

```python
def max_subarray_sum(arr):
    max_so_far = arr[0]  # Initialize max_so_far with the first element of the array
    max_ending_here = arr[0]  # Initialize max_ending_here with the first element of the array
    
    # Loop through the array starting from the second element
    for i in range(1, len(arr)):
        # Calculate the maximum sum ending at the current position
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        
        # Update max_so_far if the maximum sum ending at the current position is greater
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum sum of a contiguous sub-array:", max_subarray_sum(arr))
```

This code will output:

```
Maximum sum of a contiguous sub-array: 6
```

This function `max_subarray_sum` takes an array as input and returns the maximum sum of a contiguous sub-array using Kadane's algorithm.