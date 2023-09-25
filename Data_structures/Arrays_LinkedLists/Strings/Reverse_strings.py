'''
Given an input string, reverse it. 

'''

def reverse_strings(my_string:str) -> str:
    reverse_string = ''

    right = len(my_string) - 1
    while(right >= 0):
        reverse_string = reverse_string + my_string[right]
        right -= 1

    return reverse_string

my_string = 'water'

print(reverse_strings(my_string))

