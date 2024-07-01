### Chocolate Distribution Problem

To solve this problem, we can use a greedy algorithm approach. The idea is to minimize the difference between the maximum and minimum number of chocolates given to the students. Here's a detailed step-by-step explanation:

### Algorithm Explanation

1. **Sort the Array:**
   - First, sort the array of chocolates. Sorting helps in easily finding the minimum difference by comparing adjacent elements.

2. **Find the Minimum Difference:**
   - After sorting, iterate through the array and consider each subarray of size `M`. Calculate the difference between the maximum and minimum chocolates in each subarray and keep track of the minimum difference encountered.

- **Time Complexity:** \( O(N log N) \)

- **Space Complexity:** \(O(1)\)

### Steps

1. **Input:**
   - Array `A` of size `N` containing the number of chocolates in each packet.
   - Integer `M` representing the number of students.

2. **Sorting:**
   - Sort the array `A`.

3. **Sliding Window:**
   - Initialize a variable `min_diff` to store the minimum difference. Set it to a large value initially.
   - Use a sliding window of size `M` to iterate through the sorted array and calculate the difference between the maximum and minimum chocolates in each window. Update `min_diff` if a smaller difference is found.

4. **Return Result:**
   - Return the minimum difference found.

### Implementation

```python
def find_min_diff(A, N, M):
    # Edge case: If there are no students or no chocolates
    if M == 0 or N == 0:
        return 0
    
    # Edge case: If there are fewer packets than students
    if N < M:
        return -1  # or some error code indicating invalid input
    
    # Step 1: Sort the array
    A.sort()
    
    # Step 2: Initialize the minimum difference as a large number
    min_diff = float('inf')
    
    # Step 3: Find the minimum difference by sliding a window of size M
    for i in range(N - M + 1):
        diff = A[i + M - 1] - A[i]
        if diff < min_diff:
            min_diff = diff
            
    return min_diff

# Example usage
A = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
N = len(A)
M = 7
result = find_min_diff(A, N, M)
print("The minimum difference is", result)
```

### Explanation of the Example

- **Input:** `A = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]`, `M = 7`
- **Sorted Array:** `A = [2, 4, 7, 9, 12, 23, 25, 28, 30, 30, 40, 41, 42, 43, 44, 48, 50]`
- **Sliding Window:**
  - Window [2, 4, 7, 9, 12, 23, 25] → Difference = 25 - 2 = 23
  - Window [4, 7, 9, 12, 23, 25, 28] → Difference = 28 - 4 = 24
  - ...
  - Window [25, 28, 30, 30, 40, 41, 42] → Difference = 42 - 25 = 17 (minimum found)
  - ...
  - Continue until the end of the array

### Time Complexity

- Sorting the array: \(O(N log N)\)
- Sliding window to find the minimum difference: \(O(N)\)

Overall time complexity: \(O(N log N)\)

### Space Complexity

- The space complexity is \(O(1)\) for the algorithm itself, not counting the input array.

This solution efficiently finds the minimum difference between the maximum and minimum chocolates given to the students.