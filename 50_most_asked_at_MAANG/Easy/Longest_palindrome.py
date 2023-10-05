'''
Longest Palindrom 

Given a string s which consists of lowercase or uppercase letters, return the length of the longest padlindrom that can be built with those
letters 

letters are case sensitive, for example "Aa" is not considered a palindrome here. 

'''

def longestPalindrome(s:str) -> int:
    singles = set()
    length = 0

    for char in s:
        if char in singles:
            singles.remove(char)
            length += 2
        else:
            singles.add(char)

    if len(singles):
        length += 1
    
    return length

s = 'abccccddd'

print(longestPalindrome(s))
