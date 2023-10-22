# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
def LongestRepeatingSubsequence(str):
    s1 = str
    s2 = str
    n = len(str)+1
    lcs = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0):
                lcs[i][j]=0
            elif(s1[i-1]==s2[j-1] and i-1!=j-1):
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
    return lcs[n-1][n-1]
print("Longest Subsequence: "+str(LongestRepeatingSubsequence("axxzxy")))
