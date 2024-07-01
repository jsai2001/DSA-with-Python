### Maximize sum of consecutive differences in a circular array

To solve the problem of finding the maximum sum of the absolute difference between consecutive elements in a circular array, we need to maximize the expression \(|a_1 - a_2| + |a_2 - a_3| + \ldots + |a_{n-1} - a_n| + |a_n - a_1|\).

- **Time Complexity:** \( O(N log N) \)

- **Space Complexity:** \(O(N)\)

### Detailed Explanation

1. **Understanding the problem**:
   - We have an array `a` of size `N`.
   - The array is circular, meaning the element after `a[N-1]` is `a[0]`.
   - We can rearrange the elements to maximize the sum of the absolute differences between consecutive elements, including the circular difference.

2. **Optimal Strategy**:
   - To maximize the sum of absolute differences, we need to arrange the elements such that the differences between consecutive elements are as large as possible.
   - A useful approach is to sort the array and then arrange the elements by alternating between the smallest and largest available elements.

3. **Algorithm**:
   - Sort the array `a`.
   - Create a new array `b` where we place the smallest available element, then the largest, then the second smallest, then the second largest, and so on.
   - This arrangement ensures that each pair of consecutive elements in `b` has a large absolute difference.

### Steps:

1. Sort the array `a`.
2. Create two pointers: one starting at the beginning of the sorted array and the other at the end.
3. Construct the new array `b` by alternately picking elements from the start and end.
4. Calculate the sum of the absolute differences for this arrangement.

### Time Complexity
- Sorting the array takes \(O(N \log N)\).
- Constructing the new array and calculating the sum takes \(O(N)\).
- Therefore, the overall time complexity is \(O(N \log N)\).

### Space Complexity
- The space complexity is \(O(N)\) because we need an extra array to store the rearranged elements.

### Implementation

```python
def max_absolute_difference(arr):
    n = len(arr)
    arr.sort()
    
    # Create a new array to hold the rearranged elements
    b = [0] * n
    
    # Fill the new array in alternating fashion
    left = 0
    right = n - 1
    for i in range(n):
        if i % 2 == 0:
            b[i] = arr[left]
            left += 1
        else:
            b[i] = arr[right]
            right -= 1
            
    # Calculate the sum of absolute differences
    max_sum = 0
    for i in range(1, n):
        max_sum += abs(b[i] - b[i - 1])
    max_sum += abs(b[0] - b[n - 1])  # Include the circular part
    
    return max_sum

# Example usage
arr = [1, 2, 4, 8]
print(max_absolute_difference(arr))  # Output should be 18
```

### Explanation of Example:
For an input array `[1, 2, 4, 8]`:
1. Sorted array is `[1, 2, 4, 8]`.
2. The rearranged array `b` could be `[1, 8, 2, 4]` or `[8, 1, 4, 2]` (both give the same result in terms of maximum sum).
3. Calculate the sum of absolute differences:
   - For `[1, 8, 2, 4]`: 
     \[
     |1 - 8| + |8 - 2| + |2 - 4| + |4 - 1| = 7 + 6 + 2 + 3 = 18
     \]

Thus, the maximum sum of absolute differences for the given example is 18.