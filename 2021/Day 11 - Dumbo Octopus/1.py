from collections import deque


with open("input.txt") as f:
    grid = [list(map(int, list(l.strip()))) for l in f.readlines()]

flashes = 0
ready = deque()

deltas = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]

for _ in range(100):
    trig = set()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] += 1
            if grid[x][y] > 9:
                ready.append((x, y))
                trig.add((x, y))

    while ready:
        nx, ny = ready.popleft()
        for dx, dy in deltas:
            if 0 <= nx+dx < len(grid) and 0 <= ny+dy < len(grid[0]):
                grid[nx+dx][ny+dy] += 1
                if grid[nx+dx][ny+dy] > 9 and (nx+dx, ny+dy) not in trig:
                    ready.append((nx+dx, ny+dy))
                    trig.add((nx+dx, ny+dy))

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] > 9:
                grid[x][y] = 0
                flashes += 1

print(flashes)
