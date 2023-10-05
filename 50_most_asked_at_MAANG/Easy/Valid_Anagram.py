'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise 


An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original 
letters exactly once 

'''

def validAnagrams(s:str, t:str) -> bool:
    
    if sorted(s) == sorted(t):
        return True
    return False

s  = 'art'
t = 'tart'

print(validAnagrams(s, t))

