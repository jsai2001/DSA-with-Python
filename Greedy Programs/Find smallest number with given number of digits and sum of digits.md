### Find smallest number with given number of digits and sum of digits

Implementation to find the smallest number with the sum of its digits as \( s \) and the number of digits as \( d \):

### Approach:

1. **Initialization and Validation**:
    - If \( s = 0 \) and \( d = 1 \), the smallest number is "0".
    - If \( s = 0 \) and \( d > 1 \), it is impossible to form such a number because the sum of digits of any multi-digit number cannot be zero.
    - If \( s > 9 \times d \), it is impossible to form such a number because the maximum sum with \( d \) digits is \( 9 \times d \).

2. **Construct the Smallest Number**:
    - Start by initializing an array to store the digits.
    - Allocate the digits from the least significant to the most significant.
    - Ensure the first digit is at least 1 (to avoid leading zeros), if necessary.

- **Time Complexity:** \(O(d)\)

- **Space Complexity:** \(O(d)\)

### Algorithm:

1. If \( s = 0 \) and \( d = 1 \), return "0".
2. If \( s = 0 \) and \( d > 1 \), return "-1".
3. If \( s > 9 \times d \), return "-1".
4. Initialize an array `digits` of size \( d \) with all elements set to 0.
5. Set `remaining_sum` to \( s \).
6. Iterate over the digits array from the last position to the first:
   - For each position, set the current digit to the minimum of 9 and `remaining_sum`.
   - Subtract this value from `remaining_sum`.
7. Ensure the first digit is non-zero if `d > 1`.
8. Join the digits array to form the resultant number as a string and return it.

### Implementation:

```python
def smallest_number_with_sum_and_digits(s, d):
    # Case when sum is zero
    if s == 0:
        if d == 1:
            return "0"
        else:
            return "-1"

    # Case when the sum is greater than the maximum possible sum for d digits
    if s > 9 * d:
        return "-1"
    
    # Initialize the result array with zeros
    digits = [0] * d
    
    # Remaining sum to be distributed
    remaining_sum = s
    
    # Fill digits from the least significant digit to the most significant
    for i in range(d - 1, -1, -1):
        if remaining_sum > 9:
            digits[i] = 9
            remaining_sum -= 9
        else:
            digits[i] = remaining_sum
            remaining_sum = 0
    
    # Make sure the first digit is non-zero if needed
    if digits[0] == 0:
        for i in range(1, d):
            if digits[i] > 0:
                digits[i] -= 1
                digits[0] = 1
                break

    # Join the digits to form the resultant number
    return ''.join(map(str, digits))

# Test cases
print(smallest_number_with_sum_and_digits(9, 2))  # Output: "18"
print(smallest_number_with_sum_and_digits(20, 3)) # Output: "299"
print(smallest_number_with_sum_and_digits(0, 1))  # Output: "0"
print(smallest_number_with_sum_and_digits(0, 2))  # Output: "-1"
print(smallest_number_with_sum_and_digits(10, 1)) # Output: "-1"
```

### Explanation of Test Cases:

1. `smallest_number_with_sum_and_digits(9, 2)`:
   - The smallest 2-digit number with a sum of digits equal to 9 is "18" (1 + 8 = 9).

2. `smallest_number_with_sum_and_digits(20, 3)`:
   - The smallest 3-digit number with a sum of digits equal to 20 is "299" (2 + 9 + 9 = 20).

3. `smallest_number_with_sum_and_digits(0, 1)`:
   - The smallest 1-digit number with a sum of digits equal to 0 is "0".

4. `smallest_number_with_sum_and_digits(0, 2)`:
   - It is impossible to have a 2-digit number with a sum of digits equal to 0, hence "-1".

5. `smallest_number_with_sum_and_digits(10, 1)`:
   - It is impossible to have a 1-digit number with a sum of digits equal to 10, hence "-1".

### Time Complexity:

- The algorithm involves a single iteration over the digits array, so the time complexity is \( O(d) \).

### Space Complexity:

- The space complexity is \( O(d) \) due to the storage required for the digits array.