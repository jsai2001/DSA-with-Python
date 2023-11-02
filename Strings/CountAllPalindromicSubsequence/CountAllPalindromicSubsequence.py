# Time Complexity : O(N^2)
# Space Complexity : O(N^2)
# Dynamic Programming
class Solution:

    # Function to count the palindromic subsequences in the given string.
    def countPS(self,s):
        # Initializing a 2D array to store the results of subproblems.
        t = [[-1 for i in range(1001)]for i in range(1001)]
        # Modulus value for calculations.
        mod = 10**9+7

        # Function to solve the problem recursively.
        def solve(s,i,j,t):
            # Base cases: if the string has only one character or no characters.
            if i==j:
                return 1
            if i>j:
                return 0
            # If the result for the current subproblem has already been calculated, return it.
            if t[i][j]!=-1:
                return t[i][j]
            # If the first and last characters of the string are the same.
            elif s[i]==s[j]:
                # Recursively calculate the result for the remaining string (excluding the first and last characters).
                # Add 1 to account for the current subsequence itself.
                # Take the modulus to ensure the result is within the given range.
                t[i][j] = 1 + solve(s,i+1,j,t)%mod + solve(s,i,j-1,t)%mod
                t[i][j] %= mod
                return t[i][j]
            # If the first and last characters of the string are different.
            else:
                # Recursively calculate the result for the remaining string (excluding the first character OR the last character).
                # Subtract the result for the subproblem where the first and last characters are both excluded.
                # Take the modulus to ensure the result is within the given range.
                t[i][j] = solve(s,i+1,j,t)%mod + solve(s,i,j-1,t)%mod - solve(s,i+1,j-1,t)%mod
                t[i][j] %= mod
                return t[i][j]

        # Starting point of the recursive function.
        return solve(s,0,len(s)-1,t)

PalinSubseq = Solution()
print("Number of Palindromic Subsequences are: ",PalinSubseq.countPS("aab"))
