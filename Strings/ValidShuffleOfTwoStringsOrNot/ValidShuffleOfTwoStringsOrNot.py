# Time Complexity : O(n)
# Space Complexity : O(1)
def validShuffle(s1,s2,res):
    s1len = len(s1)
    s2len = len(s2)
    reslen = len(res)
    if(s1len+s2len != reslen):
        return "No"
    else:
        flag = 0
        s1iter = s2iter = resiter = 0
        while(resiter < reslen):
            if(s1iter < s1len and s1[s1iter]==res[resiter]):
                s1iter+=1
            elif(s2iter < s2len and s2[s2iter]==res[resiter]):
                s2iter+=1
            else:
                flag = 1
                break
            resiter+=1
        if(s1iter < s1len or s2iter < s2len):
            return "No"
        else:
            return "Yes"
s1 = "xy"
s2 = "12"
res = "x1y2"
print(validShuffle(s1,s2,res))