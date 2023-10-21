# Check if given strings are rotations of each other or not

#Time Complexity: O(n)
#Space Complexity: O(1)
def checkRotation(s1,s2):
    temp = s1
    s1 = s1+s1
    if(s1.find(s2)):
        return "Yes , "+s2+" is rotation of "+temp
    else:
        return "No , "+s2+" is not rotation of "+temp
s1 = 'abcd'
s2 = 'cdab'
print(checkRotation(s1,s2))