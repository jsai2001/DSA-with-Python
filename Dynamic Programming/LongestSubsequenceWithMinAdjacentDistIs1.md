### Longest subsequence in an array where the difference between adjacent elements is one

**Time Complexity:** 

    Dual for loop approch O(n^2)

    Single Loop with Hashmap approch O(n)

**Space Complexity:** O(n)

To find the longest subsequence in an array where the difference between adjacent elements is one, we can use dynamic programming. Here's a step-by-step approach to solve this problem:

1. **Define the Problem**: We need to find the length of the longest subsequence where the absolute difference between consecutive elements is exactly 1.

2. **Dynamic Programming Array**: We use an array `dp` where `dp[i]` represents the length of the longest subsequence ending at index `i`.

3. **Initialize DP Array**: Initialize each element of `dp` to 1 since the minimum length of any subsequence ending at any element is 1 (the element itself).

4. **Fill the DP Array**: For each element in the array, check all previous elements to see if the difference between the current element and the previous element is 1. If it is, update the `dp[i]` value accordingly.

5. **Compute the Result**: The maximum value in the `dp` array will be the length of the longest subsequence.

Here's the Python code implementing the above steps:

```python
def longest_subsequence(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    # Initialize dp array
    dp = [1] * n
    
    # Fill dp array
    for i in range(1, n):
        for j in range(i):
            if abs(arr[i] - arr[j]) == 1:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Find the maximum value in dp array
    return max(dp)

# Example usage
arr = [1, 2, 3, 4, 2, 3, 5, 6, 7]
print(f"Length of the longest subsequence: {longest_subsequence(arr)}")
```

### Explanation:
- **Initialization**: Each element in `dp` is initialized to 1.
- **Filling DP Array**: For each element `arr[i]`, we check all previous elements `arr[j]` (where `j < i`). If the absolute difference between `arr[i]` and `arr[j]` is 1, we update `dp[i]` as `dp[i] = max(dp[i], dp[j] + 1)`.
- **Result**: The length of the longest subsequence is the maximum value in the `dp` array.

### Complexity:
- **Time Complexity**: \(O(n^2)\) due to the nested loops.
- **Space Complexity**: \(O(n)\) for the `dp` array.

Yes, we can solve this problem in \( O(n) \) time complexity using a combination of dynamic programming and hash maps.

Here's the optimized approach:

1. **Use a Dictionary**: We'll use a dictionary to store the length of the longest subsequence ending with each element.

2. **Iterate Through the Array**: For each element in the array, we'll check the lengths of subsequences ending with `element - 1` and `element + 1`. We'll then update the current element's subsequence length based on these values.

3. **Compute the Result**: Track the maximum length of the subsequences during the iteration.

Here's the Python code implementing this optimized approach:

```python
def longest_subsequence(arr):
    if not arr:
        return 0

    # Dictionary to store the length of the longest subsequence ending with each element
    dp = {}
    max_length = 1

    for num in arr:
        # Calculate the longest subsequence length ending at `num`
        # Check if `num - 1` and `num + 1` are in dp
        if num - 1 in dp and num + 1 in dp:
            dp[num] = max(dp[num - 1], dp[num + 1]) + 1
        elif num - 1 in dp:
            dp[num] = dp[num - 1] + 1
        elif num + 1 in dp:
            dp[num] = dp[num + 1] + 1
        else:
            dp[num] = 1

        # Update the maximum length
        max_length = max(max_length, dp[num])

    return max_length

# Example usage
arr = [1, 2, 3, 4, 2, 3, 5, 6, 7]
print(f"Length of the longest subsequence: {longest_subsequence(arr)}")
```

### Explanation:
- **Dictionary Initialization**: `dp` is a dictionary that will map each element to the length of the longest subsequence ending with that element.
- **Iterate and Update**: For each number in the array, we:
  - Check if `num - 1` or `num + 1` is present in the dictionary `dp`.
  - Update the current element's subsequence length based on the values of `dp[num - 1]` and `dp[num + 1]`.
  - If neither `num - 1` nor `num + 1` is present, the subsequence length ending at the current element is 1.
- **Update Maximum Length**: During each iteration, update the maximum length encountered.

### Complexity:
- **Time Complexity**: \( O(n) \), where `n` is the number of elements in the array. Each element is processed in constant time due to dictionary operations.
- **Space Complexity**: \( O(n) \), for storing the lengths of the subsequences in the dictionary.

This approach ensures we efficiently find the longest subsequence where the difference between adjacent elements is one, in linear time.