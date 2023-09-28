# Time Complexity: O(m+n)*O(log (m+n)), the outer loop runs from m+n to 1 and its everytime divided by 1. 
# So, outer loop complexity is O(log(m+n)). The inner loop time complexity is O(m+n).
# Space Complexity: O(1), as no extra space is used.
def merge(arr1,arr2,m,n):
    len_arr = m+n
    gap = len_arr//2+(len_arr%2)
    while gap>0:
        left , right = 0 , gap
        while right < len_arr:
            # If left and right pointer is in arr1[]
            if left < m and right < m:
                if(arr1[left]>arr1[right]):
                    arr1[left],arr1[right]=arr1[right],arr1[left]
                # self.swapIfGreater(arr1,arr1,left,right)
            # If left pointer is in arr1[] and right in arr2[]
            elif left < m and right >=m:
                if(arr1[left]>arr2[right-m]):
                    arr1[left],arr2[right-m]=arr2[right-m],arr1[left]
                # self.swapIfGreater(arr1,arr2,left,right-m)
            # If left and right pointers are in arr2[]
            else:
                if(arr2[left-m]>arr2[right-m]):
                    arr2[left-m],arr2[right-m]=arr2[right-m],arr2[left-m]
                # self.swapIfGreater(arr2,arr2,left-m,right-m)
            left+=1
            right+=1
        if gap == 1:
            break
        # Decrement the gap value as the right reaches the end
        # And no more comparision to do
        gap = (gap//2) + (gap%2)
    print(arr1,arr2)
merge([1, 5, 9, 10, 15, 20],[2, 3, 8, 13],6,4)