def countWaysToMakeSum(coins, N, sum):
    # Initialize the dp array with zeros
    dp = [0] * (sum + 1)
    
    # There's one way to make sum 0, by using no coins
    dp[0] = 1
    
    # Iterate over each coin
    for coin in coins:
        # Update dp array for all values from coin to sum
        for i in range(coin, sum + 1):
            dp[i] += dp[i - coin]
    
    return dp[sum]

# Example usage:
coins = [1, 2, 3]
N = len(coins)
sum_value = 4
print(countWaysToMakeSum(coins, N, sum_value))  # Output: 4

# Time and Space Complexity
# Time Complexity: 𝑂(sum × 𝑁) : 
#       This is because we iterate over each coin and for each coin, we update the dp array up to the given sum.
# Space Complexity: O(sum) : 
#       We use an array of size sum + 1 to store the number of ways to make each sum.
