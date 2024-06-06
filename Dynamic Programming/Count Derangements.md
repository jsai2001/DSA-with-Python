## Count Derangements (Permutation such that no element appears in its original position)

- Time Complexity : O(n)

- Space Complexity : O(1)

A derangement is a permutation of the elements of a set, such that no element appears in its original position. The task of counting derangements is a classic problem in combinatorics. 

The number of derangements of a set of size \( n \) (denoted \( !n \)) can be computed using the following recursive formula:

\[ !n = (n - 1) \times (!(n - 1) + !(n - 2)) \]

With the base cases:

\[ !0 = 1 \]
\[ !1 = 0 \]

Let's implement this in Python and also analyze the time and space complexity.

### Recursive Solution with Memoization (Dynamic Programming)

The recursive solution can be made efficient using memoization to store intermediate results. Here's the implementation:

```python
def count_derangements(n):
    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return 0
    
    # Memoization array to store results of subproblems
    memo = [-1] * (n + 1)
    
    # Fill base cases
    memo[0] = 1
    memo[1] = 0
    
    # Fill the memoization array using the recursive formula
    for i in range(2, n + 1):
        memo[i] = (i - 1) * (memo[i - 1] + memo[i - 2])
    
    return memo[n]

# Example usage:
n = 5
print(f"Number of derangements for {n} elements is {count_derangements(n)}")
```

### Time and Space Complexity Analysis

1. **Time Complexity:**
   - The algorithm iterates from 2 to \( n \), performing a constant amount of work for each value of \( i \).
   - Therefore, the time complexity is \( O(n) \).

2. **Space Complexity:**
   - The memoization array `memo` of size \( n + 1 \) is used to store the intermediate results.
   - Therefore, the space complexity is \( O(n) \).

### Explanation:

- **Initialization:** The base cases \( !0 = 1 \) and \( !1 = 0 \) are initialized.
- **Iteration:** For each \( i \) from 2 to \( n \), the derangement count is computed using the formula \( !(i) = (i - 1) \times (!(i - 1) + !(i - 2)) \) and stored in the `memo` array.
- **Result:** The final result \( !n \) is returned from the `memo` array.

This implementation efficiently computes the number of derangements for a given \( n \) using dynamic programming, ensuring that intermediate results are reused and not recomputed.

To achieve the best time and space optimization for counting derangements, we can use an iterative approach that only keeps track of the last two computed values, rather than storing all intermediate results. This approach reduces the space complexity to \( O(1) \).

Here's the optimized implementation:

```python
def count_derangements(n):
    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return 0
    
    # Initialize the first two derangements
    derangement_prev2 = 1  # !0
    derangement_prev1 = 0  # !1
    
    # Compute derangements iteratively
    for i in range(2, n + 1):
        current_derangement = (i - 1) * (derangement_prev1 + derangement_prev2)
        derangement_prev2 = derangement_prev1
        derangement_prev1 = current_derangement
    
    return derangement_prev1

# Example usage:
n = 5
print(f"Number of derangements for {n} elements is {count_derangements(n)}")
```

### Time and Space Complexity Analysis

1. **Time Complexity:**
   - The algorithm iterates from 2 to \( n \), performing a constant amount of work for each value of \( i \).
   - Therefore, the time complexity is \( O(n) \).

2. **Space Complexity:**
   - Only a constant amount of space is used to store the last two computed values (`derangement_prev2` and `derangement_prev1`).
   - Therefore, the space complexity is \( O(1) \).

### Explanation:

- **Initialization:** The base cases \( !0 = 1 \) and \( !1 = 0 \) are initialized.
- **Iteration:** For each \( i \) from 2 to \( n \), the derangement count is computed using the formula \( !(i) = (i - 1) \times (!(i - 1) + !(i - 2)) \). Only the last two computed values are maintained, updating them as new derangements are calculated.
- **Result:** The final result \( !n \) is stored in `derangement_prev1`.

This optimized implementation efficiently computes the number of derangements with linear time complexity and constant space complexity, making it the best approach for large values of \( n \).