### Maximize the sum of arr[i]*i

To solve the problem of finding the maximum value of ∑arr[i]*i, where \( i = 0, 1, 2, ..., n-1 \), given that we can rearrange the elements of the array, we need to strategically arrange the elements in a way that maximizes the sum.

## Solution Explanation

### Key Insight

To maximize the sum of \( \sum arr[i] * i \), we need to place larger values in positions with higher indices. The reason for this is that multiplying larger values by larger indices will yield a greater sum. Therefore, we should sort the array in ascending order and then compute the sum.

- **Time Complexity:** \( O(N log N) \)

- **Space Complexity:** \(O(1)\)

### Steps

1. **Sort the array** in ascending order.
2. **Compute the sum** using the formula \( \sum arr[i] * i \).
3. **Return the result modulo \( 10^9 + 7 \)** to handle large numbers.

### Detailed Algorithm

1. **Sort the Array:**
   - Sort the array in non-decreasing order.
   
2. **Calculate the Sum:**
   - Initialize a variable `result` to 0.
   - Iterate through the sorted array and for each element at index \( i \), add \( arr[i] * i \) to `result`.
   
3. **Apply Modulo Operation:**
   - Since the result can be large, take the modulo \( 10^9 + 7 \) of the result to prevent overflow.

### Example

Let's go through a small example to illustrate the steps:

- Input array: \( [3, 5, 6, 1] \)
- Step 1: Sort the array: \( [1, 3, 5, 6] \)
- Step 2: Calculate the sum:
  - \( 1*0 + 3*1 + 5*2 + 6*3 \)
  - \( = 0 + 3 + 10 + 18 \)
  - \( = 31 \)
- Step 3: Apply modulo \( 10^9 + 7 \):
  - Since 31 is less than \( 10^9 + 7 \), the result is 31.

### Time and Space Complexity

- **Time Complexity:**
  - Sorting the array takes \( O(N log N) \).
  - Calculating the sum takes \( O(N) \).
  - Overall, the time complexity is \( O(N log N) \).

- **Space Complexity:**
  - The space complexity is \( O(1) \) for the sorting algorithm if done in-place, plus \( O(1) \) for the additional variables used, making it overall \( O(1) \).

### Python Code

```python
def max_sum(arr):
    MOD = 10**9 + 7
    arr.sort()
    result = 0
    n = len(arr)
    
    for i in range(n):
        result = (result + arr[i] * i) % MOD
    
    return result

# Example usage:
arr = [3, 5, 6, 1]
print(max_sum(arr))  # Output: 31
```

This function `max_sum` sorts the input array, computes the sum as described, and returns the result modulo \( 10^9 + 7 \). This ensures the solution is both efficient and handles large numbers correctly.