def kthSmallest(arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        return sorted(arr)[k-1]
arr = [7,10,4,3,20,15]
print("Kth Smallest Element: ",kthSmallest(arr,0,len(arr)-1,3))