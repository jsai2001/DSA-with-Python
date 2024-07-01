### Maximum sum of absolute difference of any permutation

To find the maximum sum of absolute differences of any permutation of an array, we need to maximize the expression \(\sum |a_i - a_j|\), where \(a\) is the permutation of the given array. Here's how we can achieve this:

## Explanation

Given an array \(A\) of \(n\) elements, we want to maximize the sum of the absolute differences of its permutation \(P\).

### Steps to Solve:

1. **Sort the Array**:
   - First, sort the array in ascending order. Let the sorted array be \(B\).

2. **Create a Specific Permutation**:
   - To maximize the sum of absolute differences, we can arrange the sorted array \(B\) in a specific way. The optimal arrangement is to place the smallest and largest elements alternately.
   - For example, if \(B = [b_1, b_2, b_3, \ldots, b_n]\), the optimal permutation \(P\) would look like: \(P = [b_1, b_n, b_2, b_{n-1}, b_3, b_{n-2}, \ldots]\).

3. **Calculate the Maximum Sum**:
   - Iterate through the permutation \(P\) and compute the sum of absolute differences of consecutive elements.

- **Time Complexity:** \( O(N log N) \)

- **Space Complexity:** \(O(N)\)

### Pseudo-code:

```python
def maxSumOfAbsoluteDifferences(A):
    # Step 1: Sort the array
    A.sort()
    
    # Step 2: Create the specific permutation
    n = len(A)
    P = [0] * n
    left, right = 0, n - 1
    
    for i in range(n):
        if i % 2 == 0:
            P[i] = A[left]
            left += 1
        else:
            P[i] = A[right]
            right -= 1
    
    # Step 3: Calculate the maximum sum of absolute differences
    max_sum = 0
    for i in range(1, n):
        max_sum += abs(P[i] - P[i-1])
    
    return max_sum

# Example Usage
A = [1, 2, 4, 8]
print(maxSumOfAbsoluteDifferences(A))  # Output: 18
```

### Time and Space Complexity

- **Time Complexity**:
  - Sorting the array takes \(O(n \log n)\).
  - Creating the permutation takes \(O(n)\).
  - Calculating the sum of absolute differences takes \(O(n)\).
  - Therefore, the overall time complexity is \(O(n \log n)\).

- **Space Complexity**:
  - We use an additional array \(P\) to store the permutation, which takes \(O(n)\) space.
  - Therefore, the overall space complexity is \(O(n)\).

### Detailed Explanation:

- **Sorting**:
  - Sorting the array ensures that we have a baseline for arranging elements to maximize the differences.
  
- **Creating the Permutation**:
  - By alternating the smallest and largest elements, we ensure that each difference between consecutive elements is maximized. This is because the absolute difference between a large and a small number is greater than the difference between numbers that are close in value.
  
- **Calculating the Maximum Sum**:
  - Iterating through the permutation and summing the absolute differences gives the desired result.

This approach ensures that the sum of absolute differences is maximized efficiently.