'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

'''
def twoSum(nums:list[int], target:int) -> list[int]:
    nums.sort()

    left = 0 
    right = len(nums) - 1

    while left < right:
        result = nums[left] + nums[right]

        print(result, nums[left], nums[right], left, right)

        if result == target:
            return [left, right]
        elif result < target:
            left += 1
        elif result > target:
            right -= 1
        
    
    return []

nums = [2,7,11,15]
nums1 = [4, 2, 4]
target = 6

print(twoSum(nums1, target))