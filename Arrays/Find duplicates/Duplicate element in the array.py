def findDuplicate(nums):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            return nums[i]
print(findDuplicate([3,1,3,4,2]))