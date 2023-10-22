# Time Complexity: O(n)
# Space Complexity: O(1)
'''
We need to find maximum possible strings such that ,
we will be having equal number of 0s and 1s.
If it is not possible to split string satisfying the conditions 
then print -1

So, we need strings with equal number of 0's and 1's,
We are having iterators to keep track of count of 0's and 1's
When the count of 0's and 1's are equal , we assume it as a string
which satisfy our requirement , and make the counters of 0's and 1's as 0

Now , for instance , we are having 0100110101 , the possible resultant strings are

Input : 0100110101

Output:
01
0011
01
01

Total possible strings are : 4
'''
def splitBinaryStringsIntoSubstrings(string):
    count0 = count1 = count = 0
    for i in range(len(string)):
        if(string[i]=="0"):
            count0+=1
        else:
            count1+=1
        if(count0 == count1):
            count+=1
            count0 = count1 = 0
    if(count == 0):
        return -1
    return count

string = "0100110101"
print("Maximum count of consecutive substrings: "+str(splitBinaryStringsIntoSubstrings(string)))