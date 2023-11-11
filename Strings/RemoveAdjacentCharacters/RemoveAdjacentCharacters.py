# Time Complexity: O(|S|)
# Auxiliary Space: O(|S|)
def removeConsecutiveCharacter(S):
    result=""
    for i in range(len(S)):
        if(len(result)==0 or S[i-1]!=S[i]):
            # We are ignoring current character into result
            # If current character is same as the earlier character
            # And populating rest of the characters into result and return them as output
            result+=S[i]
    return result
text = "aabb"
print(f"For the string {text},\nAfter removing all adjacent duplicates,\nIt becomes :  {removeConsecutiveCharacter(text)}")