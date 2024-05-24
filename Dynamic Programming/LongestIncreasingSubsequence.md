## Longest Increasing Subsequence

### Dynamic Programming Approch

Time Complexity: (O(n^2))

Space Complexity: (O(n))

### Binary Search Approch

Time Complexity (O(n log n))

Space Complexity (O(n))

### Dynamic Programming Approch

This approach is efficient and avoids recursion overhead. Here's the code:

```python
def longest_increasing_subsequence(arr):
  """
  This function finds the length of the longest increasing subsequence in an array.

  Args:
      arr: The input array.

  Returns:
      The length of the longest increasing subsequence.
  """
  n = len(arr)
  lis = [1] * n  # Create a list to store LIS lengths

  # Iterate through the array and compare with previous elements
  for i in range(1, n):
    for j in range(i):
      if arr[i] > arr[j] and lis[i] < lis[j] + 1:
        lis[i] = lis[j] + 1

  # Maximum value in lis represents LIS length
  return max(lis)

# Example usage
arr = [10, 9, 2, 5, 1, 7, 101, 18]
length = longest_increasing_subsequence(arr)
print("Length of LIS is", length)
```

The dynamic programming approach is generally preferred due to its efficiency for larger inputs.

Important Line:

This line in the longest increasing subsequence (LIS) code snippet is crucial for determining the length of the LIS at a particular index (`i`) in the input array (`arr`). Let's break it down:

- **`arr[i] > arr[j]`**: This condition checks if the element at the current index (`i`) is greater than the element at the previous index (`j`). Essentially, it ensures we're only considering increasing subsequences.

- **`lis[i] < lis[j] + 1`**: Here, `lis` is an array that stores the lengths of LIS ending at each index up to that point. This condition checks if the current length of the LIS ending at `i` (`lis[i]`) is less than the length of the LIS ending at `j` (`lis[j]`) plus 1.

Why is this check important?

Imagine we're iterating through the array, and we've reached index `i`. We want to find the longest increasing subsequence ending at `i`. The loop iterates through previous elements (`j`) to see if including `arr[i]` would create a longer subsequence.

- If `arr[i]` is greater than `arr[j]`, then including `arr[i]` in the subsequence ending at `j` might potentially lead to a longer sequence.

- However, the `lis[i] < lis[j] + 1` check ensures we only update `lis[i]` if including `arr[i]` would actually create a longer subsequence. Here's why:

  - If `lis[i]` is already equal to `lis[j] + 1`, it means there already exists an LIS ending at `i` with the same length as the potential sequence formed by including `arr[i]` after the LIS ending at `j`. No need to update `lis[i]` in this case.

  - If `lis[i]` is greater than `lis[j] + 1`, it means there's already a longer increasing subsequence ending at `i` identified previously. Again, no update is needed.

In summary, this line ensures we only update the length of the LIS at index `i` if including the current element (`arr[i]`) would genuinely extend a previously identified increasing subsequence. This helps build the `lis` array efficiently, ultimately leading to the length of the overall LIS in the array.

Time Complexity (O(n^2))

The code uses two nested loops:

An outer loop iterates through the array arr from index 1 to n-1 (n elements).
Within the outer loop, an inner loop iterates through the elements before the current index i (j goes from 0 to i-1). In the worst case, this inner loop runs for all elements visited so far (n elements in the worst case).
The total number of comparisons and updates happening within the nested loops is proportional to n * n, resulting in a time complexity of O(n^2).

Space Complexity (O(n))

The code utilizes an auxiliary array lis to store the lengths of LIS ending at each index. This array has a size of n.
Other space requirements like variables and function call stack are negligible compared to n.

### Binary Search Approch

Finding the longest increasing subsequence (LIS) using a binary search approach in Python:

```python
def longest_increasing_subsequence_binary_search(arr):
  """
  This function finds the length of the longest increasing subsequence in an array
  using binary search.

  Args:
      arr: The input array.

  Returns:
      The length of the longest increasing subsequence.
  """
  n = len(arr)
  # Initialize a list with the first element as the LIS (length 1)
  tail = [arr[0]]

  for i in range(1, n):
    # Binary search to find the insertion position for arr[i]
    # (guarantees a sorted increasing sequence)
    insertion_index = binary_search(tail, arr[i])

    # If insertion_index is equal to the length of tail, it means arr[i] is
    # greater than all elements in tail. We can append directly.
    if insertion_index == len(tail):
      tail.append(arr[i])
    # Otherwise, update the element at insertion_index with arr[i]
    else:
      tail[insertion_index] = arr[i]

  return len(tail)

def binary_search(arr, target):
  """
  This function performs a binary search on a sorted array.

  Args:
      arr: The sorted array to search.
      target: The element to search for.

  Returns:
      The index where the target element should be inserted to maintain order.
  """
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  # If target is not found, return the insertion index based on the last comparison
  return low

# Example usage
arr = [10, 9, 2, 5, 1, 7, 101, 18]
length = longest_increasing_subsequence_binary_search(arr)
print("Length of LIS is", length)
```

