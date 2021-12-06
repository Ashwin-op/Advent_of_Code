def points_between(points):
    points = []
    x1, x2, y1, y2 = line[0][0], line[1][0], line[0][1], line[1][1]
    if x1 == x2:  # horizontal vents
        if y1 > y2:
            while y2 <= y1:
                points.append([x1, y2])
                y2 += 1
        else:  # y1 < y2
            while y1 <= y2:
                points.append([x1, y1])
                y1 += 1
    elif y1 == y2:  # vertical vents
        if x1 > x2:
            while x2 <= x1:
                points.append([x2, y1])
                x2 += 1
        else:  # x1 < x2
            while x1 <= x2:
                points.append([x1, y1])
                x1 += 1
    else:  # diagonal vents
        if x1 < x2 and y1 < y2:
            while x1 <= x2:
                points.append([x1, y1])
                x1 += 1
                y1 += 1
        elif x1 > x2 and y1 < y2:
            while x1 >= x2:
                points.append([x1, y1])
                x1 -= 1
                y1 += 1
        elif x1 > x2 and y1 > y2:
            while x1 >= x2:
                points.append([x1, y1])
                x1 -= 1
                y1 -= 1
        elif x1 < x2 and y1 > y2:
            while x1 <= x2:
                points.append([x1, y1])
                x1 += 1
                y1 -= 1
    return points


lines = []

with open("input.txt") as file:
    for line in file.readlines():
        lines.append(
            [list(map(int, line.split(",")))
             for line in line.strip().split(" -> ")]
        )

map = [[0]*1000 for i in range(1000)]

for line in lines:
    for point in points_between(line):
        map[point[0]][point[1]] += 1

counter = sum(map[i][j] >= 2 for i in range(1000) for j in range(1000))

print(counter)
