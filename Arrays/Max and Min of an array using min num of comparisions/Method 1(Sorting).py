# Maximum and minimum elements of an array using minimum number of comparisions (Sorting)
# We have created a structure named pair , which contains min and max to return multiple values
class pair:
    def __init__(self):
        self.min = None
        self.max = None
'''
One approach to find the maximum and minimum element in an array 
is to first sort the array in ascending order. 
Once the array is sorted, the first element of the array will be 
the minimum element and the last element of the array will be the maximum element.
'''
def getMinMax(arr):
    arr.sort()
    minmax = {"min":arr[0],"max":arr[-1]}
    return minmax
arr = [1000,11,445,1,330,3000]
minmax = getMinMax(arr)
print("Minimum element is", minmax["min"])
print("Maximum element is", minmax["max"])
'''
Output:
-------------------------
Minimum element is 1
Maximum element is 3000
-------------------------
'''
'''
Complexity Analysis:

The time complexity of this approach is O(n log n), 
where n is the number of elements in the array, 
as we are using a sorting algorithm. 
The space complexity is O(1), as we are not using any extra space.

Number of Comparisons:

The number of comparisons made to find the minimum and maximum elements 
is equal to the number of comparisons made during the sorting process. 
For any comparison-based sorting algorithm, 
the minimum number of comparisons required to sort an array of n elements is O(n log n). 
Hence, the number of comparisons made in this approach is also O(n log n).
'''