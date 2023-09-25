'''
Three sum 

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

'''

# O(n^2) time | O(n) space

def threeSum(nums:list[int]) -> list[list[int]]:
    
    nums.sort()

    result = []

    for i in range(len(nums) - 2):
        leftIdx = i+1
        rightIdx = len(nums) - 1

        while leftIdx < rightIdx:
            currentSum = nums[i] +  nums[leftIdx] + nums[rightIdx]
            buffer = [nums[i], nums[leftIdx], nums[rightIdx]]
            if currentSum == 0:
                if buffer not in result:
                    result.append([nums[i], nums[leftIdx], nums[rightIdx]])
                left += 1
                right -= 1
            elif currentSum < 0:
                left += 1
            elif currentSum > 0:
                right -= 1

    
    return result

nums = [-1,0,1,2,-1,-4]
