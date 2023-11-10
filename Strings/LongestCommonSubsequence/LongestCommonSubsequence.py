'''
Expected Time Complexity : O(|str1|*|str2|)
Expected Auxiliary Space: O(|str1|*|str2|)
'''
def longestCommonSubsequence(text1,text2):
    '''
    Initialize DP array with 0 , as we are iterating DP array from the last ,
    This will be helpful for us for initial accumulation for the array 
    (i.e 1+dp[i+1][j+1] , max(dp[i+1][j],dp[i][j+1]]))
    '''
    dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
    for i in range(len(text1)-1,-1,-1):
        for j in range(len(text2)-1,-1,-1):
            if(text1[i]==text2[j]):
                '''
                If current character of both strings matched , then it is a possibility of having longest common subsequence
                So , we are adding 1 to current longest common subsequence , then it will be the new longest common subsequence
                '''
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                '''
                If current characters didn't matched , 
                we need to see the possibility of comparing elementating current character of str1 or current character of str2
                So , we would get maximum length of common subsequence , that we have until now
                We only do this due to current characters didn't matched
                '''
                dp[i][j] = max(dp[i][j+1],dp[i+1][j])
    return dp[0][0]
text1 = 'ABCDGH'
text2 = 'AEDFHR'
print(f"Longest Common Subsequence for {text1} and {text2} is : {longestCommonSubsequence(text1,text2)}")