**Explanation:**

1. We maintain a list `tail` that represents the current increasing subsequence. Initially, it contains only the first element of the input array.

2. We iterate through the remaining elements (`arr[1]` to `arr[n-1]`).

3. For each element `arr[i]`:
   - We perform a binary search on the `tail` list to find the appropriate insertion position for `arr[i]` that maintains the increasing order.

   - If the binary search returns the length of `tail` (meaning `arr[i]` is greater than all elements in `tail`), we simply append `arr[i]` to the end.

   - Otherwise, we update the element at the insertion index with `arr[i]`, effectively replacing a smaller element with a larger one to maintain the increasing order.

4. After processing all elements, the length of the `tail` list represents the length of the longest increasing subsequence in the original array.

The binary search within the loop helps us efficiently find the insertion position for each element, leading to a time complexity of O(n log n). This approach is generally faster than the nested loop approach (O(n^2)) for larger inputs.

=============================================
Here's a breakdown of the logic:

1. **`insertion_index == len(tail)`**: This condition occurs when the binary search on `tail` doesn't find an existing element greater than or equal to `arr[i]`. This implies `arr[i]` is larger than all elements in `tail` so far.

- **Action:** Since `arr[i]` can be appended to maintain the increasing order, we simply add it to the end of `tail`. This effectively extends the current increasing subsequence.

2. **`insertion_index != len(tail)`**: This condition happens when the binary search finds an element in `tail` that's greater than `arr[i]`. This doesn't necessarily mean the entire `tail` is not sorted. It simply means `arr[i]` doesn't fit seamlessly at the end of the current increasing subsequence.

- **Action:** We update the element at `insertion_index` with `arr[i]`. This essentially replaces a smaller element in the current increasing subsequence with a larger one, maintaining the increasing order. The `tail` list remains an increasing subsequence but might not be fully sorted yet.

**Key Point:**

The `tail` list is constantly evolving as we process elements. It doesn't represent a fixed sorted sequence but rather the **longest increasing subsequence we've identified so far**. The binary search helps us efficiently find the insertion point within this growing increasing subsequence for each new element we encounter.

**Example:**

Consider the array `[2, 5, 10, 7]`:

**1. Initialization:**

- We begin with an empty `tail` list, which will represent the current increasing subsequence. So, initially, `tail = []`.

**2. Processing elements:**

- **`arr[0] = 2`**:
   - Since `tail` is empty, any element is a valid increasing subsequence. We directly append `2` to `tail`, making it `[2]`.

- **`arr[1] = 5`**:
   - We perform a binary search on `tail` (which is just `[2]`). Since `5` is greater than the only element in `tail`, the binary search would return the length of `tail` (which is 1 in this case).
   - This indicates `insertion_index == len(tail)`. Following the code, we append `5` to `tail`, resulting in `tail = [2, 5]`.

- **`arr[2] = 10`**:
   - Binary search on `tail = [2, 5]` finds that `10` is greater than both elements. Again, `insertion_index == len(tail)`.
   - We append `10` to `tail`, making it `tail = [2, 5, 10]`.

- **`arr[3] = 7`**:
   - Binary search on `tail = [2, 5, 10]` finds that `7` is greater than `2` but not `10`. So, `insertion_index` wouldn't be equal to `len(tail)`.
   - The code locates the insertion point at index 2 (between `5` and `10`). We update `tail[2]` with `7`, resulting in `tail = [2, 5, 7]`.

**Key points to remember:**

- `tail` represents the current increasing subsequence we're building, not necessarily a fully sorted list.
- `insertion_index == len(tail)` indicates `arr[i]` is larger than all elements in `tail` so far, allowing us to simply append it.
- `insertion_index != len(tail)` means `arr[i]` fits within the existing increasing order but not at the end. We replace a smaller element with `arr[i]` to maintain the increasing property.

**End result:**

After processing all elements, `tail = [2, 5, 7]` represents the longest increasing subsequence in the array, which is `[2, 5, 7]`.

**In conclusion:**

The binary search approach efficiently finds the insertion point for each element in the `tail` list, ensuring we maintain an increasing subsequence while considering the element's position relative to the existing elements. This helps us build the final LIS efficiently.

Time Complexity (O(n log n))

The code performs a binary search within the loop to find the insertion position for each element. A binary search on a sorted list has a time complexity of O(log n).
The loop iterates through the entire array (n elements).
However, the key factor is that the binary search is performed within the loop. Although each binary search itself is O(log n), the total number of binary searches becomes proportional to the number of elements (n). This leads to an overall time complexity of O(n * log n), which can be simplified to O(n log n).

Space Complexity (O(n))

The code utilizes an auxiliary list (tail) to store the current increasing subsequence. This list grows as we process elements and ultimately stores the LIS. In the worst case, the length of tail can be equal to the length of the input array (n).
Other space requirements like variables and function call stack are negligible compared to n.
