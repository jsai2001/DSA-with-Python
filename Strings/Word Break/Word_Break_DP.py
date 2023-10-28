# Dynamic Programming
# Time Complexity: O(n^2)
# Space complexity: O(n)
def wordBreak(wordList, word):
    if word == '':
        return True
    wordLen = len(word)
    dp = [False] * (wordLen + 1)
    dp[0] = True
    for i in range(1, wordLen + 1):
        for j in range(i):
            if dp[j] and word[j:i] in wordList:
                dp[i] = True
                break
    return dp[wordLen]

wordList = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']
word = 'ilikesamsung'
result = wordBreak(wordList, word)
print(result)
'''
The above implementation uses dynamic programming to check if the input string 
can be segmented into a space-separated sequence of dictionary words. 
The function wordBreak takes two arguments: wordList, which is a list of valid words, 
and word, which is the input string to be checked. 

The function returns True if the input string can be segmented into a space-separated sequence of dictionary words, 
and False otherwise.

The above implementation has a time complexity of O(n^2), 
where n is the length of the input string. 
This is because the function iterates over all possible prefixes of the input string.

The if dp[j] and word[j:i] in wordList: 
    statement checks if the prefix of the input string from index j to index i is a valid word in the dictionary wordList, 
    and if the prefix can be broken into a space-separated sequence of dictionary words.

Here, 
    dp[j] is a boolean value that indicates whether the prefix of the input string from index 0 to index j-1 
    can be broken into a space-separated sequence of dictionary words. 
    If dp[j] is True, it means that the prefix from index 0 to index j-1 can be broken into a space-separated sequence of dictionary words.

The condition word[j:i] in wordList checks if the substring of the input string from index j to index i-1 is a valid word in the dictionary wordList. 
If it is, then we can break the input string from index j to index i-1 into a space-separated sequence of dictionary words.

If both conditions are satisfied, then we can break the input string from index 0 to index i-1 into a space-separated sequence of dictionary words. 
The dynamic programming table dp is used to store whether each prefix of the input string can be broken into a space-separated sequence of dictionary words 1.

The space complexity of the dynamic programming implementation of the word break problem is O(n), where n is the length of the input string
'''