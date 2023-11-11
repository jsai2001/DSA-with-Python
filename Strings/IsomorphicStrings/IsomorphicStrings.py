# Problem Statement
'''
Given two strings 'str1' and 'str2', 
check if these two strings are isomorphic to each other.

If the characters in str1 can be changed to get str2, then two strings, str1 and str2, are isomorphic. 
A character must be completely swapped out for another character while maintaining the order of the characters. 
A character may map to itself, but no two characters may map to the same character.
'''
# Expected Time Complexity: O(|str1|+|str2|).
# Expected Auxiliary Space: O(Number of different characters).
# Note: |s| represents the length of string s.

def areIsomorphic(str1,str2):
    if(len(str1)!=len(str2)):
        return 0
    charmap = dict()
    usedchars = set()
    for i in range(0,len(str1)):
        if(str1[i] not in charmap):
            if(str2[i] in usedchars):
                return False
            charmap[str1[i]]=str2[i]
            usedchars.add(str2[i])
        elif(str1[i] in charmap and str2[i]!=charmap[str1[i]]):
            return False
    return True
text1='pijthbsfy'
text2='fvladzpbf'
result="" if areIsomorphic(text1,text2) else "Not"
print(f"{text1} and {text2} are {result} isomorphic to each other")

# Algorithm
'''
First we need to compare lengths of string 1 & 2 ,
If those are not same , it means they cannot be isomorphic strings in any way

Later we need to ensure , that every character of str1 , will be mapped to a unique character of str2
No two characters of str1 , should match to single character of str2,
If yes , It can't be isomophic string.

If we get , as repeated character in str1 , then the corresponding character of str2 ,
should be same as earlier occurance. This should be True , else return False

If character of str1 , has no occurance until now , and it's corresponding char of str2 isn't used earlier
Add them in the map and char of str2 to usedChars set , else return False

'''