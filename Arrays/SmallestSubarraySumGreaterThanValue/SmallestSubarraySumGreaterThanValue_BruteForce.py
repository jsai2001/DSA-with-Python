# Time Complexity: O(n^2)
# Space Complexity: O(1)
import sys
def smallestSubArrayGreaterThanX(arr,n,X):
    minLength = sys.maxsize
    for i in range(n):
        curr_sum = 0
        for j in range(i,n):
            curr_sum+=arr[j]
            if(curr_sum>X):
                minLength = min(minLength,j-i+1)
    return minLength
arr = [1, 4, 45, 6, 0, 19]
X = 51
n = len(arr)
print("Smallest Subarray Sum Greater than Value: ",smallestSubArrayGreaterThanX(arr,n,X))