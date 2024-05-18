# Time Complexity: O(log n)
# Space Complexity: O(1)
"""
To solve this problem, we need to implement an algorithm that efficiently finds the target in a rotated sorted array. 
Given the requirement of O(log n) time complexity, we should use a modified binary search approach. 

Here’s the step-by-step solution:

Key Observations
Array Characteristics: The array is originally sorted but may be rotated at an unknown pivot.
Binary Search Adaptation: A standard binary search has O(log n) complexity, but due to the rotation, we need to adjust our comparisons to correctly find the target.

Steps to Solve the Problem

Initialize Pointers: Start with two pointers, left and right, at the beginning and end of the array.
Binary Search Loop:
    Compute the mid index.
    Check if the element at mid is the target. If yes, return mid.
    Determine whether the left or right half is properly sorted.
    Depending on the sorted half and where the target lies, adjust the left and right pointers to narrow down the search range.

Exit Condition: If the target is found, return its index; if the loop completes without finding the target, return -1.

Detailed Implementation
Here’s the Python code that implements the above logic:
"""
def search(nums, target):
    left, right = 0, nums.length - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if the mid element is the target
        if nums[mid] == target:
            return mid
        
        # Determine which half is properly sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1  # Target not found

# Example Usage
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))  # Output: 4
"""
Explanation of the Code

Initialization: The left pointer starts at the beginning of the array, and the right pointer starts at the end.
Binary Search Loop:
    Calculate the middle index (mid).
    If the middle element is the target, return mid.
    Check if the left half (nums[left] to nums[mid]) is sorted:
        If sorted and the target lies within this range, adjust the right pointer to mid - 1.
        Otherwise, adjust the left pointer to mid + 1.
    If the right half (nums[mid] to nums[right]) is sorted:
        If sorted and the target lies within this range, adjust the left pointer to mid + 1.
        Otherwise, adjust the right pointer to mid - 1.
Return Value: If the target is found, return its index; otherwise, return -1.
This approach ensures that each step reduces the search space by half, maintaining the O(log n) time complexity.
"""
