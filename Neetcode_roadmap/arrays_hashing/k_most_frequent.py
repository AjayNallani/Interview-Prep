'''

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
'''

def mostFrequent(nums: list[int], k:int) -> list[int]:
    counter = {}

    result = []
    for i in nums:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    print(counter)
    for i in counter:
        if counter[i] >= k:
            result.append(i)

    return result

nums = [1,1,1,2,2,3]
k = 2

print(mostFrequent(nums, k))