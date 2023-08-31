'''
Given an array of intergers nums whichs is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise return -1. 

You must write an algorithm with O(log n) runtime complexity

input params = nums -> array of integers
               target -> integer

output = index -> integer 

'''

# O(log n) time | O(1) space 

def binarySearch(nums: list, target: int) -> int:

    startIdx = 0
    endIdx = len(nums) - 1
    
    while startIdx < endIdx:
        middleIdx = (startIdx + endIdx) // 2
        if target == nums[middleIdx]:
            return middleIdx
        elif target < nums[middleIdx]:
            endIdx = middleIdx - 1
        elif target > nums[middleIdx]:
            startIdx = middleIdx + 1
    
    return -1


nums = [1, 4, 5, 6, 8, 10, 11]
target = 10

print(binarySearch(nums, target))