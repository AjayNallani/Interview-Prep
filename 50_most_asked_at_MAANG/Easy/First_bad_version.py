'''
First Bad Version 

Suppose you have n versions [1, 2, 3, 4, 5,......, n] and you want to find out the first bad one, which causes all the following 
one to be bad 

you are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version 

'''

def isBadVersion(version) -> bool:

    return 

def firstBadVersion(versions: list) -> int:
    left = 0 
    right = len(versions) - 1

    result = 0

    while left <= right:
        middle = (left + right) // 2

        if versions[middle] == 'b':
            result = middle
            right = middle - 1
        else:
            left = middle + 1
    
    return result

versions = ['g', 'g', 'g', 'g', 'b', 'b', 'b']

print(firstBadVersion(versions))