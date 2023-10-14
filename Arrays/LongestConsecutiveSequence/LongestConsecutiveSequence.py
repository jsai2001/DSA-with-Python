# Time Complexity : O(n)
# Space Complexity : O(n)
def findLongestConseqSubseq(arr, N):
    numSet = set(arr)
    longest = 0
    for n in arr:
        #Check if it is the start of the sequence
        if (n-1) not in numSet:
            length = 0
            while (n+length) in numSet:
                length+=1
            longest = max(length, longest)
    return longest
arr = [100,4,300,1,3,2]
n = len(arr)
print(findLongestConseqSubseq(arr,n))
