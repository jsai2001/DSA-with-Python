### Maximum profit by buying and selling a share at most twice

- **Time Complexity:** \(O(n)\)
- **Space Complexity:** \(O(n)\)

To solve this problem, we need to find the maximum profit that can be achieved with at most two transactions. The key constraint is that the second transaction can only start after the first one is complete.

Here's a detailed step-by-step approach to solve this problem with optimal time and space complexity:

### Step-by-Step Solution

1. **Define the Problem:**
   Given an array `prices` where `prices[i]` is the price of a given stock on the i-th day, we need to maximize the profit with at most two transactions.

2. **First Pass (Left to Right):**
   - We calculate the maximum profit we can make by making the first transaction from day 0 to day i.
   - Let `left_profits[i]` be the maximum profit we can make from day 0 to day i.

3. **Second Pass (Right to Left):**
   - We calculate the maximum profit we can make by making the second transaction from day i to the last day.
   - Let `right_profits[i]` be the maximum profit we can make from day i to the last day.

4. **Combine Results:**
   - The maximum profit with at most two transactions is the maximum value of `left_profits[i] + right_profits[i]` for all i.

### Implementation

Here's the code to implement this approach:

```python
def maxProfit(prices):
    if not prices:
        return 0
    
    n = len(prices)
    
    # Step 1: Calculate maximum profit for one transaction from day 0 to i
    left_profits = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        left_profits[i] = max(left_profits[i-1], prices[i] - min_price)
    
    # Step 2: Calculate maximum profit for one transaction from day i to end
    right_profits = [0] * n
    max_price = prices[-1]
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        right_profits[i] = max(right_profits[i+1], max_price - prices[i])
    
    # Step 3: Calculate maximum profit with at most two transactions
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, left_profits[i] + right_profits[i])
    
    return max_profit

# Example usage:
prices = [3,3,5,0,0,3,1,4]
print(maxProfit(prices))  # Output: 6
```

### Explanation

- **Left Profits Calculation:**
  - We maintain `min_price` as the minimum price encountered so far.
  - For each day, we update `left_profits[i]` to be the maximum of `left_profits[i-1]` and the profit from buying at `min_price` and selling at `prices[i]`.

- **Right Profits Calculation:**
  - We maintain `max_price` as the maximum price encountered from the right.
  - For each day, we update `right_profits[i]` to be the maximum of `right_profits[i+1]` and the profit from buying at `prices[i]` and selling at `max_price`.

- **Combining Results:**
  - For each day, the combined profit is the sum of `left_profits[i]` and `right_profits[i]`.
  - We track the maximum of these combined profits to get the final result.

### Complexity

- **Time Complexity:** \(O(n)\) where \(n\) is the number of days.
- **Space Complexity:** \(O(n)\) due to the additional space used for `left_profits` and `right_profits`.

This solution ensures we find the maximum profit efficiently with linear time and space complexity.