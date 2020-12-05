options = {
    'F': lambda x: x/2,
    'B': lambda x: x,
    'R': lambda x: x,
    'L': lambda x: x/2
}

with open("input.txt") as fp:
    seats = [i.strip() for i in fp.readlines()]

seatIds = []
for seat in seats:
    row_start = 0
    row_end = 127
    col_start = 0
    col_end = 7
    for op in seat:
        if op == 'F':
            row_end = row_start + int((row_end-row_start) / 2)
        elif op == 'B':
            row_start += int((row_end-row_start) / 2) + 1
        elif op == 'L':
            col_end = col_start + int((col_end-col_start) / 2)
        elif op == 'R':
            col_start += int((col_end-col_start) / 2) + 1
    seatIds.append((row_start, col_start))

seatIds.sort()
print(seatIds)


for i in range(seatIds[0][0], seatIds[-1][0]):
    for j in range(8):
        if (i, j) not in seatIds:
            print(i, j)
