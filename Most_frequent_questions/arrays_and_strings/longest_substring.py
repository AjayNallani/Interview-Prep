'''
Longest substring without repeating characters 

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. 


'''

def longestSubstringWithoutRepeating(s:str) -> str:
    lastSeen = {}
    longest =[0, 1]
    startIdx = 0

    for i, char in enumerate(s):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i+1]

        lastSeen[char] = i

    return s[longest[0]:longest[1]]

s = 'pwwkew'

print(longestSubstringWithoutRepeating(s))

