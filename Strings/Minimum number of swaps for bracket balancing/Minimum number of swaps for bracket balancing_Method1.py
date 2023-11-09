# Time Complexity: O(n)
    # Iterating through whole string
# Space Complexity: O(n)
    # Maximum length of openBracketIdx could be of len(n/2) , so it would be O(n)
def minimumNumberOfSwaps(S):
    S = list(S)
    openBracketIdx = []
    for i in range(len(S)):
        if(S[i]=='['):
            openBracketIdx.append(i)
    Idx = 0
    count = 0
    ans = 0
    for i in range(len(S)):
        if(S[i] == '['):
            count += 1
            Idx += 1
        else: # S[i] = ']'
            count -= 1
            if(count<0): # If we have any unbalanced closed bracket
                ans += openBracketIdx[Idx] - i
                S[i],S[openBracketIdx[Idx]]=S[openBracketIdx[Idx]],S[i]
                count = 1
                Idx += 1
    return ans
print("Minimum number of swaps required to balance ]][[ : "+str(minimumNumberOfSwaps(']][[')))