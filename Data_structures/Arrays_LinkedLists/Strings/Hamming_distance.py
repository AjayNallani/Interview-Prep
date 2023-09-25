'''
In information theory, the hamming distance between two strings of equal length is the number of positions at which the 
corresponding symbols are different. 

'''

def hamming_distance(str1, str2):
    
    hamming_distance = 0 

    if len(str1) != len(str2):
        return hamming_distance

    for i, char in enumerate(str1):
        if str1[i] != str2[i]:
            hamming_distance += 1
    
    return hamming_distance

str1 = 'abcdefgh'
str2 = 'abbddfggs'

print(hamming_distance(str1, str2))