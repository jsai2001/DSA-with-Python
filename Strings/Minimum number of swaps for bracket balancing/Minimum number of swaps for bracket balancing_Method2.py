# Time Complexity: O(n)
    # Iterating through whole string
# Space Complexity: O(1)
    # We are not using any extra space , we are using variables for calculating the result
def minimumNumberOfSwaps(S):
    '''
    Basically , we gonna have a counter for number of open brackets and number of closing brackets
    When current character is ']' then we gonna see number closing brackets are more or less than the open brackets
    But , if we got current character as '[' then , we will have a chance of balancing the extra close brackets with current closing bracket
    So , whenever we are getting an opening bracket , we check , do we have close brackets more than open brackets (fault = close - open & fault > 0)
    And if we are having , we will add 'close - open' to the ans , this is similar to the swap operation , and later ,
    we will decrease fault by 1 , because , we balanced one fault closing bracket with an opening bracket.
    '''
    open = close = 0
    ans = 0
    fault = 0
    for i in range(len(S)):
        if(S[i] == ']'):
            close += 1
            fault = close - open
        else:
            open += 1 # This open doesn't affect previously calculated fault value
            if( fault > 0 ):
                ans += fault
                fault -= 1
    return ans
print("Minimum number of swaps required to balance ]][[ : "+str(minimumNumberOfSwaps(']][[')))