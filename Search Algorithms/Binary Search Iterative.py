# Iterative Binary Search function
# It returns index of x in given array arr if present
# else returns -1
def binary_search(arr,x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low<=high:
        mid = ( high + low ) //2
        # If x is greater , ignore left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller , ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # element x found at mid
        else:
            return mid
    # If we reach here , 
    # we can decide that element is not found in the array
    return -1

arr = [2, 3, 4, 10, 40]
x = 10
# Function call
result = binary_search(arr,x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")