### Maximize array sum after K negations

To solve this problem, the goal is to maximize the sum of the array after performing exactly \( K \) modifications where each modification can flip the sign of an array element. Let's break down the approach step-by-step:

### Approach

1. **Sort the Array**: Start by sorting the array in ascending order. This will help in efficiently finding the smallest element to flip.
2. **Flip the Smallest Elements**: To maximize the sum, we should aim to flip the smallest (most negative) elements first. If the element is negative, flipping it will turn it positive, thereby increasing the sum significantly.
3. **Post-Flipping Adjustments**: After \( K \) flips, if \( K \) is greater than the number of negative elements, we need to flip some positive elements. If \( K \) is even, the result is straightforward as flipping an element twice brings it back to its original value. If \( K \) is odd, we need to flip the smallest element again after making all possible beneficial flips.
4. **Edge Cases**: If \( K \) is very large, we need to handle the cases where we might flip elements multiple times by leveraging the modulo operation.

- **Time Complexity:** \( O(N log N) \)

- **Space Complexity:** \(O(1)\)

### Detailed Steps

1. **Sort the Array**:
    ```python
    arr.sort()
    ```

2. **Flip the Smallest Elements**:
    Iterate through the array and flip the negative elements until \( K \) is exhausted or there are no more negative elements left.
    ```python
    for i in range(len(arr)):
        if arr[i] < 0 and K > 0:
            arr[i] = -arr[i]
            K -= 1
    ```

3. **Post-Flipping Adjustments**:
    After flipping the smallest negative elements, if \( K \) is still greater than zero:
    - If \( K \) is odd, flip the smallest element in the array (which might be the smallest positive element now).
    - If \( K \) is even, do nothing as flipping twice cancels out.

    ```python
    if K > 0 and K % 2 == 1:
        arr.sort()  # Re-sort to find the new smallest element
        arr[0] = -arr[0]  # Flip the smallest element
    ```

4. **Calculate the Sum**:
    ```python
    max_sum = sum(arr)
    ```

### Time and Space Complexity

- **Time Complexity**: \( O(N log N) \)
    - Sorting the array takes \( O(N log N) \).
    - The subsequent iteration through the array takes \( O(N) \).
    - Sorting again (if needed) takes \( O(N log N) \).

- **Space Complexity**: \( O(1) \) (excluding the space for input array).
    - We are modifying the array in place, so no additional space proportional to input size is required.

### Complete Solution Code

Here is the complete Python code to solve the problem:

```python
def maximize_sum(arr, K):
    # Sort the array
    arr.sort()
    
    # Flip the smallest (most negative) elements first
    for i in range(len(arr)):
        if arr[i] < 0 and K > 0:
            arr[i] = -arr[i]
            K -= 1

    # If K is still greater than 0 and is odd, flip the smallest element again
    if K > 0 and K % 2 == 1:
        arr.sort()  # Re-sort the array to find the new smallest element
        arr[0] = -arr[0]

    # Return the maximum sum
    return sum(arr)

# Example Usage
arr = [-2, 0, 5, -1, 2]
K = 3
print("Maximum sum after K modifications:", maximize_sum(arr, K))  # Output should be 10
```

This approach ensures that the sum of the array is maximized after exactly \( K \) modifications, handling all edge cases efficiently.