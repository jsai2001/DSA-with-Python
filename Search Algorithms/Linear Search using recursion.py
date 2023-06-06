'''
Recursive approch for Linear Search

Time Complexity: O(n)
    We iterate through whole array in the worst case , 
    for finding an element
Space Complexity: O(n)
    While we does the recursion , 
    we are piling up the stack of recursion stages , 
    to get the end result
'''
def search(arr,curr_index,key):
    if curr_index == -1:
        return -1
    if arr[curr_index] == key:
        return curr_index
    return search(arr, curr_index-1, key)

# Iterations flows from end to start
# So, current_index , we are pointing it to the end of the array
array = [1,2,3,4,5,6]
foundIndex = search(array,len(array)-1,5)
if(foundIndex!=-1):
    print("Element found at index ",foundIndex)
else:
    print("Element not found in the list")