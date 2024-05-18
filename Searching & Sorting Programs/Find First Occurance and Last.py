"""
Problem Statement:
Given a sorted array arr containing n elements with possibly some duplicate, 
the task is to find the first and last occurrences of an element x in the given array.
Note: If the number x is not found in the array then return both the indices as -1.

Approch:

This code utilizes binary search twice:

Find the first occurrence:

It performs a standard binary search to find the index mid where arr[mid] is equal to x.
If arr[mid] is less than x, it means x can only be present in the right half of the array, so we update low to mid + 1.
If arr[mid] is greater than x, it means x can only be present in the left half, so we update high to mid - 1.
If arr[mid] is equal to x, we update first to mid and continue searching in the left half to find the exact first occurrence. 
We achieve this by setting high to mid - 1 in the loop.

Find the last occurrence (starting from the first occurrence):

We perform another binary search similar to the first one, but starting from the index first (which holds the first occurrence).
This time, when we find arr[mid] equal to x, we update last to mid and continue searching in the right half to find the last occurrence. 
We achieve this by setting low to mid + 1 in the loop.
This approach achieves logarithmic time complexity (O(log n)) because the search space is halved in each iteration of the binary search. 
By using separate searches for the first and last occurrences, we avoid iterating through the entire array and achieve the desired time complexity.
"""

"""
Finds the first and last occurrences of an element in a sorted array with duplicates using binary search.
Args:
    arr: A sorted array of integers.
    x: The element to search for.
Returns:
    A list containing the first and last occurrences of x in arr, or [-1, -1] if x is not found.
"""
def binary_search(arr, x, findFirst):
    """
    Performs binary search to find the first or last occurrence of x.
    Args:
        low: Lower bound of the search space.
        high: Upper bound of the search space.
        direction: +1 for finding first occurrence, -1 for last occurrence.
    Returns:
        The index of the first or last occurrence of x, or -1 if not found.
    """
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            result = mid
            if findFirst:
                high = mid - 1  # Search in the left half
            else:
                low = mid + 1   # Search in the right half
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return result
arr = [7, 7, 9, 10, 10]
x = 6
# Find the first occurrence using binary search
first_occurrence = binary_search(arr, x, True)
# Find the last occurrence using binary search
last_occurrence = binary_search(arr, x, False)
# If x is not found, return [-1, -1]
if first_occurrence == -1:
    print([-1, -1])
else:
    print([first_occurrence, last_occurrence])
