'''
Given a sentence, reverse each word in a sentence while keeping the order same 

'''

def string_reverse(string):

    right = len(string) - 1
    new_string = ''
    while (right >= 0):
        new_string = new_string + string[right]
        right -= 1

    return new_string

def word_flipper(string):
    stringList = string.split(' ')

    for i in range(len(stringList)):
        stringList[i] = string_reverse(stringList[i])
    
    
    return ' '.join(stringList)

string = 'this is an example!'

print(word_flipper(string))