'''
Write a function to determine if two strings are anagrams to each other. 

An anagram is a word that is formed by rearranging the letters of another word 

'''

def anagram_checker(str1, str2):
    str1.lower()
    str2.lower()

    if sorted(str1) == sorted(str2):
        return True

    return False


str1 = 'rat'
str2 = 'arat'

print(anagram_checker(str1, str2))