# Time Complexity: O(n)
# Space Complexity: O(1)
def nextPermutation(nums):
    index=-1
    n = len(nums)
    for i in range(n-1,0,-1):
        if(nums[i]>nums[i-1]):
            index = i
            break
    if(index==-1):
        nums.reverse()
    else:
        prev = index
        for i in range(index+1,n):
            if nums[i]>nums[index-1] and nums[i]<=nums[prev]:
                prev = i
        nums[index-1],nums[prev] = nums[prev],nums[index-1]
        nums[index:]=reversed(nums[index:])
    return nums
print(nextPermutation([1,1,5]))
