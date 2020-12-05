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
    seatIds.append(row_start * 8 + col_start)

print(max(seatIds))
