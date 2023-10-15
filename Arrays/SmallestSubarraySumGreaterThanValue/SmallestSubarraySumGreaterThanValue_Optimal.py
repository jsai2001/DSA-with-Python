# Time Complexity : O(n)
# Space Complexity : O(1)
import sys
def smallestSubArrayGreaterThanX(arr,n,X):
    i = j = 0
    curr_sum = 0
    min_subarr_len = sys.maxsize
    flag = 0
    while(i<=j and j<n):
        while(curr_sum<=X and j<n):
            curr_sum+=arr[j]
            j+=1
        while(curr_sum>X and i<j):
            min_subarr_len = min(min_subarr_len,j-i)
            curr_sum-=arr[i]
            i+=1
            flag = 1
    if(flag == 0): # If we didn't find any subarray which sum is greater than X
        return 0
    return min_subarr_len
arr = [1, 4, 45, 6, 0, 19]
X = 51
n = len(arr)
print("Smallest Subarray Sum Greater than Value: ",smallestSubArrayGreaterThanX(arr,n,X))