'''
Find and return the nth row of pascal's traingle in the form of a list. n is 0-based

for example if n is 4 then output = [1, 4, 6, 4, 1]

0        1          1
1       1 1         2
2      1 2 1        3
3     1 3 3 1       4
4    1 4 6 4 1      5

'''

def pascal_triangle(num_rows: int) -> list:

    traingle = [[1]]
    for i in range(num_rows-1):
        temp = [0] + traingle[-1] + [0]
        row = []

        for j in range(len(traingle[-1]) + 1):
            row.append(temp[j] + temp[j+1])

        traingle.append(row)

    return traingle   

num_rows = 4

print(pascal_triangle(num_rows)[num_rows - 1])
