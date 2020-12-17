import math
import copy
import itertools


with open('input.txt') as fp:
    lines = [list(i.strip()) for i in fp.readlines()]


def count_active_neighbors(x, y, z, w, active_set):
    count = 0
    for x1, y1, z1, w1 in itertools.product([-1, 0, 1], repeat=4):
        if not x1 and not y1 and not z1 and not w1:
            continue
        if (x + x1, y + y1, z + z1, w + w1) in active_set:
            count += 1
    return count


active_coords = set()

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "#":
            active_coords.add((j, i, 0, 0))

for p in range(6):
    temp_set = copy.deepcopy(active_coords)

    mins = [math.inf, math.inf, math.inf, math.inf]
    maxes = [-math.inf, -math.inf, -math.inf, -math.inf]
    for coord in active_coords:
        mins = [min(x, y) for x, y in zip(coord, mins)]
        maxes = [max(x, y) for x, y in zip(coord, maxes)]

    mins = [x - 1 for x in mins]
    maxes = [x + 1 for x in maxes]

    for x in range(mins[0], maxes[0] + 1):
        for y in range(mins[1], maxes[1] + 1):
            for z in range(mins[2], maxes[2] + 1):
                for w in range(mins[3], maxes[3] + 1):
                    active_neighbor_count = count_active_neighbors(
                        x, y, z, w, active_coords)
                    if (x, y, z, w) in active_coords:
                        if active_neighbor_count != 2 and active_neighbor_count != 3:
                            temp_set.remove((x, y, z, w))
                    else:
                        if active_neighbor_count == 3:
                            temp_set.add((x, y, z, w))

    active_coords = temp_set

print(len(active_coords))
