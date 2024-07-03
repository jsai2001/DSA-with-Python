### Minimum Cost of ropes

To solve the problem of connecting N ropes with minimum cost, we can use a greedy algorithm with a min-heap (priority queue). The idea is to always connect the two smallest ropes first, as this will minimize the cost at each step. Here's a detailed explanation and implementation:

## Problem Explanation

Given an array of integers `arr[]` representing the lengths of N ropes, the task is to connect these ropes into one rope. The cost to connect two ropes is equal to the sum of their lengths. We need to find the minimum cost to connect all ropes into one.

### Example

Let's say we have the following ropes with lengths: `[4, 3, 2, 6]`.

- First, we connect ropes with lengths 2 and 3. The cost is 2 + 3 = 5.
- Then, we have ropes of lengths `[4, 5, 6]`.
- Next, we connect ropes with lengths 4 and 5. The cost is 4 + 5 = 9.
- Then, we have ropes of lengths `[6, 9]`.
- Finally, we connect ropes with lengths 6 and 9. The cost is 6 + 9 = 15.

The total minimum cost is 5 + 9 + 15 = 29.

- **Time Complexity:** \(O(N log N)\)

- **Space Complexity:** \(O(N)\)

## Solution

To implement this, we use a min-heap to always get the two smallest elements efficiently.

### Steps:
1. Insert all rope lengths into a min-heap.
2. While the heap contains more than one rope, do the following:
   - Extract the two smallest ropes from the heap.
   - Calculate the cost to connect these two ropes.
   - Add this cost to the total cost.
   - Insert the resulting new rope back into the heap.
3. The total cost accumulated will be the minimum cost to connect all ropes.

### Algorithm Implementation

```python
import heapq

def min_cost_to_connect_ropes(arr):
    # Create a min-heap from the array of rope lengths
    heapq.heapify(arr)
    
    total_cost = 0
    
    # Iterate while the heap has more than one rope
    while len(arr) > 1:
        # Extract the two smallest ropes
        first_smallest = heapq.heappop(arr)
        second_smallest = heapq.heappop(arr)
        
        # Calculate the cost to connect these two ropes
        cost = first_smallest + second_smallest
        
        # Add this cost to the total cost
        total_cost += cost
        
        # Insert the resulting rope back into the heap
        heapq.heappush(arr, cost)
    
    return total_cost

# Example usage
arr = [4, 3, 2, 6]
print(min_cost_to_connect_ropes(arr))  # Output: 29
```

### Time and Space Complexity

- **Time Complexity**:
  - Building the min-heap from the array takes \(O(N)\).
  - Extracting the two smallest elements and inserting the new rope back into the heap takes \(O(log N)\) each time, and this operation is performed \(N-1\) times.
  - Therefore, the overall time complexity is \(O(N log N)\).

- **Space Complexity**:
  - The space complexity is \(O(N)\) because we store the heap which contains all the ropes' lengths.

This solution ensures that we always connect the two smallest ropes first, minimizing the total cost efficiently using a priority queue (min-heap).