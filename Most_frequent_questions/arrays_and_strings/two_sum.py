'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example - 
    nums = [2, 7, 11, 15], target = 9 
    output = [0, 1]

    Explanation : nums[0] + nums[1] == 9, we return [0, 1]

'''

# O(nlogn) time | O(1) space , n being the length of the list 
def twoSum(nums:list[int], target:int) -> list[int]:
    
    nums.sort()

    left = 0
    right = len(nums) - 1

    while left < right:
        currentSum = nums[left] + nums[right]
        print(left, right, nums[left], nums[right], currentSum, target)
        if currentSum == target:
            return[left, right]
        elif currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1
    
    return []

nums = [2, 3, 4]
target = 7

print(twoSum(nums, target))


