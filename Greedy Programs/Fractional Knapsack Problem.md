### Fractional Knapsack Problem

The problem you're referring to is the Fractional Knapsack Problem, which is a variation of the classic Knapsack Problem. In the Fractional Knapsack Problem, you are allowed to break items to maximize the total value of the knapsack. Here's a detailed explanation of how to solve this problem, including the algorithm, documentation, and analysis of time and space complexity.

- **Time Complexity:** \(O(n \log n)\)

- **Space Complexity:** \(O(n)\)

## Fractional Knapsack Problem

### Problem Statement

Given:
- `n` items, each with a weight `wi` and a value `vi`.
- A knapsack with a maximum weight capacity `W`.

Objective:
- Maximize the total value in the knapsack by possibly taking fractions of items.

### Approach

The optimal solution to the Fractional Knapsack Problem can be achieved using a greedy algorithm. The key idea is to take items in the order of their value-to-weight ratio, which ensures that we are maximizing the value added to the knapsack at each step.

### Algorithm

1. **Calculate the value-to-weight ratio** for each item.
2. **Sort the items** in descending order of their value-to-weight ratio.
3. **Initialize total value** as 0 and remaining capacity as `W`.
4. **Iterate through the sorted items**:
   - If the current item can fit entirely in the knapsack, take the whole item.
   - If the current item cannot fit entirely, take the fraction that fits.
5. **Return the total value** of the knapsack.

### Pseudocode

```python
def fractional_knapsack(weights, values, W):
    # Calculate value to weight ratio for each item
    n = len(values)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    
    # Sort items by value to weight ratio in descending order
    items.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0  # Total value of the knapsack
    remaining_capacity = W  # Remaining capacity of the knapsack

    for ratio, weight, value in items:
        if remaining_capacity >= weight:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take the fraction of the item that fits
            total_value += ratio * remaining_capacity
            break

    return total_value
```

### Time Complexity

1. **Calculating value-to-weight ratios**: \(O(n)\)
2. **Sorting items**: \(O(n \log n)\)
3. **Iterating through sorted items**: \(O(n)\)

The overall time complexity is dominated by the sorting step, so it is \(O(n \log n)\).

### Space Complexity

The space complexity is \(O(n)\) because we need to store the list of items with their value-to-weight ratios.

### Example

Let's consider an example:

- Weights: [10, 20, 30]
- Values: [60, 100, 120]
- Capacity: 50

Using the algorithm:

1. Calculate value-to-weight ratios:
   - Item 1: 60/10 = 6
   - Item 2: 100/20 = 5
   - Item 3: 120/30 = 4

2. Sort items by ratio: [(6, 10, 60), (5, 20, 100), (4, 30, 120)]

3. Initialize total value = 0, remaining capacity = 50.

4. Iterating through sorted items:
   - Take the whole item 1: total value = 60, remaining capacity = 40
   - Take the whole item 2: total value = 160, remaining capacity = 20
   - Take 2/3 of item 3: total value = 160 + 4 * 20 = 240, remaining capacity = 0

The maximum total value of the knapsack is 240.

### Implementation in Python

```python
def fractional_knapsack(weights, values, W):
    # Calculate value to weight ratio for each item
    n = len(values)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    
    # Sort items by value to weight ratio in descending order
    items.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0  # Total value of the knapsack
    remaining_capacity = W  # Remaining capacity of the knapsack

    for ratio, weight, value in items:
        if remaining_capacity >= weight:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take the fraction of the item that fits
            total_value += ratio * remaining_capacity
            break

    return total_value

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
W = 50

print(fractional_knapsack(weights, values, W))  # Output: 240
```

This implementation efficiently solves the Fractional Knapsack Problem using a greedy approach, ensuring that the maximum possible value is achieved within the given weight capacity.