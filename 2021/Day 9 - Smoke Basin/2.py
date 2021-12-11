from functools import reduce
from operator import mul

with open("input.txt") as f:
    plan = {}
    for v, row in enumerate(f.readlines()):
        for h, cell in enumerate(row.strip()):
            plan[(v, h)] = int(cell)


def get_neighbors(point):
    (h, v) = point
    yield (h + 1, v)
    yield (h - 1, v)
    yield (h, v + 1)
    yield (h, v - 1)


def get_lowpoints(plan):
    return [
        (pos, val)
        for pos, val in plan.items()
        if all(plan[n] > val for n in get_neighbors(pos) if n in plan)
    ]


def get_basin_size(start):
    seen = set([start])
    to_process = [start]
    while to_process:
        cur = to_process.pop()
        for n in get_neighbors(cur):
            if n in plan and n not in seen and plan[n] != 9:
                seen.add(n)
                to_process.append(n)
    return len(seen)


lowpoints = [point for point, _ in get_lowpoints(plan)]
basin_sizes = list(map(get_basin_size, lowpoints))
basin_sizes.sort(reverse=True)

print(reduce(mul, basin_sizes[0:3]))
