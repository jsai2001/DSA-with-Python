# Task is to find the elements of a contiguous subarray of numbers 
# that has the largest sum.

# The naive solution is to generate all the possible subarrays of
# the given array using recursion and return the array , which
# provides maximum sum of the subarray

# Print all possible subarrays for given array using recursion

# Recursive function to print all possible subarrays
def printSubArrays(arr, start, end):
    # Stop if we have reached the end of the array
    if end == len(arr):
        return
    # Increment the end point and start from 0
    elif start > end:
        return printSubArrays(arr, 0, end+1)
    # Print the subarray and increment the starting point
    else:
        print(arr[start:end+1])
        return printSubArrays(arr,start+1,end)

arr = [1, 2, 3]
print("--------------------------")
print("Generated Subarrays are: ")
print("--------------------------")
printSubArrays(arr, 0, 0)
print("--------------------------")

'''
Output:
--------------------------
Generated Subarrays are:
--------------------------
[1]
[1, 2]
[2]
[1, 2, 3]
[2, 3]
[3]
--------------------------

Time Complexity: O(2^n)
Auxiliary Space: O(2^n)
'''