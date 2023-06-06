''' 
Iterative approach for Linear search

Time Complexity: O(n)
    We traverse the entire list to find an element in the worst case
Space Complexity: O(1)
    We use only one temporary variable to compare the elements of the list ,
    while iterating through the array
'''
def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1

# Iteration flows from start to end
foundIndex = search([1,2,3,4,5,6],7)
if(foundIndex!=-1):
    print("Element found at index ",foundIndex)
else:
    print("Element not found in the list")