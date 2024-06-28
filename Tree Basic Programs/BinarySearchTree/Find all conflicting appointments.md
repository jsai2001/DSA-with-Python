### Find all conflicting appointments

## Problem Statement

Given `n` appointments, each defined by a start and end time, find all pairs of conflicting appointments. Two appointments conflict if their time intervals overlap.

- **Time Complexity:** \(O(n^2)\)

- **Space Complexity:** \(O(n)\)

## Example

**Input:**

```
appointments = [(1, 4), (2, 5), (7, 9)]
```

**Output:**

```
[(1, 4) conflicts with (2, 5)]
```

**Explanation:**

- The first appointment (1, 4) overlaps with the second appointment (2, 5).
- The third appointment (7, 9) does not overlap with any other appointments.

## Approach

1. **Sort the Appointments:**
   - Sort the list of appointments based on their start times. This makes it easier to compare each appointment with the subsequent ones.
   
2. **Find Conflicting Appointments:**
   - Iterate through the sorted list and for each appointment, check if it conflicts with the subsequent appointments. If the end time of the current appointment is greater than the start time of the next appointment, they conflict.

### Algorithm

1. **Sort the Appointments:**
   - Sort the appointments based on the start time.
   
   ```python
   appointments.sort(key=lambda x: x[0])
   ```
   
2. **Find Conflicts:**
   - Initialize an empty list to store conflicting appointments.
   - Iterate through the sorted list:
     - For each appointment, compare it with the subsequent appointments.
     - If the end time of the current appointment is greater than the start time of the next appointment, add this pair to the list of conflicts.

### Pseudocode

```
function find_conflicting_appointments(appointments):
    sort appointments by start time
    conflicts = []
    
    for i from 0 to length(appointments) - 1:
        for j from i + 1 to length(appointments):
            if appointments[i].end > appointments[j].start:
                add (appointments[i], appointments[j]) to conflicts
            else:
                break
    
    return conflicts
```

### Python Implementation

```python
def find_conflicting_appointments(appointments):
    # Sort appointments by start time
    appointments.sort(key=lambda x: x[0])
    
    conflicts = []
    
    # Iterate through each appointment and find conflicts
    for i in range(len(appointments)):
        for j in range(i + 1, len(appointments)):
            # If the end time of the current appointment is greater than the start time of the next
            if appointments[i][1] > appointments[j][0]:
                conflicts.append((appointments[i], appointments[j]))
            else:
                # Since the appointments are sorted, no need to check further
                break
    
    return conflicts

# Example usage
appointments = [(1, 4), (2, 5), (7, 9)]
print(find_conflicting_appointments(appointments))
```

## Time Complexity

1. **Sorting:** Sorting the appointments takes \(O(n \log n)\).
2. **Finding Conflicts:** 
   - In the worst case, for each appointment, we may have to compare it with all subsequent appointments. This results in a time complexity of \(O(n^2)\).

Therefore, the overall time complexity is \(O(n \log n + n^2)\), which simplifies to \(O(n^2)\).

## Space Complexity

The space complexity is \(O(n)\) because the list of conflicts can potentially store all pairs of conflicting appointments, though in practice it will store fewer. The space for storing the sorted appointments is \(O(n)\).

In summary:

- **Time Complexity:** \(O(n^2)\)
- **Space Complexity:** \(O(n)\)

This approach ensures that we efficiently find all conflicting appointments in the given list.