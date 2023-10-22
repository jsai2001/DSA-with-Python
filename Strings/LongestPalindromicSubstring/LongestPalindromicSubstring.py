# Time Complexity: O(s^2)
# Space Complexity: O(1)
def longestPalindrome(s):
    res = ""
    resLen = 0
    # we are checking palindrome present or not using inward out method
    for i in range(len(s)):
        # check odd length palindromes
        l , r = i , i
        while l>=0 and r<len(s) and s[l] == s[r]:
            if (r - l + 1)>resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1
        # check even length palindromes
        l , r = i , i+1
        while l>=0 and r<len(s) and s[l] == s[r]:
            if (r - l + 1)>resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return res

print("Longest Palindrome: "+longestPalindrome("babad"))
print("Longest Palindrome: "+longestPalindrome("cbbd"))
