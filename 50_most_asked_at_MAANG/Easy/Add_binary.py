'''
Given two binary strings a and b return their sum as a binary string s

constraints:
    1 <= a.length, b.length <= 10^4
    a and b only consists of 1 and 0 characters
    Each string does not contain leading zeros except for the zero itself
'''

# time complexity - O(max(M, N)) -> M, N being the sizes of a, b

def addBinary(a: str, b: str) -> str:
    
    # variables to store the result string and carry 
    res = ''
    carry = 0

    # reverse the strings as we calculate from right hand side
    a, b  = a[::-1], b[::-1]

    # since the input strings may not be of equal size we take max size between a and b
    for i in range(max(len(a), len(b))):

        # for each digit value taking the ascii value and converting it to integer 
        digitA = ord(a[i]) - ord('0') if i < len(a) else 0
        digitB = ord(b[i]) - ord('0') if i < len(b) else 0

        total = digitA + digitB + carry
        char = str(total % 2)
        res = char + res
        carry = total // 2

    # boundary condition when there are not more digits left to calulcate but there is a carry left
    if carry:
        res = '1' + res

    return res


# test cases 
a = '1010'
b = '1011'

result = addBinary(a, b)

print(result)