'''
 This program is mainly to balance all the brackets with minimal number of reversals,
 So , for that , we first see if the string of brackets is balanced or not
 By using the stack method , where we insert an element if the element is "{" and pop out
 if previous element is "{" and current element is "}"
 After doing that , we will have some result string , where we need to do some reversals
 To balance the string
'''

'''
The resultant string , could be like this }}}{
In first case , the resultant string , can't be odd , if it is odd , it can't be balanced
Because , we need two characters to make brackets balanced , so the resultant string must be even
If it is odd , we definitly can't balance.
So consider the resultant string is even => }}}{ , and mostly we will have group of '}' in one side
And group of '{' will be at one side , and closing brackets will be preceeded by the opening brackets

So , we are also having two counters for closing brackets as well as opening brackets,
And then we will divide the values of opening brackets and closing brackets by half , because
We are trying to reverse count/2 brackets and try to match with the rest.

For example , if we have }}}} or }{}{ , we need to reverse n/2 number of brackets to make that a 
balanced string.

}}}} => {}{} => 2 reversals (n/2 reversals)
}{}{ => {{}} => 2 reversals (n/2 reversals)

For this string }{{}}{{{

The unbalanced string would be }{{{

close brackets count is 3 => closeCount
open brackets count is 1 => openCount

Minimum number of reversals required would be : ceil(closeCount/2)+ceil(openCount/2)
                                                ceil(3/2)+ceil(1/2)
Minimum number of reversals required would be : 2+1 => 3

So , the final balanced string would be : }{{{ =>{}{}
''' 

import math
def countRev (s):
    if(len(s)%2==1):
        return "-1"
    else:
        closeCount = 0
        openCount = 0
        stack = []
        for i in range(len(s)):
            if(s[i]=='{'):
                stack.append('{')
                openCount+=1
            elif(s[i]=='}' and len(stack)>0 and stack[-1]=='{'):
                stack.pop()
                openCount-=1
            else:
                closeCount+=1
        openCount = math.ceil(openCount/2)
        closeCount = math.ceil(closeCount/2)
        return openCount + closeCount
print("}{{}}{{{")