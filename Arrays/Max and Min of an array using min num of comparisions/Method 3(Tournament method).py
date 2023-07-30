#Maximum and minimum of an array using the tournament method
#Divide the array into two parts and compare the maximums and minimums of the two parts 
#to get the maximum and the minimum of the whole array
def getMinMax(low,high,arr):
    arr_max = arr[low]
    arr_min = arr[low]
    # If there is only one element
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max,arr_min)
    # If there is only two element
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)
    # If there are more than 2 elements
    else:
        mid = int((low+high)/2)
        arr_max1, arr_min1 = getMinMax(low, mid, arr)
        arr_max2, arr_min2 = getMinMax(mid+1, high, arr)
    return (max(arr_max1, arr_max2),min(arr_min1,arr_min2))

arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_max, arr_min = getMinMax(low, high, arr)

print('Minimum element is ', arr_min)
print('Maximum element is ', arr_max)

'''
Output:

Minimum element is 1
Maximum element is 3000

Time Complexity: O(n)
Auxiliary Space: 
O(log n) as the stack space will be filled for the maximum height of the tree 
formed during recursive calls same as a binary tree.

Total number of comparisions:

Algorithmic Paradigm: Divide and Conquer 

T(n) = T(floor(n/2)) + T(ceil(n/2)) + 2
T(2) = 1
T(1) = 0
If n is a power of 2, then we can write T(n) as: 

T(n) = 2T(n/2) + 2
After solving the above recursion, we get 

T(n)  = 3n/2 -2
Thus, the approach does 3n/2 -2 comparisons if n is a power of 2. 
And it does more than 3n/2 -2 comparisons if n is not a power of 2
'''
