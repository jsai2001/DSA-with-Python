# Time Complexity: O(2^n)
# Space Complexity: O(n)
def wordBreak(wordList, word):
    if word == '':
        return True
    wordLen = len(word)
    for i in range(1, wordLen + 1):
        prefix = word[:i]
        if prefix in wordList and wordBreak(wordList, word[i:]):
            return True
    return False

wordList = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']
word = 'ilikesamsung'
result = wordBreak(wordList, word)
print(result)
'''
The above implementation uses recursion to check if the input string can be segmented 
into a space-separated sequence of dictionary words. 

The function wordBreak takes two arguments: wordList, which is a list of valid words,
and word, which is the input string to be checked.

The function returns True if the input string can be segmented into a space-separated sequence of dictionary words,
and False otherwise.

The above implementation has an exponential time complexity of O(2^n), 
where n is the length of the input string. 

This is because the function recursively checks all possible prefixes of the input string.

A more efficient solution to this problem involves using dynamic programming. 
The dynamic programming solution has a time complexity of O(n^2), where n is the length of the input string

The space complexity of the recursive implementation of the word break problem is O(n), 
where n is the length of the input string. 
This is because each function call will be stored on the program stack, 
and there will be at most n function calls in the stack at any given time
'''