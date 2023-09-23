# Python3 code to generate all possible
# subarrays/subArrays
# Complexity- O(n^3) 
  
# Prints all subarrays in arr[0..n-1]
def subArray(arr, n):
    # Pick starting point
    for i in range(0,n):
        # Pick ending point
        for j in range(i,n):
            # Print subarray between
            # current starting and ending points
            for k in range(i,j+1):
                print(arr[k],end=" ")
            print("\n",end="")
arr = [1,2,3,4]
n = len(arr)
print("-------------------------")
print("All Non-empty Subarrays")
print("-------------------------")
subArray(arr,n)
print("-------------------------")
'''
Output:

-------------------------
All Non-empty Subarrays
-------------------------
1
1 2
1 2 3
1 2 3 4
2
2 3
2 3 4
3
3 4
4
-------------------------

Time Complexity: O(n^3)
Space Complexity: O(1)
'''