'''
you are given a non-negative number in the form of list elements. For example, the number 123 would be provided as [1, 2, 3]. 
Add one to the number and return in the form of a new list

'''
def AddOne(input:list) -> list:
    numStr = ''
    for i in input:
        numStr = numStr + str(i)
    
    finalStr = str(int(numStr) + 1)

    return [int(char) for char in finalStr]

input = [1, 2, 3]

print(AddOne(input))