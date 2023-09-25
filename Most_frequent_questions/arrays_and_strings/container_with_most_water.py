'''
Container with most water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the 
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

'''

def waterArea(heights:list[int]) -> int:
    
    if len(heights) == 0:
        return 0
    
    leftIdx = 0
    rightIdx = len(heights) - 1
    maxArea = 0

    while leftIdx < rightIdx:
        currentArea = min(heights[leftIdx], heights[rightIdx]) * (rightIdx - leftIdx)

        maxArea = max(maxArea, currentArea)

        if heights[leftIdx] < heights[rightIdx]:
            leftIdx += 1
        else:
            rightIdx -= 1

    return maxArea

heights = [1,8,6,2,5,4,8,3,7]

print(waterArea(heights))