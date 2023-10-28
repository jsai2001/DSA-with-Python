# Expected Time Complexity: O(|x|)
# Expected Auixilliary Space: O(|x|)
def isBalanced(x):
    stack = []
    itr = 0
    for i in range(len(x)):
        if(x[i] in ('{','[','(')):
            stack.append(x[i])
        elif(len(stack)>0 and ((stack[-1]=='{' and x[i]=='}') or (stack[-1]=='[' and x[i]==']') or (stack[-1]=='(' and x[i]==')'))):
            stack.pop()
        else:
            return False
    if(len(stack)==0):
        return True
    else:
        return False
string = "{([])}"
if(isBalanced(string)):
    print("Paranthesis are Balanced")
else:
    print("Paranthesis are unbalanced")