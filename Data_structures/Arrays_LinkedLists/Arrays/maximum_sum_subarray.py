'''
You have been given an array containing numbers. Find and return the largest sum in a contiguous subarray within the input array

arr = [1, 2, 3, -4, 6]
the largest sum is 8, which is the sum of all elements in the array 


'''

def maxSum(arr:list) -> int:
    sum = -float('inf')
    buffer = 0
    for i in range(len(arr)):
        
        buffer = buffer + arr[i]
        for j in range(i+1, len(arr)):
            buffer = buffer + arr[j]
        
        sum = max(sum, buffer)
        buffer = 0

    return sum

arr = [1, 2, 3, -4, 6]

arr1 = [1, 2, -5, -4, 1, 6]

print(maxSum(arr1))
