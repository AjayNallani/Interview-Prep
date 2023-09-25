'''
You have been given an array of length n. The array contains integers from 0 to n-2. Each number in the array is present is present 
exactly once except for one number which is present twice. Find and return this duplicate number in the array 

arr = [0, 2, 3, 1, 4, 5, 3]
output = 3

'''

def findDuplicate(arr:list) ->  int:
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]

        
    return 

arr = [0, 2, 3, 1, 4, 5, 3]
print(findDuplicate(arr))