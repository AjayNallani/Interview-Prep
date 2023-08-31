'''
Flood fill 
An image is represented by an mxn integer grid image where image[i][j] represents the pixel value of the image

you are also given three integers sr, sc and color. you should perform a flood fill on the image starting from the pixel image[sr][sc]

to perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color
as the starting pixel, plus any pixels connected 4-directionally to those pixels(also with the same color) and so on. Replace the color of all the 
aforementioned pixels with color 

Return the modifier image after performing the flood fill 

'''


def floodfill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    startColor= image[sr][sc]

    def dfs(x, y):
        if x<0 or x >= len(image):
            return 
        if y<0 or y >= len(image[0]):
            return
        
        if image[x][y] == color:
            return 
        if image[x][y] != startColor:
            return 

        image[x][y] = color

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

    dfs(sr, sc)
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

image_mod = floodfill(image, sr, sc, color)

for i in range(len(image_mod)):
    for j in range(len(image_mod[0])):
        print(image_mod[i][j])
    print('\n')
