### Minimum Platforms Problem

To solve the problem of finding the minimum number of platforms required at a railway station to ensure that no train is kept waiting, we can use a sorting-based approach. Here’s a step-by-step explanation:

- **Time Complexity:** \(O(n \log n)\)

- **Space Complexity:** \(O(1)\)

### Detailed Explanation

1. **Input Definition**:
   - We have two lists: `arrivals` and `departures`, each containing the arrival and departure times of the trains, respectively.
   - For example: 
     ```python
     arrivals = [900, 940, 950, 1100, 1500, 1800]
     departures = [910, 1200, 1120, 1130, 1900, 2000]
     ```

2. **Sorting**:
   - Sort both the `arrivals` and `departures` lists. This allows us to process events (arrivals and departures) in chronological order.
     ```python
     arrivals.sort()
     departures.sort()
     ```

3. **Two-pointer Technique**:
   - Use two pointers `i` and `j` to traverse the `arrivals` and `departures` lists, respectively.
   - Initialize variables `platform_needed` and `max_platforms` to keep track of the current number of platforms needed and the maximum number of platforms needed at any time.
     ```python
     i = 0  # Pointer for arrivals
     j = 0  # Pointer for departures
     platform_needed = 0
     max_platforms = 0
     ```

4. **Traverse the Lists**:
   - Traverse both lists using the two pointers.
   - If the next event in the timeline is an arrival (`arrivals[i] <= departures[j]`), increment `platform_needed` and move the `i` pointer.
   - If the next event is a departure (`arrivals[i] > departures[j]`), decrement `platform_needed` and move the `j` pointer.
   - Update `max_platforms` to be the maximum of `max_platforms` and `platform_needed`.
     ```python
     while i < len(arrivals) and j < len(departures):
         if arrivals[i] <= departures[j]:
             platform_needed += 1
             i += 1
             max_platforms = max(max_platforms, platform_needed)
         else:
             platform_needed -= 1
             j += 1
     ```

5. **Result**:
   - The value of `max_platforms` after processing all events will be the minimum number of platforms required.

### Implementation in Python

```python
def find_minimum_platforms(arrivals, departures):
    # Sort the arrival and departure times
    arrivals.sort()
    departures.sort()
    
    # Initialize pointers for arrival and departure arrays
    i = 0
    j = 0
    
    # Initialize variables to store the count of platforms needed and the maximum platforms needed at any time
    platform_needed = 0
    max_platforms = 0
    
    # Traverse through both arrays
    while i < len(arrivals) and j < len(departures):
        if arrivals[i] <= departures[j]:
            platform_needed += 1
            i += 1
            max_platforms = max(max_platforms, platform_needed)
        else:
            platform_needed -= 1
            j += 1
            
    return max_platforms

# Example usage
arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
print(find_minimum_platforms(arrivals, departures))  # Output: 3
```

### Time and Space Complexity

- **Time Complexity**:
  - Sorting both the `arrivals` and `departures` lists takes \(O(n \log n)\).
  - The while loop to traverse through the events takes \(O(n)\).
  - Hence, the overall time complexity is \(O(n \log n)\).

- **Space Complexity**:
  - The space complexity is \(O(1)\) additional space, excluding the input lists. The sorting is done in-place if we assume the input lists can be modified.

This approach efficiently calculates the minimum number of platforms needed, ensuring that no train has to wait.