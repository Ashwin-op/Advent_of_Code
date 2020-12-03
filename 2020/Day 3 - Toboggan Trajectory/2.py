import math


with open("input.txt") as fp:
    matrix = [i.strip() for i in fp.readlines()]

height = len(matrix)
width = len(matrix[0])
row = 0
col = 0


def findTrees(matrix, height, width,  row, col, rowJump, colJump):
    trees = 0
    while row < height and col <= width:
        if matrix[row][col] == '#':
            trees += 1

        col = (col + colJump) % width
        row += rowJump

    return trees


ans = 1
for (i, j) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    ans *= findTrees(matrix, height, width, row, col, j, i)

print(ans)
