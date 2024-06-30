### Check if it is possible to survive on Island

To solve the problem of determining the minimum number of days on which you need to buy food to survive on the island, let's break it down step by step.

## Problem Explanation

Given:
- \( N \): Maximum units of food you can buy each day.
- \( S \): Number of days you need to survive.
- \( M \): Units of food required each day to survive.

Constraints:
- The shop is closed on Sundays (every 7th day).

- **Time Complexity:** \(O(1)\)

- **Space Complexity:** \(O(1)\)

You need to find the minimum number of days you need to buy food to survive for \( S \) days, or determine if it's impossible to survive.

## Approach

1. **Calculate Total Food Required**: You need \( S \times M \) units of food to survive for \( S \) days.
2. **Calculate Maximum Days to Buy Food**: Since the shop is closed on Sundays, the maximum days you can buy food is \((S - \left\lfloor S/7 \right\rfloor)\). This is because every 7th day the shop is closed.
3. **Check for Survival Possibility**:
   - If \( M > N \): It's impossible to survive since the daily required food is more than you can buy in a day.
   - If \((S \times M) > (S - \left\lfloor S/7 \right\rfloor) \times N \): It's impossible to survive since the total required food is more than the total food you can buy over the available days.
4. **Calculate Minimum Days to Buy Food**:
   - Divide the total required food by the maximum units you can buy in a day, and take the ceiling of this division to get the minimum days needed.

## Detailed Steps

1. **Calculate Total Food Required**:
   \( \text{Total\_Food\_Required} = S \times M \)

2. **Calculate Number of Days the Shop is Open**:
   \( \text{Available\_Days} = S - \left\lfloor S/7 \right\rfloor \)

3. **Check Feasibility**:
   - If \( M > N \): return "Impossible to survive".
   - If \( \text{Total\_Food\_Required} > \text{Available\_Days} \times N \): return "Impossible to survive".

4. **Calculate Minimum Days to Buy Food**:
   \( \text{Minimum\_Days\_to\_Buy} = \left\lceil \frac{\text{Total\_Food\_Required}}{N} \right\rceil \)

## Python Code

Here is the Python code to implement the above logic:

```python
import math

def min_days_to_buy_food(N, S, M):
    # Total food required to survive for S days
    total_food_required = S * M
    
    # Number of days the shop is open
    available_days = S - S // 7
    
    # Check if it is possible to survive
    if M > N:
        return "Impossible to survive"
    if total_food_required > available_days * N:
        return "Impossible to survive"
    
    # Calculate the minimum number of days to buy food
    min_days_to_buy = math.ceil(total_food_required / N)
    
    return min_days_to_buy

# Example usage
N = 4  # Maximum units of food you can buy each day
S = 10 # Number of days you are required to survive
M = 2  # Unit of food required each day to survive

result = min_days_to_buy_food(N, S, M)
print(result)
```

## Complexity Analysis

- **Time Complexity**: The algorithm runs in constant time \( O(1) \) since it involves basic arithmetic operations and a couple of conditional checks.
- **Space Complexity**: The algorithm uses constant space \( O(1) \) as it only uses a few variables to store the input values and intermediate results.

This solution efficiently determines the minimum number of days required to buy food to survive given the constraints or if survival is impossible.