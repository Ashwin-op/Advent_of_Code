with open("input.txt") as fp:
    matrix = [i.strip() for i in fp.readlines()]

height = len(matrix)
width = len(matrix[0])
row = 0
col = 0

trees = 0
while row < height and col <= width:
    if matrix[row][col] == '#':
        trees += 1

    col = (col + 3) % width
    row += 1

print(trees)
