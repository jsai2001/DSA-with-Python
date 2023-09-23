'''
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''
def rotate(arr, n):
    last=arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=last
    return arr
print(rotate([9, 8, 7, 6, 4, 2, 1, 3],8))