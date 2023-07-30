# Maximum and minimum of an array by comparing in pairs
'''
If n is odd then initialize min and max as the first element. 
If n is even then initialize min and max as minimum and maximum of the first two elements respectively. 
For the rest of the elements, pick them in pairs and compare their 
maximum and minimum with max and min respectively.
'''
def getMinMax(arr):
    n = len(arr)
    # If array has even number of elements then
    # initialize the first two elements as minimum
    # and maximum
    if( n % 2 == 0 ):
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
        # set the starting index for loop
        i = 2
    # If array has odd number of elements then
    # initialize the first element as minimum
    # and maximum
    else:
        mx = mn = arr[0]
        # set the starting index for loop
        i = 1
    # In the while loop , pick elements in pair and 
    # compare the pair with max and min so far
    while(i < n - 1):
        if arr[i] < arr[i + 1]:
            mx = max(mx, arr[i+1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i+1])
        # Increment the index by 2 as two
        # elements are processed in loop
        i += 2
    return (mx,mn)

if __name__ =='__main__':     
    arr = [1000, 11, 445, 1, 330, 3000]
    mx, mn = getMinMax(arr)
    print("Minimum element is", mn)
    print("Maximum element is", mx)

'''
Output:
Minimum element is 1
Maximum element is 3000

Time Complexity: O(n)
Auxiliary Space: O(1) as no extra space was needed.

Total number of comparisions
* Different for even and odd n

If n is odd:    3*(n-1)/2  
If n is even:   1 Initial comparison for initializing min and max, 
                and 3(n-2)/2 comparisons for rest of the elements  
                =  1 + 3*(n-2)/2 = 3n/2 -2
'''