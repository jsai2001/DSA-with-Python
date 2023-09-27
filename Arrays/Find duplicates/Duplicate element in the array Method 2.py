# Time Complexity O(n)
# Space Complexity O(1)

# Optimized than Method 1
def findDuplicate(nums):
    for i in range(len(nums)):
        if nums[abs(nums[i])]<0:
            return abs(nums[i])
        nums[abs(nums[i])]*=-1
print(findDuplicate([1, 3, 4, 2, 2]))