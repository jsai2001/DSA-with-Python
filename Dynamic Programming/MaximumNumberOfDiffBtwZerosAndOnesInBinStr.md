## maximum difference between the number of 0s and the number of 1s

- Time Complexity: O(n)
- Space Complexity: O(1)

To solve the problem of finding the maximum difference between the number of 0s and the number of 1s (number of 0s – number of 1s) in the substrings of a binary string \( S \), we can use the concept of modifying the problem into a maximum subarray sum problem, which can be efficiently solved using Kadane's Algorithm.

Here's a step-by-step approach:

1. **Transform the Binary String**: Convert the binary string into an array of integers where 0 is replaced with +1 and 1 is replaced with -1. This transformation helps us convert the problem into finding the maximum sum subarray in this new array. Specifically:
   - Replace each '0' with +1 (because a '0' contributes positively to the difference).
   - Replace each '1' with -1 (because a '1' contributes negatively to the difference).

2. **Apply Kadane's Algorithm**: Use Kadane's Algorithm to find the maximum sum subarray in the transformed array. Kadane's Algorithm works as follows:
   - Initialize `max_so_far` and `max_ending_here` to the first element of the transformed array.
   - Iterate through the array, updating `max_ending_here` as the maximum of the current element or the sum of `max_ending_here` and the current element.
   - Update `max_so_far` to be the maximum of `max_so_far` and `max_ending_here`.

3. **Handle Special Case**: If the original string consists entirely of '1's, the transformed array will contain only -1s, and the maximum sum subarray will be -1. Thus, if the maximum sum is negative, return -1 as specified.

### Implementation

Here's the Python implementation of the described approach:

```python
def max_difference(S):
    # Transform the string: 0 -> +1, 1 -> -1
    transformed = [1 if char == '0' else -1 for char in S]
    
    # Implement Kadane's Algorithm to find the maximum sum subarray
    max_ending_here = transformed[0]
    max_so_far = transformed[0]
    
    for x in transformed[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    
    # If the maximum sum subarray is negative, it means all 1s case
    return max_so_far if max_so_far > 0 else -1

# Example usage:
S = "11000111101010111"
print(max_difference(S))  # Output: 3
```

### Explanation

- The transformation of the string converts it into an array of integers.
- Applying Kadane's Algorithm helps find the maximum difference of 0s and 1s in any substring by identifying the maximum sum subarray.
- The check for a negative maximum sum helps handle the edge case where the string contains only '1's.

This solution efficiently computes the desired result with a time complexity of \( O(n) \), where \( n \) is the length of the binary string \( S \).