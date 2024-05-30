To solve the problem of finding the minimum number of jumps needed to reach the end of an array optimally, we can use a greedy algorithm. Let's break down the solution step-by-step with a clear explanation:

### Problem Statement
Given an array of integers where each element represents the maximum number of steps that can be jumped forward from that element, find the minimum number of jumps needed to reach the end of the array starting from the first element.

### Example
Input: `[2, 3, 1, 1, 4]`
Output: `2`

Explanation: The minimum number of jumps to reach the last index is `2`. Jump `1` step from index `0` to `index 1`, then `3` steps to the last index.

### Steps to Solve the Problem

1. **Initialize variables**:
   - `jumps`: to store the minimum number of jumps needed to reach the end.
   - `current_end`: the farthest point that can be reached with the current number of jumps.
   - `farthest`: the farthest point that can be reached with the next jump.

2. **Iterate through the array**:
   - Update `farthest` with the maximum index that can be reached from the current index.
   - If the current index reaches `current_end`, it means we need to make another jump to move forward, so increment `jumps` and update `current_end` to `farthest`.

3. **Check for edge cases**:
   - If the array length is `1`, no jumps are needed since we are already at the end.
   - If the first element is `0`, it's not possible to move forward, hence return `-1` or an appropriate message indicating it's not possible to reach the end.

### Algorithm Implementation

Here's the Python implementation of the described algorithm:

```python
def min_jumps(arr):
    n = len(arr)
    if n == 1:
        return 0  # Already at the end
    if arr[0] == 0:
        return -1  # Can't move anywhere

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):  # No need to jump from the last element
        farthest = max(farthest, i + arr[i])
        
        # If we have reached the end of what we can reach with current jumps
        if i == current_end:
            jumps += 1
            current_end = farthest

            # If we have reached or passed the last index
            if current_end >= n - 1:
                break
    
    # If we are still within the loop and have not reached the end
    if current_end < n - 1:
        return -1  # It's not possible to reach the end
    
    return jumps

# Test the function with the example
arr = [2, 3, 1, 1, 4]
print("Minimum number of jumps:", min_jumps(arr))
```

### Explanation of the Code
1. **Initialization**: The variables `jumps`, `current_end`, and `farthest` are initialized. `jumps` counts the number of jumps taken, `current_end` is the farthest point reachable with the current jumps, and `farthest` tracks the farthest point that can be reached in the next step.
2. **Loop through the array**: We iterate through the array up to the second-to-last element (because we don't need to jump from the last element). For each index, we update `farthest`.
3. **Update jumps**: When we reach `current_end`, we increment the jump count and update `current_end` to `farthest`.
4. **Check reachability**: If during the loop, `current_end` surpasses or reaches the end of the array, we break out of the loop.
5. **Return result**: If after the loop, `current_end` hasn't reached the end, it means it's not possible to reach the end, so we return `-1`. Otherwise, we return the number of jumps.

This solution ensures we find the minimum number of jumps in an optimal way, with a time complexity of \(O(n)\) and space complexity of \(O(1)\).