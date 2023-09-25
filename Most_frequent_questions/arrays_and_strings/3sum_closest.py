'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

'''


def threeSumClosest(self, nums: List[int], target: int) -> int:
     
        diff = float('inf')
        nums.sort()
        
        for i in range(len(nums) - 2):
            leftIdx = i+1
            rightIdx = len(nums) -  1
            
            while leftIdx <  rightIdx:
                currentSum = nums[i] + nums[leftIdx] + nums[rightIdx]
                if abs(target - currentSum) < abs(diff):
                    diff = target - currentSum
                if currentSum < target:
                    leftIdx += 1
                else:
                    rightIdx -= 1
                
                if diff == 0:
                    break
        return target - diff

nums = [-1,2,1,-4]

target = 1

print(threeSumClosest(nums, target))