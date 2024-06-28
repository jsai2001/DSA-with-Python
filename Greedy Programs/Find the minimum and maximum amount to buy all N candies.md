### Find the minimum and maximum amount to buy all N candies

### Problem Summary

In a candy store, you have \( N \) different types of candies with given prices. You can buy one candy and get \( K \) other different types for free. You need to determine:
1. The minimum amount of money required to buy all \( N \) candies.
2. The maximum amount of money required to buy all \( N \) candies.

- **Time Complexity:** \(O(n \log n)\)

- **Space Complexity:** \(O(1)\)

### Strategy

#### Minimum Cost Calculation
1. Sort the candy prices in ascending order.
2. Buy the cheapest candy and get the most expensive available \( K \) candies for free.
3. Repeat until all candies are bought.

#### Maximum Cost Calculation
1. Sort the candy prices in descending order.
2. Buy the most expensive candy and get the cheapest available \( K \) candies for free.
3. Repeat until all candies are bought.

### Implementation

```python
def calculate_minimum_and_maximum_costs(candies, K):
    N = len(candies)
    
    # Sort prices for minimum cost calculation
    candies.sort()
    
    min_cost = 0
    i = 0
    candies_used = 0
    while candies_used < N:
        min_cost += candies[i]
        candies_used += (K + 1)
        i+=1
    
    # Sort prices for maximum cost calculation
    candies.sort(reverse=True)
    
    max_cost = 0
    i = 0
    candies_used = 0
    while candies_used < N:
        max_cost += candies[i]
        candies_used += (K + 1)
        i += 1
    
    return min_cost, max_cost

# Example usage
prices = [1, 3, 4, 7, 8, 9]
K = 2
print(calculate_minimum_and_maximum_costs(prices, K))
# Output should be (4, 17)
```

### Example

For \( N = 6 \) candies with prices [1, 3, 4, 7, 8, 9] and \( K = 2 \):

- **Minimum Cost Calculation**:
  - Sorted prices: [1, 3, 4, 7, 8, 9]
  - Buy candy with price 1, get candies with prices 9 and 8 for free.
  - Buy candy with price 3, get candies with prices 7 and 4 for free.
  - Total minimum cost = 1 + 3 = 4

- **Maximum Cost Calculation**:
  - Sorted prices: [9, 8, 7, 4, 3, 1]
  - Buy candy with price 9, get candies with prices 1 and 3 for free.
  - Buy candy with price 8, get candies with prices 4 and 7 for free.
  - Total maximum cost = 9 + 8 = 17

### Time and Space Complexity

- **Time Complexity**: \( O(N \log N) \) due to sorting.
- **Space Complexity**: \( O(1) \) if the sorting is done in place.

This solution correctly calculates both the minimum and maximum costs required to buy all candies using the given offer.