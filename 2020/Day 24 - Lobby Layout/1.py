import re


def move(coord, step):
    x, y = coord
    if step == "e":
        return (x + 1, y)
    elif step == "w":
        return (x - 1, y)
    elif step == "ne":
        return (x if y % 2 == 0 else x + 1, y + 1)
    elif step == "nw":
        return (x - 1 if y % 2 == 0 else x, y + 1)
    elif step == "se":
        return (x if y % 2 == 0 else x + 1, y - 1)
    elif step == "sw":
        return (x - 1 if y % 2 == 0 else x, y - 1)


with open("input.txt") as fp:
    lines = [re.findall(r"(nw|ne|sw|se|w|e)", line) for line in fp]

black = set()
for line in lines:
    point = (0, 0)
    for step in line:
        point = move(point, step)
    if point in black:
        black.remove(point)
    else:
        black.add(point)

print(len(black))
