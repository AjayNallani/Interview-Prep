'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''
def arrayProduct(nums:list[int]) -> list[int]:
    
    products = [1] * len(nums)

    leftRunningProduct = 1
    for i in range(len(nums)):
        products[i] = leftRunningProduct
        leftRunningProduct *= nums[i]
    
    rightRunningProduct = 1
    for i in reversed(range(len(nums))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= nums[i]

    return products
nums = [1,2,3,4]

print(arrayProduct(nums))