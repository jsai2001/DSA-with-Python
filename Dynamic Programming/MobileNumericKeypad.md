## Mobile Numeric Keypad

To solve this problem, we need to understand the constraints of movement on a standard numeric keypad and then determine how many unique sequences of length \( n \) can be formed by adhering to those constraints.

- **Time Complexity:** \( O(n) \)

- **Space Complexity:** \( O(n) \)

Here's a step-by-step breakdown of the approach:

### Step-by-Step Approach

1. **Define the Keypad and Valid Moves:**
   A standard mobile keypad looks like this:

   ```
   1 2 3
   4 5 6
   7 8 9
   * 0 #
   ```

   From each key, you can move to its adjacent keys (up, down, left, right).

2. **Create a Map of Moves:**
   We need to map each key to its possible moves:

   ```python
   moves = {
       '1': ['1', '2', '4'],
       '2': ['2', '1', '3', '5'],
       '3': ['3', '2', '6'],
       '4': ['4', '1', '5', '7'],
       '5': ['5', '2', '4', '6', '8'],
       '6': ['6', '3', '5', '9'],
       '7': ['7', '4', '8'],
       '8': ['8', '5', '7', '9', '0'],
       '9': ['9', '6', '8'],
       '0': ['0', '8']
   }
   ```

3. **Dynamic Programming Approach:**
   Use a dynamic programming (DP) table where `dp[i][j]` represents the number of unique sequences of length \( i \) ending at key \( j \).

4. **Initialize the DP Table:**
   For sequences of length 1, each key is a valid sequence of length 1:

   ```python
   dp[1][j] = 1 for all j in keys
   ```

5. **Fill the DP Table:**
   For each length \( i \) from 2 to \( n \), compute `dp[i][j]` by summing the values of `dp[i-1][k]` for all keys \( k \) that can move to key \( j \):

   ```python
   for i in range(2, n + 1):
       for key in keys:
           dp[i][key] = sum(dp[i-1][neigh] for neigh in moves[key])
   ```

6. **Compute the Result:**
   Sum all the values in `dp[n][j]` for all \( j \) to get the total number of unique sequences of length \( n \).

### Implementation

Let's write the implementation in Python:

```python
def count_sequences(n):
    # Define the moves map
    moves = {
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '5', '7', '9', '0'],
        '9': ['9', '6', '8'],
        '0': ['0', '8']
    }
    
    # Initialize the dp table
    dp = {i: {key: 0 for key in moves} for i in range(1, n + 1)}
    
    # Base case: sequences of length 1
    for key in moves:
        dp[1][key] = 1
    
    # Fill the dp table
    for i in range(2, n + 1):
        for key in moves:
            dp[i][key] = sum(dp[i-1][neigh] for neigh in moves[key])
    
    # Sum all sequences of length n
    result = sum(dp[n][key] for key in moves)
    return result

# Example usage
n = 3
print(count_sequences(n))  # Output the number of unique sequences of length 3
```

This function will return the number of unique sequences of length \( n \) that can be formed on a mobile keypad with the given movement constraints. Adjust the value of \( n \) to get results for different sequence lengths.

### Time and Space Complexity Analysis

Let's analyze the time and space complexity of the given dynamic programming solution.

#### Time Complexity

1. **Initialization of DP Table:**
   - Initializing the DP table with zeros: \( O(10n) \), where 10 is the number of keys and \( n \) is the sequence length.

2. **Filling the DP Table:**
   - There are \( n \) layers (from 2 to \( n \)).
   - For each layer \( i \) and each key, we compute the sum of sequences ending at each neighboring key.
   - This results in \( 10 \times n \times 5 \) operations in the worst case because each key can have at most 5 neighbors (e.g., key '5').

Therefore, the overall time complexity is \( O(10n \times 5) = O(50n) = O(n) \).

#### Space Complexity

1. **DP Table Storage:**
   - The DP table requires \( O(10n) \) space because it stores values for each key for each sequence length from 1 to \( n \).

Therefore, the space complexity is \( O(10n) = O(n) \).

### Summary

- **Time Complexity:** \( O(n) \)
- **Space Complexity:** \( O(n) \)

The given solution is efficient, with linear time and space complexities relative to the sequence length \( n \).