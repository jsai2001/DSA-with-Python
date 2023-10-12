# Time Complexity: O(n * log(n) ), applying binary search on each element
# Auxiliary Space: O(1)

# Follow the steps below to solve the given problem:

# Sort the array arr[] in increasing order.
# Loop from i = 0 to N-1.
# Find the index of the first element having value same or just greater than (K – arr[i]) using lower bound.
# Find the index of the first element having value just greater than (K – arr[i]) using upper bound.
# The gap between these two indices is the number of elements with value same as (K – arr[i]).
# Add this with the final count of pairs.
# Return the final count after the iteration is over.
import bisect
# Function to find the count of pairs
def getPairsCount(arr,n,k):
    arr.sort()
    x,c = 0,0
    for i in range(n-1):
        x = k-arr[i]
        # Lower bound from i+1
        y = bisect.bisect_left(arr,x,i+1,n)
        # Upper bound from i+1
        z = bisect.bisect_right(arr,x,i+1,n)
        c += z - y
    return c

arr = [1, 5, 7, -1]
n = len(arr)
k = 6
 
# Function call
print("Count of pairs is", getPairsCount(arr, n, k))