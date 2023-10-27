# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
'''
It is preferable to insert , delete , replace characters of str1 to match with str2,
rather than touching str2, which makes this solution more complex.
'''
def FindMineditDistance(str1,str2,m,n):
    if(m==-1):
        return n+1
    if(n==-1):
        return m+1
    if(DP[m][n]!=-1):
        return DP[m][n]
    if(str1[m]==str2[n]):
        DP[m][n]=FindMineditDistance(str1,str2,m-1,n-1)
        return DP[m][n]
    replaceOp = FindMineditDistance(str1,str2,m-1,n-1)
    insertOp = FindMineditDistance(str1,str2,m,n-1)
    deleteOp = FindMineditDistance(str1,str2,m-1,n)
    DP[m][n] = 1 + min(replaceOp,min(insertOp,deleteOp))
    return DP[m][n]

str1="geek"
m=len(str1)
str2="gesek"
n=len(str2)
DP = [[-1 for i in range(n)] for j in range(m)]
print("Minimum Edit Distance: ",FindMineditDistance(str1,str2,m-1,n-1))

'''
The algorithm works by building a matrix dp where each cell (i, j) represents the
minimum number of operations required to convert the first i characters of str1 to the first j characters of str2.
The value in each cell is calculated based on the values in its adjacent cells and whether or not the corresponding characters match.

When we encounter a mismatch between the characters of str1 and str2, we have three options:

Insert a character into str1 to match the current character of str2.
Delete a character from str1 to skip over the current character of str2.
Replace the current character of str1 with the current character of str2.

To find the minimum number of operations required for each option, we look at the values in the adjacent cells of dp[i][j]. Specifically, we look at:

The value in dp[i][j - 1], 
    which represents the number of operations required to convert the first i characters of str1 to the first j - 1 characters of str2. This is because we are considering the case where we insert a character into str1 to match the current character of str2.
The value in dp[i - 1][j], 
    which represents the number of operations required to convert the first i - 1 characters of str1 to the first j characters of str2. This is because we are considering the case where we delete a character from str1 to skip over the current character of str2.
The value in dp[i - 1][j - 1], 
    which represents the number of operations required to convert the first i - 1 characters of str1 to the first j - 1 characters of str2. This is because we are considering the case where we replace the current character of str1 with the current character of str2.
We then take the minimum value among these three options and add one to it (to account for performing one more operation). 
This gives us our final value for dp[i][j].
'''