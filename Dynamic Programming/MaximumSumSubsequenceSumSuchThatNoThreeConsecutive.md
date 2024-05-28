To solve the problem of finding the maximum subsequence sum such that no three elements are consecutive, we can use dynamic programming. Let's define the problem and then outline the steps to solve it.

### Problem Definition
Given an array `arr` of length `n`, we need to find the maximum sum of a subsequence such that no three elements are consecutive.

Time Complexity: O(n)
Space Complexity: O(n)

### Dynamic Programming Approach

#### Step-by-Step Solution

1. **Base Cases:**
    - If the array has no elements (`n == 0`), the maximum sum is 0.
    - If there is one element (`n == 1`), the maximum sum is the value of that element.
    - If there are two elements (`n == 2`), the maximum sum is the sum of both elements.
    - If there are three elements (`n == 3`), the maximum sum is the maximum of:
        - Sum of all three elements.
        - Sum of the first two elements.
        - Sum of the last two elements.

2. **Recursive Case:**
    - For an array with more than three elements, define `sum[i]` as the maximum sum of a subsequence of the first `i` elements such that no three elements are consecutive. We can write the relation:
      \[
      sum[i] = \max(sum[i-1], sum[i-2] + arr[i-1], sum[i-3] + arr[i-1] + arr[i-2])
      \]
      Here, the three cases represent:
        - Not including the `i-th` element.
        - Including the `i-th` element but not the `(i-1)-th`.
        - Including the `i-th` and `(i-1)-th` elements but not the `(i-2)-th`.

3. **Initialization:**
    - Initialize `sum[0] = 0` (no elements to choose from).
    - Initialize `sum[1] = arr[0]` (only one element).
    - Initialize `sum[2] = arr[0] + arr[1]` (two elements).
    - Initialize `sum[3] = max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])` (three elements).

4. **Compute sum array:**
    - Use a loop to fill the `sum` array from `sum[4]` to `sum[n]` using the relation defined above.

5. **Result:**
    - The result will be `sum[n]`.

Here’s the implementation of the above approach in Python:

```python
def max_sum_no_three_consecutive(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0] + arr[1]
    if n == 3:
        return max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])
    
    sum = [0] * (n + 1)
    sum[1] = arr[0]
    sum[2] = arr[0] + arr[1]
    sum[3] = max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])
    
    # Process rest of the elements
    # We have three cases
    # 1) Exclude arr[i], i.e., sum[i] = sum[i-1]
    # 2) Exclude arr[i-1], i.e., sum[i] = sum[i-2] + arr[i]
    # 3) Exclude arr[i-2], i.e., sum[i-3] + arr[i] + arr[i-1]
    for i in range(4, n + 1):
        sum[i] = max(sum[i-1], sum[i-2] + arr[i-1], sum[i-3] + arr[i-1] + arr[i-2])
    
    return sum[n]

# Example usage
arr = [3, 2, 5, 10, 7]
print(max_sum_no_three_consecutive(arr))  # Output should be 15 (3 + 5 + 7)
```

### Explanation of the Example
For the array `[3, 2, 5, 10, 7]`:
- If we take elements `3, 5, and 7`, the sum is \(3 + 5 + 7 = 15\), which is the maximum sum of a subsequence where no three elements are consecutive.

Certainly! The line

\[ \text{max}(sum[i-1], sum[i-2] + arr[i-1], sum[i-3] + arr[i-1] + arr[i-2]) \]

is crucial in our dynamic programming approach. It computes the maximum sum of a subsequence up to the \(i\)-th element such that no three elements are consecutive. Let's break down the three cases considered by this line:

1. **\( sum[i-1] \) (Excluding the \(i\)-th element):**
    - This term represents the maximum sum we can obtain by not including the \(i\)-th element at all. Essentially, we rely on the maximum sum calculated for the first \(i-1\) elements.
    - **Reasoning:** If we exclude the current element \(arr[i-1]\), the best sum we can have is the one calculated up to the previous element.

2. **\( sum[i-2] + arr[i-1] \) (Including the \(i\)-th element, but not the \((i-1)\)-th element):**
    - This term represents the maximum sum we can obtain by including the \(i\)-th element \(arr[i-1]\) but excluding the \((i-1)\)-th element.
    - **Reasoning:** If we include the current element \(arr[i-1]\), then to avoid including three consecutive elements, we must exclude the \((i-1)\)-th element. Therefore, we add the current element to the maximum sum we can obtain up to the first \(i-2\) elements.

3. **\( sum[i-3] + arr[i-1] + arr[i-2] \) (Including the \(i\)-th and \((i-1)\)-th elements, but not the \((i-2)\)-th element):**
    - This term represents the maximum sum we can obtain by including the \(i\)-th element \(arr[i-1]\) and the \((i-1)\)-th element \(arr[i-2]\) but excluding the \((i-2)\)-th element.
    - **Reasoning:** If we include both the current element \(arr[i-1]\) and the previous element \(arr[i-2]\), then to avoid three consecutive elements, we must exclude the \((i-2)\)-th element. Therefore, we add both \(arr[i-1]\) and \(arr[i-2]\) to the maximum sum we can obtain up to the first \(i-3\) elements.

### Putting It Together

When computing \( sum[i] \):

- We take the maximum value among the three scenarios described above.
- This ensures that the subsequence sum we consider is maximized while respecting the constraint that no three elements are consecutive.

### Example Walkthrough

Let's take a small example array `[3, 2, 5, 10, 7]` and see how this works for \(i = 4\) (considering 1-based index for explanation):

- \( sum[3] \) will have the maximum sum for the first three elements, considering no three elements are consecutive.
- \( sum[2] \) will have the maximum sum for the first two elements.
- \( sum[1] \) will have the maximum sum for the first element.

Now, for \(i = 4\):

\[ sum[4] = \text{max}(sum[3], sum[2] + arr[3], sum[1] + arr[3] + arr[2]) \]

Substitute the values:

- \( sum[3] \): Maximum sum for first three elements.
- \( sum[2] \): Maximum sum for first two elements.
- \( sum[1] \): Maximum sum for first element.
- \( arr[3] \): 10 (4th element in 0-based index array).
- \( arr[2] \): 5 (3rd element in 0-based index array).

Thus:

\[ sum[4] = \text{max}(sum[3], sum[2] + 10, sum[1] + 10 + 5) \]

By evaluating these values, we get the maximum sum that includes the 4th element but no three consecutive elements.

### Conclusion

This line effectively ensures that each state \( sum[i] \) captures the maximum possible subsequence sum up to the \(i\)-th element while enforcing the constraint that no three elements in the subsequence are consecutive.