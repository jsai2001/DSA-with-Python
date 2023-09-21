# Three Way Partitioning method
def sort012(arr,n):
    # code here
    low = mid = 0
    high = len(arr)-1
    while mid<=high:
        if(arr[mid]==0):
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif(arr[mid]==1):
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr
print(sort012([0,1,2,0,0,1,2,1,0,1],10))
'''
Time Complexity: O(N), where N = size of the given array. We are using a single loop that can run at most N times.
Space Complexity: O(1) as we are not using any extra space.

Solving this method using count sort takes
Time Complexity: O(N) + O(N), where N = size of the array. First O(N) for counting the number of 0’s, 1’s, 2’s, 
and second O(N) for placing them correctly in the original array.
Space Complexity: O(1) as we are not using any extra space.
'''