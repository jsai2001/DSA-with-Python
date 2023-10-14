# Time Complexity : O(n)
# Space Complexity : O(1)
def maxProduct(arr,n):
    if(len(arr)==0):
        return 0
    max_pro,min_pro=arr[0],arr[0]
    result=max_pro
    for i in range(1,len(arr)):
        curr=arr[i]
        temp_max=max(curr, curr*max_pro , curr*min_pro)
        min_pro=min(curr, curr*max_pro , curr*min_pro)
        max_pro=temp_max
        result=max(max_pro, result)
    return result
arr=[-2,3,-4]
n=len(arr)
print(maxProduct(arr,n))