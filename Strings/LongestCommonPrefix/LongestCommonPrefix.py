'''
n = len(strs)
m = minlen of all strings in the strs
Time Complexity: O(nm)
Space Complexity: O(1)

We are trying to find longestCommonPrefix,
The method we are following is to , 
first find the minlength string among all the strings of strs,
And why is that? The maximum length of longest Common Prefix would be that minlength

For example [aaaa,aaa,aaaaa] , the minlength is 3 , and the LCS is aaa

And we are also checking the edge cases ,
for example if only one string is passed , that would be only LCS possible
And if no strings passed or one of the strings is an empty string ,
then the LCS will be definitly the empty string of length 0 ,
even we have any other strings in strs array

And in the main algorithm , after all these base cases verification
We will iterate through the strs string array , and compare the 1st string with rest of the strings ,
character by character , it means we will compare the string 1's char 0 with rest of the strings
And if we find any character mismatch at any stage , we are going to return the str[0][:maxidx] , 
We are not including character at maxidx , because that is the character which caused mismatch,
And if without any mismatches , if we get out of the loops , we would return str[0][:maxlen+1]

Here the maxidx variable , will be anywhere between 0 and minlen , 
It is not restricted to be always equal to len(str[0])
'''
def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minlen = 201
        if(len(strs)==1):
            return strs[0]
        elif(len(strs)==0):
            return ""
        for i in strs:
            currlen = len(i)
            if currlen<minlen:
                minlen=currlen
        if(minlen==0):
            return ""
        maxidx = 0
        for chariteridx in range(minlen):
            for striter in range(1,len(strs)):
                maxidx = chariteridx
                if(strs[striter][chariteridx]!=strs[0][chariteridx]):
                    return strs[0][:maxidx]                    
        return strs[0][:maxidx+1]
print("""LCS for ["flower","flow","flight"]: """+longestCommonPrefix(["flower","flow","flight"]))
print("""LCS: for ["dog","racecar","car"]: """+longestCommonPrefix(["dog","racecar","car"]))
print("""LCS: for ["ab", "a"]: """+longestCommonPrefix(["ab", "a"]))
